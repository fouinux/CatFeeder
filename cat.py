#!/usr/bin/env python3

import sys
import time
import gpiozero

# Do a barrel roll
def PerformStep(Delay, Step):
    global StepPin
    for n in range(int(Step)):
        StepPin.on()
        time.sleep(Delay)
        StepPin.off()
        time.sleep(Delay)

# I/O Definition
EnablePin = gpiozero.LED(16)
StepPin = gpiozero.LED(12)
DirPin = gpiozero.LED(1)

# General stuff
Speed = 0.00001

Microstep = 32 # Full steps are devided by 32
StepPerTurn = 200 # Nema17

TurnOrder = 1.0 # Default 1 turn
ReverseOrder = 0.1

# Get number of turn for args
if len(sys.argv) > 1:
    TurnOrder = float(sys.argv[1])

# Perform 0.1 turn in reverse
StepOrder = ReverseOrder * StepPerTurn * Microstep
DirPin.off()
PerformStep(Speed, StepOrder)

# Compute the number of steps
StepOrder = (TurnOrder + ReverseOrder) * StepPerTurn * Microstep
DirPin.on()
PerformStep(Speed, StepOrder)
