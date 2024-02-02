import pyb


class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """




    def __init__ (self, 
                  en_pin: pyb.Pin.board, 
                  in1pin: pyb.Pin.board, in1_timer_num: int, in1_timer_channel_number: int, 
                  in2pin: pyb.Pin.board, in2_timer_num: int, in2_timer_channel_number: int, 
                  pwm_frequency: int):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        print ("Creating a motor driver")

        self.en_pin = pyb.Pin(en_pin, pyb.Pin.OUT_PP)

        self.pin1_timer_channel = self.__setupmotor__(in1pin, in1_timer_num, in1_timer_channel_number, pwm_frequency)
        self.pin2_timer_channel = self.__setupmotor__(in2pin, in2_timer_num, in2_timer_channel_number, pwm_frequency)

        
    def __setupmotor__(self, inpin: pyb.Pin.board, in_timer_num: int, in_timer_channel_number: int, pwm_frequency: int):

        pwm_pin = pyb.Pin(inpin, pyb.Pin.OUT_PP)
        pwm_timer = pyb.Timer (in_timer_num , freq=pwm_frequency)
        timer_channel = pwm_timer.channel(in_timer_channel_number, pyb.Timer.PWM, pin=pwm_pin)
        return timer_channel


    def set_enable(self, value: int):
        self.en_pin.value(value)


    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")


        if(level < 0):
            self.pin1_timer_channel.pulse_width_percent(level * -1)
            self.pin2_timer_channel.pulse_width_percent(0)
        else:
            self.pin1_timer_channel.pulse_width_percent(0)
            self.pin2_timer_channel.pulse_width_percent(level)

    