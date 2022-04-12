import time
import simpleaudio
import keyboard


def wait(delay):
    end_time = time.time() + delay
    while end_time > time.time():
        continue


def metronome(bpm):
    print(float(bpm), "BPM")
    delay = 60 / bpm
    count = 0
    beat = 0
    mode = 4

    while True:
        if keyboard.is_pressed('q'):
            break
        wait(delay)
        count += 1
        if count > mode:
            count = 1
            beat += 1
        wave_obj = simpleaudio.WaveObject.from_wave_file('metronome.wav')
        if count == 1:
            wave_obj = simpleaudio.WaveObject.from_wave_file('metronomeup.wav')
        wave_obj.play()


while True:
    beats = input("Input bpm or 'q' to stop: ")
    try:
        beats = int(beats)
        metronome(beats)
    except ValueError:
        print("Invalid input, please input a valid bpm!")
    except ZeroDivisionError:
        print("Invalid input, please input a valid bpm!")
