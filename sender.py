import asyncio
from packetsender import UDPHandler
import math
import threading
class sender:
    def __init__(self):
        self.udp_handler = UDPHandler()
    
        class Quaternion:
            def __init__(self, x, y, z):
                # Calculate the half angles
                half_x = math.radians(x) / 2
                half_y = math.radians(y) / 2
                half_z = math.radians(z) / 2
                
                # Calculate sin and cos of half angles
                sin_half_x = math.sin(half_x)
                sin_half_y = math.sin(half_y)
                sin_half_z = math.sin(half_z)
                cos_half_x = math.cos(half_x)
                cos_half_y = math.cos(half_y)
                cos_half_z = math.cos(half_z)
                
                # Calculate quaternion components
                self.x = sin_half_x * cos_half_y * cos_half_z - cos_half_x * sin_half_y * sin_half_z
                self.y = cos_half_x * sin_half_y * cos_half_z + sin_half_x * cos_half_y * sin_half_z
                self.z = cos_half_x * cos_half_y * sin_half_z - sin_half_x * sin_half_y * cos_half_z
                self.w = cos_half_x * cos_half_y * cos_half_z + sin_half_x * sin_half_y * sin_half_z
        self.Quaternion=Quaternion
    
    async def create_imu(self, imu_id):
        imu_task = asyncio.create_task(self.udp_handler.add_imu(imu_id))
        await imu_task

    async def send_reset(self):
        await self.udp_handler.reset()
    
    def get_slimevr_ip(self):
        return self.udp_handler.slimevr_ip
        
    async def set_rotation(self, imu_id, x, y, z):
        await self.udp_handler.rotate_imu(imu_id, self.Quaternion(x, y, z))
    
    async def setup(self):
        self.handshake_task = asyncio.create_task(self.udp_handler.handshake(1, 1, 1))
        await self.handshake_task
        
        # Start the heartbeat function in a separate thread
        heartbeat_thread = threading.Thread(target=self.heartbeat)
        heartbeat_thread.start()

    def heartbeat(self):
        asyncio.run(self.udp_handler.heartbeat())

