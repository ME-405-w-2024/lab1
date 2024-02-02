import pyb
import config

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
    config.update_led = 1