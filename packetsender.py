import socket
import struct
import asyncio
from packetbuilder import packetbuilder  # Assuming packetbuilder.py is in the same directory

class UDPHandler:
    def __init__(self):
        self.packet_builder = packetbuilder()

        # Can be any non-bound port.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0", 21201))

        self.slimevr_port = 6969
        self.broadcast_ip = "255.255.255.255"
        self.slimevr_ip = self.broadcast_ip
        #self.slimevr_ip = "127.0.0.1"
    async def heartbeat(self):
        while True:
            if self.slimevr_ip != self.broadcast_ip:
                await self.send_packet(self.packet_builder.heartbeat_packet)
                print("sent heartbeat")
            await asyncio.sleep(0.8)  # At least 1 time per second (<1000ms)

    async def handshake(self, imu_type, board_type, mcu_type):
        self.slimevr_ip = self.broadcast_ip
        result = ""
        while result == "":
            await self.send_packet(self.packet_builder.build_handshake_packet(imu_type, board_type, mcu_type))
            result = await self.listen_for_handshake()
            print("Waiting for server")
            await asyncio.sleep(0.5)
        print("Server found")
        return f"Found server:\n{result}"

    async def add_imu(self, imu_type):
        if self.slimevr_ip == self.broadcast_ip:
            return "Server not found"
        await self.send_packet(self.packet_builder.build_imu_packet(imu_type))
        return "Added IMU"

    async def rotate_imu(self, imu_id, rotation):
        if self.slimevr_ip == self.broadcast_ip:
            return "Server not found"
        await self.send_packet(self.packet_builder.build_rotation_packet(imu_id, rotation))
        return f"Rotated IMU {imu_id}"

    async def send_packet(self, packet):
        self.socket.sendto(packet, (self.slimevr_ip, self.slimevr_port))

    async def listen_for_handshake(self):
        while True:
            received, addr = self.socket.recvfrom(1024)
            received_message = received.decode('utf-8', 'ignore')
            if "Hey OVR =D 5" in received_message:
                self.slimevr_ip = addr[0]
                return self.slimevr_ip
