# import random
# from subprocess import call

import time
import audioio
import board
import digitalio
import busio
import adafruit_mprls

i2c = busio.I2C(board.SCL, board.SDA)

# Simplest use, connect to default over I2C
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)

audio = audioio.AudioOut(board.A0)

timeout = time.time() + 3 # 3 seconds from now
sip_list = []
puf_list = []
d = {(0, 3): 'yes.wav', (3, 0): 'no.wav', (2, 1): 'maybe.wav', (1, 2): 'certainly_not.wav'}

while True:
    test = 0
    # ana_val = random.randint(1,30)
    ana_val = round(mpr.pressure/ 68.947572932)
    time.sleep(1)
    print (ana_val)
    if ana_val > 15:
        sip_list.append(ana_val)
    if ana_val < 15:
        puf_list.append(ana_val)
    if ana_val == 15:
        pass
    if test == 3 or time.time() > timeout:
        break
    test = test - 1
# print(sip_list)
# print(puf_list)
print (len(sip_list), len(puf_list))
sp =  (len(sip_list), len(puf_list))
word = str(d.get(sp))
#this one line evals sp(which is the length of the sip/puf lists) it finds the key in the d dict, then it returns the value, which then is put into the say command
# call(["say", (d.get(sp))])
if word != (0, 0):
    wave_file = open(("yes.wav"), "rb")
    wave = audioio.WaveFile(wave_file)
    audio.play(wave)
    return
