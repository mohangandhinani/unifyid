import struct
import wave

from rand_generator import ran_list_generator


def sound_gen():
    l = ran_list_generator(3 * 44100)  # 3sec * samples per second
    obj = wave.Wave_write("soundgen.wav")
    obj.setparams((1, 2, 44100, len(l), 'NONE', 'not compressed'))

    for s in l:
        obj.writeframes(struct.pack('h', s))
    obj.close()


if __name__ == "__main__":
    sound_gen()
