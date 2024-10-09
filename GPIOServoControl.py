from gpiozero import Servo
from time import sleep

servo = Servo(17)

# defining the PWM function dimensions for the servo
# min_pulse_width = 1ms
# max_pulse_width = 2ms
# frame_width = 20ms
# pulse_width = 1.5ms
# active_high = True
# initial_duty_cycle = 0
# pin_factory = None
# pin = 17
# frequency = 50
# initiial_value = 0
# min_value = 0
# max_value = 1


def __PWM__(self, pin=17, frequency=50, initiial_value=0, min_value=0, max_value=1, 
            min_pulse_width=1/1000, max_pulse_width=2/1000, frame_width=20/1000,
            pulse_width=1.5/1000, active_high=True, initial_duty_cycle=0, pin_factory=None):
    if min_pulse_width >= max_pulse_width:
        raise ValueError('min_pulse_width must be less than max_pulse_width', , servo.close(), exit(1))
    if max_pulse_width > frame_width:
        raise ValueError('max_pulse_width must be less than frame_width', servo.close(), exit(1))
    
    self._frame.width = frame_width
    self._min_pulse_width = min_pulse_width
    self._max_pulse_width = max_pulse_width
    self._min_duty_cycle = min_pulse_width / frame_width
    self._max_duty_cycle = max_pulse_width / frame_width
    self._duty_cycle_range = (max_pulse_width - min_pulse_width) / frame_width
    self._min_value = -1
        self._value_range = 2
        super().__init__(
            pwm_device=PWMOutputDevice(
                pin, frequency=int(1 / frame_width), pin_factory=pin_factory),                        #gotta find out the pin.factory settings
            pin_factory=pin_factory
        )

while True:
    # Set the servo to its minimum position
    servo.min()
    sleep(1)
    # Set the servo to its central position
    servo.mid()
    sleep(1)
    # Set the servo to its maximum position
    servo.max()
    sleep(1)

    # Close the servo
servo.close()
exit(0)
