#!/bin/env python
import asyncio
import sender
import time
from OSCreceiver import OSCServerThread
from predictor import IMUPredictor

async def main():
    global s
    s = sender.sender()
    print("sender init")
    await s.setup()
    print("sender setup")
    print(f"SlimeVR server is at {s.get_slimevr_ip()}")
    await s.create_imu(1)
    await s.create_imu(2)
    print("sender imu init")
    await s.set_rotation(1,0,0,0)
    await s.set_rotation(2,0,0,0)
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
    predict=IMUPredictor("imu_model.pkl")
    while True:
        rotations=osc_server_thread.get_tracker_rotations()
        preprocessed={
            "hip":rotations["hip"],
            "chest":rotations["chest"],
            "feetl":rotations["feetl"],
            "feetr":rotations["feetr"]
        }
        newdata=predict.predict(preprocessed)
        asyncio.run(s.set_rotation(1,newdata[0][0],newdata[0][1],newdata[0][2]))
        asyncio.run(s.set_rotation(2,newdata[1][0],newdata[1][1],newdata[1][2]))
        #print(newdata)
        
