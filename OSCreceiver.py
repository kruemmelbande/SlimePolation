from pythonosc import dispatcher
from pythonosc import osc_server

# Define the handler function to handle incoming OSC messages
def print_message(address, *args):
    print(f"Received message from {address}: {args}")

# Create a dispatcher
dispatcher = dispatcher.Dispatcher()
dispatcher.set_default_handler(print_message)  # Set the default handler to print any received messages

# Create an OSC server and start it
server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 9000), dispatcher)
print("Server listening on {}".format(server.server_address))
server.serve_forever()  # This will keep the server running indefinitely
