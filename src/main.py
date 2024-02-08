import pyb
import time
from motor_driver import MotorDriver as Motor

sleep_time_ms = 10
bright_loop_time_ms = 5000

LED_max_brightness = 100

if __name__ == "__main__":

    en_pin = pyb.Pin.board.PC1
    in1b_pin = pyb.Pin.board.PA1
    in1a_pin = pyb.Pin.board.PA0

    motor = Motor(en_pin, 
                  in1a_pin, 2, 1,
                  in1b_pin, 2, 2,
                  30000)


    motor.set_enable(1)


    try:

        while 1:
        
            motor.set_duty_cycle(10)
            time.sleep(1)
            motor.set_duty_cycle(100)
            time.sleep(1)
            motor.set_duty_cycle(0)
            time.sleep(1)
            motor.set_duty_cycle(-10)
            time.sleep(1)
            motor.set_duty_cycle(-100)
            time.sleep(1)

    except KeyboardInterrupt:
        motor.set_duty_cycle(0)
        motor.set_enable(0)
        print("Program Ended")
