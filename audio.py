import pyaudio
import wave
import sys
from datetime import datetime
import os
import logging
arr = os.listdir('.')
logging.basicConfig(filename='audio_record.log', filemode='a', level=logging.DEBUG, 
                    format='%(asctime)s %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

class AudioFile:

    def __init__(self, file):
        """ Init audio stream """ 
        self.file = file
        self.RECORD_SECONDS=3
        self.CHUNK = 2
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100

    def play(self,file=None):
        """ Play entire file """
        if file is not None:
            filename = file
        else:
            filename = self.file
        self.wf = wave.open(filename, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )
        logging.info(f'Playing audio {filename}')
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.wf.readframes(self.CHUNK)
            self.stream.write(data)
        self.close()


    def record(self,sec=3):
        self.RECORD_SECONDS=sec
        self.wf = wave.open(self.file, 'wb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK)
        frames = []
        logging.info(f'Recording audio {self.file}')
        print('start recording')
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK, exception_on_overflow = False)
            frames.append(data)
        self.stream.stop_stream()
        self.wf.setnchannels(self.CHANNELS)
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        self.wf.setframerate(self.RATE)
        self.wf.writeframes(b''.join(frames))
        self.wf.close()
        self.close()

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

    def play_last_nine(self):
        nine_list = []
        for item in arr:
            if '.wav' in item:
                nine_list.append(item)
        nine_list.sort(reverse=True)
        print(nine_list[1:10])
        for i in nine_list[10:]:
            os.remove(os.path.join('.',i))
            logging.info(f'Removing file {i}')
        for i in nine_list[1:10]:
            self.play(os.path.join('.',i))
        





