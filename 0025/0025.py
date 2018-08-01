# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:50:38 2018

@author: zhang
based on python 2.7
"""

from Tkinter import *
import pyaudio
import wave
import requests
import json
import pycurl
from io import BytesIO
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 5

def record_wave():
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)
    print("Recording...")
    frames = []
    
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Recording end...")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes('b'.join(frames))
    wf.close()
    
def button():
    root = Tk()
    
    label = Label(root)
    label['text'] = 'Start recording'
    label.pack()
    
    btn1 = Button(root)
    btn1['text'] = 'Start'
    btn1['command'] = record_wave
    btn1['fg'] = 'red'
    btn1.pack()
    
    root.mainloop()
    
def get_token():
    api_id = '9550153'
    api_key = 't2ePzNA79W4dOEVkhmDCB7al'
    secret_key = '248a85ff8c633684760a0b53bfebe2ef'
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='\
          + api_key + '&client_secret=' + secret_key + '&'
    data = requests.post(url)
    token = json.loads(data.content).get('access_token')
    return token

def post_voice(token):
    fp = wave.open('output.wav', 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)
    cuid = "778617402"
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
            'Content-Type: audio/pcm; rate=8000',
            'Content-Length: %d' % f_len
            ]
    
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url))
    c.setopt(c.HTTPHEADER, http_header)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    
    c.setopt(c.WRITEDATA, buffer)
    
    c.perform()
    c.close()
    response = buffer.getvalue().decode('utf-8')
    print(response)
    data = json.loads(response)
    result = data.get('result')[0]
    return result

def run():
    record_wave()
    token = get_token()
    result = post_voice(token)
    return result

if __name__ == '__main__':
    result = run()
    print(result)
    if u"浏览器" in result:
        print("success")
        os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    
    
    