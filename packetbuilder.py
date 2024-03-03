import struct

class packetbuilder:
    def __init__(self):
        self.fw_string = "SlimeVR Sender Example"
        self.firmware_build = 17
        self.packet_id = 1
        self.imu_id = 1

    @property
    def heartbeat_packet(self):
        return struct.pack('>I', 0)  # 28 bytes

    def build_handshake_packet(self, imu_type, board_type, mcu_type):
        fw_string_bytes = self.fw_string.encode('utf-8')
        mac_address = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])
        self.packet_id += 1
        return struct.pack(
            '>QIII{}s6s'.format(len(fw_string_bytes)),
            self.packet_id, board_type, imu_type, mcu_type,
            fw_string_bytes, mac_address
        )



    def build_imu_packet(self, imu_type):
        return struct.pack('>IBB', 15, self.packet_id, self.imu_id, imu_type)

    def build_rotation_packet(self, imu_id, rotation):
        return struct.pack('>IBBffffB', 17, self.packet_id, imu_id, 1,
                           rotation.x, rotation.y, rotation.z, rotation.w, 0)
