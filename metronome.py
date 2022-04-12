import time
import simpleaudio


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
        wait(delay)
        count += 1

        if count > mode:
            count = 1
            beat += 1

        wave_obj = simpleaudio.WaveObject.from_wave_file('metronome.wav')
        if count == 1:
            wave_obj = simpleaudio.WaveObject.from_wave_file('metronomeup.wav')

        play_obj = wave_obj.play()
        play_obj


while True:
    beats = input("Input bpm: ")
    try:
        beats = int(beats)
        metronome(beats)
    except ValueError:
        print("Invalid input, please input a valid bpm.")
    except ZeroDivisionError:
        print("Invalid input, please input a valid bpm.")
    continue
