import pyb

class Motor:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    

    def __init__ (self, pwm_pin_num: pyb.Pin.board, timer_num: int, timer_channel_num: int, timer_frequency: int):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """

        self.pwm_pin = pyb.Pin(pwm_pin_num, pyb.Pin.OUT_PP)
        self.pwm_timer = pyb.Timer (timer_num , freq=timer_frequency)
        self.timer_channel = self.pwm_timer.channel(timer_channel_num, pyb.Timer.PWM, pin=self.pwm_pin)

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        self.timer_channel.pulse_width_percent(level)

    