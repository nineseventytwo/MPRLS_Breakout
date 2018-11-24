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

code_list = [0,0]
no_pressure = 14

d = {(0, 3): 'yes.wav', (3, 0): 'no.wav', (2, 1): 'maybe.wav', (1, 2): 'certainly_not.wav'}

# if (len(code_list) <= 3):
#     print(code_list)
def num():
    global ana_val
    ana_val = round(mpr.pressure/ 68.947572932)
    return ana_val

def sort(num):
    if (sum(code_list) <= 2):
        if ana_val > no_pressure: #sip
            code_list[0] += 1
        if ana_val < no_pressure: #puff
            code_list[1] += 1
        if ana_val == no_pressure:
            pass
    else:
        print(code_list)
        code_val = tuple(code_list)
        word = (d.get(code_val))
        if word in d.values():
            print(word)
            wave_file = open(word, "rb")
            wave = audioio.WaveFile(wave_file)
            audio.play(wave)
            time.sleep(0.5)

        else:
            pass
        code_list[0] = 0
        code_list[1] = 0

    time.sleep(0.5)

def main():
    try:
        while True:
            num()
            sort(num())

    except KeyboardInterrupt:
        print('exited program')

main()
