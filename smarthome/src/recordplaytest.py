#!usr/bin/python
# -*- coding: utf-8 -*-
import wave
import os
import sys
from pyaudio import PyAudio,paInt16

chunk=8192#定义数据流块
framerate=48000#采样率
sampwidth=2
channels=1
RECORD_SECONDS=5#录音时间，单位s


'''保存数据到WAV文件'''
def save_wave_file(filename,data):
	wf=wave.open(filename,'wb') 
	wf.setnchannels(channels)#声道数
	wf.setsampwidth(sampwidth)
	wf.setframerate(framerate)#采样频率
	wf.writeframes(b"".join(data))
	wf.close()


def my_record():
	os.close(sys.stderr.fileno())#隐藏错误消息，因为会有一堆ALSA和JACK错误消息，但其实能正常录音
	pa=PyAudio()
	stream=pa.open(format = paInt16,channels=1,rate=framerate,input=True,frames_per_buffer=chunk)#paInt16表示我们使用量化位数16位来进行录音
	print('正在录音……')
	frames=[]
	for i in range(0, int(framerate / chunk * RECORD_SECONDS)):
		data = stream.read(chunk)
		frames.append(data)
	save_wave_file('test.wav',frames)
	stream.close()


def play():
	wf=wave.open(r"test.wav",'rb')
	p=PyAudio()
	stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
	print('正在播放……')
	# 读取数据
	data = wf.readframes(chunk)
	# 播放  
	while data != '':
		stream.write(data)
		data = wf.readframes(chunk)
	#停止数据流  
	stream.stop_stream()
	stream.close()
	#关闭 PyAudio  
	p.terminate()

if __name__ == '__main__':
	my_record()
	print('录音完成')
	play()