import time
from display import Display
from state import State
from sensor import TempSensor
from userInput import UserInput

# Init
state = State()
display = Display(state)
temp_sensor = TempSensor(state)
user_input = UserInput(state)
start_time = time.time()

# Temperature range allowance (+- 0.5C)
TEMP_DIFF = 0.5

def uptime():
    return time.time() - start_time

def update_socket():
    if not state.get_sensor_init():
        # Temp sensor error, turn off socket
        state.set_socket_on(False)
        return
    actual_temp = state.get_actual_temp()
    target_temp = state.get_target_temp()
    if state.get_socket_on():
        if actual_temp >= (target_temp + TEMP_DIFF):
            # Turn off
            state.set_socket_on(False)
    else:
        if actual_temp <= (target_temp - TEMP_DIFF):
            # Turn on
            state.set_socket_on(True)

def controller_thread():
    while True:
        display.run()
        user_input.run()
        temp_sensor.run()
        update_socket()
        state.set_uptime(uptime())

controller_thread()
