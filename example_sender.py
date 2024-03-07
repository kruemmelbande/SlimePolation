import asyncio
import sender
import time
from OSCreceiver import OSCServerThread

async def main():
    global s
    s = sender.sender()
    print("sender init")
    await s.setup()
    print("sender setup")
    print(f"SlimeVR server is at {s.get_slimevr_ip()}")
    await s.create_imu(1)
    print("sender imu init")
    await s.set_rotation(1,0,0,0)
    print("imu rotation")
    #await asyncio.sleep(4)
    await s.send_reset()
    print("yaw reset")

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
    print("a")
    osc_server_thread = OSCServerThread()
    osc_server_thread.start()
    while True:
        print(osc_server_thread.get_tracker_rotations())
        for i in range(360):
            asyncio.run(s.set_rotation(1, i, i, i))