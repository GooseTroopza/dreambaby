import time
from gpiozero import LED, Button

other = 0
phase = 0
timer = 0
phase_time = 0
timer_start = 0
timer_end = 0
sound_input = bool(True)
run = bool(False)
start = False
led = LED(4)
button = Button(14)
silance_wait = 2
silance_start = 0
silance_run = 0

def phases():
    global phase
    global phase_time
    if phase == 5:
        phase == 0
    if phase == 0:
        phase_time = 6
    if phase == 1:
        phase_time = 12
    if phase == 2:
        phase_time = 18
    if phase == 3:
        phase_time = 24
    if phase == 4:
        phase_time = 30

def stop():
    global run
    global sound_input
    global silance_wait
    global silance_start
    global silance_run
    if button.is_pressed:
        run = True
        silance_run = 0
    if not button.is_pressed:
        silance_start = time.perf_counter()
        while silance_wait > silance_run:
            silance_run = time.perf_counter() - silance_start
            if button.is_pressed:
                break
        run = False


while True:
    stop()
    while run:
        phases()
        timer_start = time.perf_counter()
        while (phase_time) > timer:
            timer = time.perf_counter() - timer_start
            stop()
            if not run:
                break
        if run:
            phase += 1
            #print(time.perf_counter())
            print("Phase " + str(phase) + " ended")
            time.sleep(1)
            led.on()
            time.sleep(5)
            led.off()
    time.sleep
