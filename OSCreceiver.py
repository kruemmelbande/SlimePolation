from pythonosc import dispatcher
from pythonosc import osc_server
import threading

class OSCServerThread(threading.Thread):
    def __init__(self, address=("127.0.0.1", 9000)):
        super().__init__()
        self.address = address
        self.trackerrotations = {
            "feetl": (0., 0., 0.),
            "feetr": (0., 0., 0.),
            "hip": (0., 0., 0.),
            "chest" : (0., 0., 0.),
            "legr":(0., 0., 0.), 
            "legl":(0., 0., 0.) 
        }
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.set_default_handler(self.handleosc)

    def handleosc(self, address, *args):
        """
        TrackerPosition.HIP -> 1
        TrackerPosition.LEFT_FOOT -> 2
        TrackerPosition.RIGHT_FOOT -> 3
        TrackerPosition.LEFT_UPPER_LEG -> 4
        TrackerPosition.RIGHT_UPPER_LEG -> 5
        TrackerPosition.UPPER_CHEST -> 6
        TrackerPosition.LEFT_UPPER_ARM -> 7
        TrackerPosition.RIGHT_UPPER_ARM -> 8
        """
        global trackerrotations
        if address.startswith("/tracking/trackers") and address.endswith("rotation"):
            trackernumber = address.replace("/tracking/trackers/", "").replace("/rotation", "")
            if trackernumber == "head":
                return
            elif trackernumber == "1":
                self.trackerrotations["hip"] = args  # Updated key name
            elif trackernumber == "2":
                self.trackerrotations["feetl"] = args
            elif trackernumber == "3":
                self.trackerrotations["feetr"] = args
            elif trackernumber == "4":
                self.trackerrotations["legl"] = args
            elif trackernumber == "5":
                self.trackerrotations["legr"] = args
            elif trackernumber == "6":
                self.trackerrotations["chest"] = args


    def run(self):
        self.server = osc_server.ThreadingOSCUDPServer(self.address, self.dispatcher)
        print("Server listening on {}".format(self.server.server_address))
        self.server.serve_forever()

    def get_tracker_rotations(self):
        return self.trackerrotations