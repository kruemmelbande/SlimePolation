import socket
import struct
import asyncio
import time
from packetbuilder import packetbuilder  # Assuming packetbuilder.py is in the same directory

class UDPHandler:
    def __init__(self):
        self.packet_builder = packetbuilder()

        # Can be any non-bound port.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0", 21201))

        self.slimevr_port = 6969
        self.broadcast_ip = "localhost"
        self.slimevr_ip = self.broadcast_ip
        #self.slimevr_ip = "127.0.0.1"
        #self.slimevr_ip = "127.0.0.1"
    async def heartbeat(self):
        while True:
            if self.slimevr_ip != self.broadcast_ip:
                await self.send_packet(self.packet_builder.heartbeat_packet)
                print("sent heartbeat")
            await asyncio.sleep(0.8)  # At least 1 time per second (<1000ms)

    async def handshake(self, imu_type, board_type, mcu_type):
        print("Send handshake packet..")
        #self.slimevr_ip = self.broadcast_ip
        self.slimevr_ip = "127.0.0.1"
        self.broadcast_ip = "127.0.0.1"
        result = ""
        while result == "":
            await self.send_packet(self.packet_builder.build_handshake_packet(imu_type, board_type, mcu_type))
            print("Sent packet to server...")
            #result = await self.listen_for_handshake()
            print("Waiting for server")
            await asyncio.sleep(0.5)
            result= "127.0.0.1"
            self.broadcast_ip="255.255.255.255"
        print("Server found")
        print("possibly...")
        
        return f"Found server:\n{result}"

    async def add_imu(self, imu_type):
        print("Send add imu packet")
        # if self.slimevr_ip == self.broadcast_ip:
        #     return "Server not found"
        await self.send_packet(self.packet_builder.build_imu_packet(1,[0,0,0,0]))
        return "Added IMU"

    async def rotate_imu(self, imu_id, rotation):
        print("Send rotation packet")
        # if self.slimevr_ip == self.broadcast_ip:
        #     return "Server not found"
        await self.send_packet(self.packet_builder.build_rotation_packet(imu_id, rotation))
        return f"Rotated IMU {imu_id}"

    async def send_packet(self, packet):
        print(packet)
        print((self.slimevr_ip, self.slimevr_port))
        self.socket.sendto(packet, (self.slimevr_ip, self.slimevr_port))

    async def listen_for_handshake(self):
        now=time.time()
        while time.time()-now < 30:
            received, addr = self.socket.recvfrom(1024)
            received_message = received.decode('utf-8', 'ignore')
            print(received_message)
            if "Hey OVR =D 5" in received_message:
                self.slimevr_ip = addr[0]
                return self.slimevr_ip
        print("Unable to find server, assuming localhost")
        return "127.0.0.1"  