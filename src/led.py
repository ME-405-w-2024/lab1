"""! @file led.py
This is a collection of simple test functions to validate PWM usage routines
"""

import pyb



def led_setup(led_pin_num: pyb.Pin.board, timer_num: int, timer_channel_num: int, timer_frequency: int):
    """! Setup pwm for a particular pin 
            @param led_pin_num Pyboard pin to use PWM on
            @param timer_num Timer number associated with the defined PWM pin
            @param timer_channel_num Timer channel number associated with the defined PWM pin
            @param timer_frequency Frequency to initialize the PWM for this pin
            @return Timer channel object
    """
    
    led_pin = pyb.Pin(led_pin_num, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (timer_num , freq=timer_frequency)
    return tim2.channel(timer_channel_num, pyb.Timer.PWM, pin=led_pin)

    

def led_brightness(timer_channel, brightness: int) -> None:
    """!Setup pwm for a particular pin 
            @param timer_channel PWM timer to adjust
            @param brightness New brightness value in 0-100 duty cycle
    """
    timer_channel.pulse_width_percent(brightness)
    
