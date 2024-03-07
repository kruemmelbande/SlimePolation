import struct

class packetbuilder:
    def __init__(self):
        self.fw_string = "SlimeVR Sender Example"
        self.firmware_build = 17
        self.packet_id = 1
        self.imu_id = 1

    @property
    def heartbeat_packet(self):
        heartbeat_packet = bytearray(28)
        struct.pack_into('>i', heartbeat_packet, 0, 0)
        return heartbeat_packet
    
    def reset_packet(self):
        packet = bytearray(28)
        packet[0:4] = struct.pack('>i', 21)  # packet 3 header
        return packet

    def build_handshake_packet(self, imu_type, board_type, mcu_type):
        packet = bytearray(128)
        packet[0:4] = struct.pack('>i', 3)  # packet 3 header
        packet[4:12] = struct.pack('>q', self.packet_id)  # packet counter
        packet[12:16] = struct.pack('>i', board_type)  # Board type
        packet[16:20] = struct.pack('>i', imu_type)  # IMU type
        packet[20:24] = struct.pack('>i', mcu_type)  # MCU type
        packet[24:36] = struct.pack('>3i', *[0]*3)  # IMU info (unused)
        packet[36:40] = struct.pack('>i', self.firmware_build)  # Firmware build
        fw_string_bytes = self.fw_string.encode('utf-8')
        fw_string_length = len(fw_string_bytes).to_bytes(1, byteorder='big')  # Length of fw string
        packet[40:41] = fw_string_length
        packet[41:41+len(fw_string_bytes)] = fw_string_bytes  # fw string
        packet[41+len(fw_string_bytes):47+len(fw_string_bytes)] = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])  # MAC address
        return packet


    
    def build_imu_packet(self, imu_type):
        packet = bytearray(128)
        packet[0:4] = struct.pack('>i', 15)               # packet 15 header
        packet[4:12] = struct.pack('>q', self.packet_id) # packet counter
        packet[12] = self.imu_id         # tracker id (shown as IMU Tracker #x in SlimeVR)
        packet[13] = 0                                  # sensor status
        packet[14] = imu_type                 # imu type
        self.packet_id+=1
        self.imu_id+=1
        return packet


    def build_rotation_packet(self, imu_id, rotation):
        packet = bytearray(128)
        struct.pack_into('>i', packet, 0, 17)  # Packet 17 header
        struct.pack_into('>q', packet, 4, self.packet_id)  # Packet counter
        packet[12] = imu_id & 0xFF  # Tracker id (shown as IMU Tracker #x in SlimeVR)
        packet[13] = 1  # Data type
        struct.pack_into('>ffff', packet, 14, rotation.x, rotation.y, rotation.z, rotation.w)  # Quaternion x, y, z, w
        packet[30] = 0  # Calibration info
        self.packet_id += 1
        return packet
