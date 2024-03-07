# SlimePolation
Tries to interpolate missing SlimeVr trackers using AI  
I am very much just at the prototyping phase right now, so no, this isnt ready to release yet.  
Im testing all my code on linux, and i wont explicitly be providing windows support, however, i am open to pull requests to fix any windows related issues.

Mainly doing this as a learning exercise. Im not expecting amazing results, but well see where we get.

Maybe this could be helpful to you to see an example implementation of some of the smlimevr protocols in python.

## Todo  
- [x] Send data to Slimevr Server
    - [x] Send handshake
    - [x] Send heartbeat
    - [x] Send actual imu data
    - [x] Send multiple imus
- [ ] Read data from the Slimevr Server
    - [x] Make a prototype implementation using osc
    - [ ] Decide on a proper standart (osc, vmc, solarxr)
    - [ ] Implement that
- [x] Make an ai*
- [x] Train that ai*
- [x] Make it, so i dont have to restart the slimevr server every time
    - i dont know why it did that, i dont know why it doesnt do that anymore, but it works so im not complaining
- [ ] Make a nice gui
- [ ] ????
- [ ] Profit

*the ai is currently very dumb, and does not come close to being usable.

## How to use

1. dont
2. if you really want to try this anyway, start out by running recordtrackingdata.py.
    - recordtrackingdata.py reads your motions from vrchat osc
    - make sure that osc is enabled in the slimevr server
    - after its done you will see captured_data.json
    - yes, there are errors here, ignore them
3. now its time to train the ai. For this simply run trainai.py
4. now run SlimePolation.py
5. time to regret running SlimePolation.py, because the results are currently pretty bad

## Resources that helped me
- [Slimevr Sender Example](https://github.com/SlimeVR/SlimeVR-Sender-Example/)
- The amazing people at the slimevr discord
- Caffeine

## Disclaimer
SlimePolation is an independent project and is not affiliated with or endorsed by SlimeVR.
