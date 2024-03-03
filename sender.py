import asyncio
from packetsender import UDPHandler

async def main():
    udp_handler = UDPHandler()
    await asyncio.gather(
        udp_handler.heartbeat(),
        udp_handler.handshake(1, 1, 1),
        udp_handler.add_imu(1),
        udp_handler.rotate_imu(0, (10, 20, 30))
    )

asyncio.run(main())
