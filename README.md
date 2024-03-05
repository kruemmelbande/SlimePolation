# SlimePolation
Tries to interpolate missing SlimeVr trackers using AI  
I am very much just at the prototyping phase right now, so no, this isnt ready to release yet.  
Im testing all my code on linux, and i wont explicitly be providing windows support, however, i am open to pull requests to fix any windows related issues.

Mainly doing this as a learning exercise. Im not expecting amazing results, but well see where we get.

Maybe this could be helpful to you to see an example implementation of some of the smlimevr protocols in python.

## Todo  
- [ ] Send data to Slimevr Server
    - [x] Send handshake
    - [x] Send heartbeat
    - [x] Send actual imu data
    - [ ] Send multiple imus
- [ ] Read data from the Slimevr Server
- [ ] Make an ai
- [ ] Train that ai
- [ ] Make it, so i dont have to restart the slimevr server every time
- [ ] Make a nice gui
- [ ] ????
- [ ] Profit

# Resources that helped me
- [Slimevr Sender Example](https://github.com/SlimeVR/SlimeVR-Sender-Example/)
- The amazing people at the slimevr discord
- Caffeine

## Disclaimer
SlimePolation is an independent project and is not affiliated with or endorsed by SlimeVR.
