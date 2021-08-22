from lib.rotary_irq_rp2 import RotaryIRQ
import time

TEMP_MIN, TEMP_MAX = 10, 85
ENCODER_A_PIN, ENCODER_B_PIN = 12, 13

class UserInput():

    def __init__(self, state):
        # Vars
        self.state = state
        self.rotary = RotaryIRQ(pin_num_clk= ENCODER_A_PIN,
                                pin_num_dt= ENCODER_B_PIN,
                                min_val=TEMP_MIN,
                                max_val=TEMP_MAX,
                                reverse=False,
                                pull_up=True,
                                range_mode=RotaryIRQ.RANGE_BOUNDED)
        self.prev_val = state.get_target_temp()
        self.rotary.set(value=self.prev_val)

    def run(self):
        # Update target temp
        value = self.rotary.value()
        if value == self.prev_val:
            return
        self.state.set_target_temp(value)
        self.prev_val = value


