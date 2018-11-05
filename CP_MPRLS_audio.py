import time
import audioio
import board
import digitalio
import busio
import adafruit_mprls

i2c = busio.I2C(board.SCL, board.SDA)

# Simplest use, connect to default over I2C
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)

wave_file = open("slouch.wav", "rb")
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)

val = round(mpr.pressure/ 68.947572932)


while True:
    print(val)
    time.sleep(1)
    if val < 10:
        audio.play(wave)

        # This allows you to do other things while the audio plays!
        t = time.monotonic()
        while time.monotonic() - t < 6:
            pass
    else:
        print("Waiting ...")