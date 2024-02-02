"""! @file main.py
@brief Micropython code for LAB1

sample text
"""

import pyb
import utime
import micropython

micropython.alloc_emergency_exception_buf(1000)

global update_led

def main():
    global update_led

    update_led = 0

    pwm_timer = 2
    pwm_channel = 1
    irq_timer = 1
    sweep_time = 5000 # ms
    num_steps = 100 # number of steps
    on_percent = 0

    led = led_setup(pyb.Pin.board.PA0, on_percent, pwm_timer, pwm_channel)

    led_brightness(irq_timer, sweep_time, num_steps)

    while 1:
        if update_led:
                led.pulse_width_percent(on_percent)
                
                if on_percent >= 100:
                    on_percent = 0
                else:     
                    on_percent += int(100/num_steps)

                update_led = 0


def led_setup(pin_num:pyb.Pin, pulse_percent:int, tim_num:int, chan_num:int,):
    led_pin = pyb.Pin(pin_num)
    timer = pyb.Timer(tim_num, freq=1000)
    channel = timer.channel(chan_num, pyb.Timer.PWM, pin=led_pin)
    channel.pulse_width_percent(pulse_percent)

    return(channel)


def led_brightness(tim_num:int, sweep_duration:int, num_steps:int):

    timer_frequency = int(1000/(sweep_duration/num_steps))

    led_bright_timer = pyb.Timer(tim_num, freq=timer_frequency)
    led_bright_timer.callback(led_irq)


def led_irq(blank):
    global update_led
    update_led = 1


if __name__ == "__main__":
     main()