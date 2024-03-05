import asyncio
from packetsender import UDPHandler
import math
udp_handler = UDPHandler()

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


async def main():
    # Start the handshake task
    handshake_task = asyncio.create_task(udp_handler.handshake(1, 1, 1))

    # Wait for the handshake task to complete
    await handshake_task

    # Start the add_imu task after the handshake is completed
    imu_task = asyncio.create_task(udp_handler.add_imu(1))

    # Run the heartbeat task in the background
    asyncio.create_task(udp_handler.heartbeat())

    # Wait for the add_imu task to complete
    await imu_task

    # Now, you can execute other code
    while True:
        # Execute rotate_imu in a loop
        for i in range(360):
            await udp_handler.rotate_imu(1, Quaternion(0., 0., i))
            await asyncio.sleep(0.01)  # Add a delay if needed


asyncio.run(main())
