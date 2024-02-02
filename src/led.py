"""! @file led.py
Doxygen style docstring for the file (change this!)"""

import pyb



def led_setup(led_pin_num: pyb.Pin.board, timer_num: int, timer_channel_num: int, timer_frequency: int):
    """! Doxygen style docstring for this function 
        Retirns timer channel object
    """
    
    led_pin = pyb.Pin(led_pin_num, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (timer_num , freq=timer_frequency)
    return tim2.channel(timer_channel_num, pyb.Timer.PWM, pin=led_pin)

def led_brightness(timer_channel, brightness: int) -> None:
    """! Doxygen style docstring for this function 

    """
    timer_channel.pulse_width_percent(brightness)
    
