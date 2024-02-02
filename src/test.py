
sweep_duration = 5000

num_steps = 100

timer_frequency = int(1000/(sweep_duration/num_steps))

print(timer_frequency)
print(type(timer_frequency))