import time
import simpleaudio
import keyboard


def wait(delay):
    end_time = time.time() + delay
    while time.time() < end_time:
        if keyboard.is_pressed('space'):
            return True
        continue
    return False


def metronome(bpm):
    delay = 60 / bpm
    count = 0
    beat = 0
    mode = 4

    while True:
        if wait(delay):
            break
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
    if beats == 'q':
        break
    try:
        beats = int(beats)
        metronome(beats)
        print(f"Now playing at {beats} BPM. Press 'space' to stop and input a new BPM.")
    except ValueError:
        print("Invalid input, please input a valid bpm!")
    except ZeroDivisionError:
        print("Invalid input, please input a valid bpm!")
