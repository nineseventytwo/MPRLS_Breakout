import time
import audioio
import board
import digitalio
import busio
import adafruit_mprls

i2c = busio.I2C(board.SCL, board.SDA)

# Simplest use, connect to default over I2C
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)

wave_file = open("under_pressure.wav", "rb")
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)


while True:
    val = round(mpr.pressure/ 68.947572932)
    if val < 12:
        print(val)
        audio.play(wave)
        time.sleep(0.5)

    else:
        print(val)
