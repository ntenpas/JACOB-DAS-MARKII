#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import pyaudio

import time
import json
import os

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

CLIENT_ACCESS_TOKEN = '03848b1f5f2f48ef8a8fdc062674afa2'
SUBSCRIBTION_KEY = '3cd524f0-efff-4ebb-9653-b9eb7bbda1cb' 

def main():
    resampler = apiai.Resampler(source_samplerate=RATE)

    vad = apiai.VAD()

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIBTION_KEY)

    request = ai.voice_request()

    def callback(in_data, frame_count, time_info, status):
        frames, data = resampler.resample(in_data, frame_count)
        state = vad.processFrame(frames)
        request.send(data)

        if (state == 1):
            return in_data, pyaudio.paContinue
        else:
            return in_data, pyaudio.paComplete

    
    #PLACEHOLDERS FOR SPOTIFY FUNCTIONS
    def get_song(spotify_key, song_name):
        pass

    def get_playlist(spotify_key, user_ID, playlist_ID):
        pass

    def say(response):
        os.system(("echo %s |espeak" % response))

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True,
                    output=False,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)
    exit is False

    print ("-----------------------------------------------------------------")
    print ("J.A.C.O.B - Digital Assistant Series - Mark II")
    print ()
    print ("Added features from MK I - Speech to Text, Spotify integration")
    print ("-----------------------------------------------------------------")
    while exit is False:
        begin_speech = input("Press enter to speak. ")

        need_for_speech = False
        stream.start_stream()

        print ("---------------------------!Speak!----------------------------")

        try:
            while stream.is_active():
                time.sleep(0.1)
        except Exception:
            raise e
        except KeyboardInterrupt:
            pass

        stream.stop_stream()
        stream.close()
        p.terminate()

        print ("Wait for response...")
        response = request.getresponse()

        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        print(json_obj["result"]["resolvedQuery"])
        print(json_obj["result"]["fulfillment"]["speech"])
        jacob_response = json_obj["result"]["fulfillment"]["speech"]
        ###ADD SEARCH VARIABLE SO JACOB KNOWS WHEN TO SPEAK OR NAH

        ##UNTIL THEN:
        need_for_speech is True

        if need_for_speech is True: 
           say(jacob_response)
        #print (response.read())

if __name__ == '__main__':
    main()

"""
EXTRA:

    def what_do(a, b, p1, p2):
        x = (a/(a+b))*(m/p1)
        y = (b/(a+b))*(m/p2)

    def set_reminder(name, time):
        now = datetime.datetime.now()
        
        pass

"""