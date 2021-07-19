import time

phase = 0
timer = 0
phase_time = 0
timer_start = 0
timer_end = 0
sound_input = bool(True)
run = bool(True)
start = False
LED = False
silance_wait = 10
silance_start = 0
silance_run = 0

def phases():
    global phase
    global phase_time
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
    if sound_input:
        run = True
        silance_run = 0
    if not sound_input:
        silance_start = time.perf_counter()
        while silance_wait > silance_run:
            silance_run = time.perf_counter() - silance_start
            if sound_input:
                break
        run = False



while True:
    while run:
        phases()
        timer_start = time.perf_counter()
        while (phase_time) > timer:
            timer = time.perf_counter() - timer_start
            stop()
            if not run:
                break
        LED = True
        phase += 1
        #print(time.perf_counter())
        print("Phase " + str(phase) + " ended")

