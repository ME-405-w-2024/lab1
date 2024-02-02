import pyb
import time
import led

sleep_time_ms = 10
bright_loop_time_ms = 5000

LED_max_brightness = 100

if __name__ == "__main__":
    led_timer = led.led_setup(pyb.Pin.board.PA0, timer_num=2, timer_channel_num=1, timer_frequency=1000)
    
    num_steps = bright_loop_time_ms/sleep_time_ms

    current_step = 0

    while 1:
        
        if current_step < num_steps:
            
            current_brightness = LED_max_brightness * (current_step/num_steps)

            led.led_brightness(led_timer, int(current_brightness))

            current_step += 1

            time.sleep(sleep_time_ms/1000)
        else:
            current_step = 0