"""! @file main.py
@brief Micropython code for LAB1

sample text
"""

import pyb
import micropython
import led
import config

micropython.alloc_emergency_exception_buf(1000)


def main():


    pwm_timer = 2
    pwm_channel = 1
    irq_timer = 1
    sweep_time = 5000 # ms
    num_steps = 100 # number of steps
    on_percent = 0

    led_pwm = led.led_setup(pyb.Pin.board.PA0, on_percent, pwm_timer, pwm_channel)

    led.led_brightness(irq_timer, sweep_time, num_steps)

    while 1:
        if config.update_led:
                led_pwm.pulse_width_percent(on_percent)
                
                if on_percent >= 100:
                    on_percent = 0
                else:     
                    on_percent += int(100/num_steps)

                config.update_led = 0

if __name__ == "__main__":
    config.init()
    main()