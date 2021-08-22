import _thread

TARGET_TEMP_FILE = "target_temp"

class State():

    def __init__(self):
        # Temp
        self.actual_temp = 0
        self.uptime = 0
        self.sensor_init = False
        self.socket_on = False
        self.lock = _thread.allocate_lock()
        self.init_temp()

    def init_temp(self):
        # Read temp from file
        try:
            with open(TARGET_TEMP_FILE, 'r') as reader:
                self.target_temp = int(reader.read())
        except Exception:
            print("No previous target temp record, init to 35")
            self.target_temp = 35

    def save_target_temp(self, val):
        # Save target temp to file
        print("Saving target temp: ", val)
        try:
            with open(TARGET_TEMP_FILE, 'w') as writer:
                temp_string = str(val)
                writer.write(temp_string)
        except Exception:
            print("Failed to save target temp")

    def get_actual_temp(self):
        self.lock.acquire()
        val = self.actual_temp
        self.lock.release()
        return val

    def get_target_temp(self):
        self.lock.acquire()
        val = self.target_temp
        self.lock.release()
        return val

    def get_uptime(self):
        self.lock.acquire()
        val = self.uptime
        self.lock.release()
        return val

    def get_sensor_init(self):
        self.lock.acquire()
        val = self.sensor_init
        self.lock.release()
        return val

    def get_socket_on(self):
        self.lock.acquire()
        val = self.socket_on
        self.lock.release()
        return val

    def set_actual_temp(self, val):
        self.lock.acquire()
        self.actual_temp = val
        self.sensor_init = True
        self.lock.release()

    def set_target_temp(self, val):
        self.lock.acquire()
        if val != self.target_temp:
            self.target_temp = val
            self.save_target_temp(val)
        self.lock.release()

    def set_uptime(self, val):
        self.lock.acquire()
        self.uptime = val
        self.lock.release()

    def set_sensor_err(self):
        self.lock.acquire()
        self.sensor_init = False
        self.lock.release()

    def set_socket_on(self, val):
        self.lock.acquire()
        self.socket_on = val
        self.lock.release()