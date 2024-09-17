#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    print(frequency)
    utime.sleep(duration/1000)


def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

#for i in range(64):
    #print(freq)
    #playtone(freq, duration)
    #freq = int(freq * 1.1)

# Turn off the PWM
#quiet()




playtone(480,200)

playtone(1568,200)

playtone(1568,200)

playtone(1568,200)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(784,200)

playtone(370,200)

playtone(392,200)

playtone(370,200)

playtone(392,200)

playtone(392,400)

playtone(196,400)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(84,200)

playtone(880,200)

playtone(831,200)

playtone(880,200)

playtone(988,400)

playtone(880,200)

playtone(784,200)

playtone(699,200)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(784,200)

playtone(880,200)

playtone(830,200)

playtone(880,200)

playtone(988,400)

utime.sleep(400/1000)

playtone(1108,10)
playtone(1174,200)
playtone(1480,10)
playtone(1568,200)

utime.sleep(200/1000)
playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(784,200)

playtone(784,200)

playtone(740,200)

playtone(784,200)

playtone(880,200)

playtone(830,200)

playtone(880,200)

playtone(988,400)

playtone(880,200)

playtone(784,200)

playtone(699,200)

playtone(659,200)

playtone(699,200)

playtone(784,200)

playtone(880,400)

playtone(784,200)

playtone(699,200)

playtone(659,200)

playtone(587,200)

playtone(659,200)

playtone(699,200)

playtone(784,400)

playtone(699,200)

playtone(659,200)

playtone(587,200)

playtone(523,200)

playtone(587,200)

playtone(659,200)

playtone(699,400)

playtone(659,200)

playtone(587,200)

playtone(494,200)

playtone(523,200)

utime.sleep(400/1000)

playtone(349,400)

playtone(392,200)

playtone(330,200)

playtone(523,200)

playtone(494,200)

playtone(466,200)

playtone(440,200)

playtone(494,200)

playtone(523,200)

playtone(880,200)

playtone(494,200)

playtone(880,200)

playtone(1760,200)

playtone(440,200)

playtone(392,200)

playtone(440,200)

playtone(494,200)

playtone(784,200)

playtone(440, 200)

playtone(784,200)

playtone(1568,200)

playtone(392,200)

playtone(349,200)

playtone(392,200)

playtone(440,200)

playtone(699,200)

playtone(415,200)

playtone(699,200)

playtone(1397,200)

playtone(349,200)

playtone(330,200)

playtone(311,200)

playtone(330,200)

playtone(659,200)

playtone(699,400)

playtone(784,400)

playtone(440,200)

playtone(494,200)

playtone(523,200)

playtone(880,200)

playtone(494,200)

playtone(880,200)

playtone(1760,200)

playtone(440,200)

playtone(392,200)

playtone(440,200)

playtone(494,200)

playtone(784,200)

playtone(440,200)

playtone(784,200)

playtone(1568,200)

playtone(392,200)

playtone(349,200)

playtone(392,200)

playtone(440,200)

playtone(699,200)

playtone(659,200)

playtone(699,200)

playtone(740,200)

playtone(784,200)

playtone(392,200)

playtone(392,200)

playtone(392,200)

playtone(392,200)

playtone(196,200)

playtone(196,200)

playtone(196,200)

playtone(185,200)

playtone(196,200)

playtone(185,200)

playtone(196,200)

playtone(208,200)

playtone(220,200)

playtone(233,200)

playtone(247,200)


quiet()