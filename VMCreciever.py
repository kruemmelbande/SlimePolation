import argparse
from pythonosc import udp_client, dispatcher, osc_server

def print_handler(address, *args):
    print(f"Received message from {address}: {args}")

def main(ip, port):
    dispatcher_instance = dispatcher.Dispatcher()
    dispatcher_instance.set_default_handler(print_handler)

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher_instance)
    print(f"Listening for VMC data on {ip}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read VMC data over OSC")
    parser.add_argument("--ip", default="127.0.0.1", help="The IP address to listen on")
    parser.add_argument("--port", type=int, default=39539, help="The port to listen on")
    args = parser.parse_args()

    main(args.ip, args.port)
