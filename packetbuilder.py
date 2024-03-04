import struct

class packetbuilder:
    def __init__(self):
        self.fw_string = "SlimeVR Sender Example"
        self.firmware_build = 17
        self.packet_id = 1
        self.imu_id = 1

    @property
    def heartbeat_packet(self):
        packet = bytearray()
        packet.extend(struct.pack('i', 0))  # putInt(0)
        return packet
    
    def build_handshake_packet(self, imu_type, board_type, mcu_type):
        packet = bytearray()
        packet.extend(struct.pack('i', 3))                                # packet 3 header
        packet.extend(struct.pack('q', self.packet_id))                  # packet counter
        packet.extend(struct.pack('i', board_type))                # Board type
        packet.extend(struct.pack('i', imu_type))                  # IMU type
        packet.extend(struct.pack('i', mcu_type))                  # MCU type
        packet.extend(struct.pack('iii', 0, 0, 0))                       # IMU info (unused)
        packet.extend(struct.pack('i', self.firmware_build))             # Firmware build
        fw_string_bytes = self.fw_string.encode('utf-8')
        packet.append(len(fw_string_bytes))                              # Length of fw string
        packet.extend(fw_string_bytes)                                   # fw string
        packet.extend(bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06]))       # MAC address
        return packet
    
    def build_imu_packet(self, imu_id, imu_type):
        self.packet_id += 1  # Increment packet counter

        packet = bytearray()
        packet.extend(struct.pack('i', 17))                                 # packet 17 header
        packet.extend(struct.pack('q', self.packet_id))                     # packet counter
        packet.append(imu_id.to_bytes(1, byteorder='little')[0])            # tracker id (shown as IMU Tracker #x in SlimeVR)
        packet.append(int(1).to_bytes(1, byteorder='little')[0])            # data type
        packet.extend(struct.pack('ffff', imu_type[0], imu_type[1], imu_type[2], imu_type[3]))  # Quaternion values
        packet.append(int(0).to_bytes(1, byteorder='little')[0])            # Calibration info
        return packet


    def build_rotation_packet(self, imu_id, rotation):
        packet = bytearray()
        packet.extend(struct.pack('i', 17))                                 # packet 17 header
        packet.extend(struct.pack('q', self.packet_id)) # packet counter
        self.packet_id+=1
        #packet.append(imu_id.to_bytes(1, byteorder='little'))               # 
        packet.extend(struct.pack('i', self.imu_id))                                 # 
        #tracker id (shown as IMU Tracker #x in SlimeVR)
        #packet.append(int(1).to_bytes(1, byteorder='little'))               # 
        packet.extend(struct.pack('i', 1))                                 # 
        
        #data type
        packet.extend(struct.pack('ffff', rotation[0], rotation[1], rotation[2], rotation[3]))  # Quaternion values
        packet.extend(struct.pack('i', 0))               # Calibration info
        return packet
