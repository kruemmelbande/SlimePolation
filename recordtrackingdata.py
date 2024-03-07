import json
import threading
import time
from OSCreceiver import OSCServerThread

# Global variables
data = []  # To store captured data
sampling_rate = 120  # Samples per second
duration = 120  # Duration to capture data (in seconds)
output_file = "captured_data.json"  # Output file name

# Callback function to capture data
def capture_data():
    global data
    global sampling_rate
    global duration

    osc_server_thread = OSCServerThread()
    osc_server_thread.start()

    start_time = time.time()
    while time.time() - start_time < duration:
        # Capture data from osc_server_thread
        data.append(osc_server_thread.get_tracker_rotations())
        time.sleep(1 / sampling_rate)

    osc_server_thread.stop()

# Function to dump data into a file
def dump_data_to_file():
    global data
    global output_file

    with open(output_file, "w") as f:
        json.dump(data, f)

    print("Data has been successfully saved to", output_file)

# Main function
def main():
    # Start capturing data in a separate thread
    capture_thread = threading.Thread(target=capture_data)
    capture_thread.start()

    # Wait for data capture to finish
    capture_thread.join()

    # Dump captured data to a file
    dump_data_to_file()

if __name__ == "__main__":
    main()
