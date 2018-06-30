# encoding:utf-8
from flask import Flask,request
import json
from threading import Thread
import socket
import threading
import time
import sys
import sqlite3

app=Flask(__name__)
####回复文本格式##########
re={}
result={}
result["type"]="text"
result["content"]=""
re["error_code"]=0
re["error_msg"]=""
re["result"]=result
dic={'温度':'temperature','湿度':'humidity','光照':'light','二氧化碳':'co2_simulation','声音':'noise'}
class Response:
	def __init__(self,intent,nom_word):
		self.re=re
		self.intent=intent
		self.nom_word=nom_word
	def json_resp(self,intent,nom_word):
		if intent=="OPEN_AIRCONDITIONER":
			re["result"]["content"]="请稍等，正在为您打开空调"
		elif intent=="CLOSE_AIRCONDITIONER":
			re["result"]["content"]="请稍等，正在为您关闭空调"
		elif intent=="CHANGE_TEMP_UP":
			re["result"]["content"]="正在帮您升高空调温度，请稍等"
		elif intent=="CHANGE_TEMP_DOWN":
			re["result"]["content"]="正在帮您降低空调温度，请稍等"
		elif intent=="CHANGE_TEMP_TO":
			re["result"]["content"]="好的，正在为您将空调设置为该温度，请稍等"
		elif intent=="W_SPEED_UP":
			re["result"]["content"]="正在帮您提高空调风速，请稍等"
		elif intent=="W_SPEED_DOWN":
			re["result"]["content"]="正在帮您降低空调风速，请稍等"
		elif intent=="CHANGE_W_SPEED":
			re["result"]["content"]="好的，正在为您调节风速，请稍等"
		elif intent=="OPEN_SLEEP":
			re["result"]["content"]="好的，正在为您打开睡眠模式，请稍等"
		elif intent=="CLOSE_SLEEP":
			re["result"]["content"]="好的，正在为您关闭睡眠模式，请稍等"
		elif intent=="TIMER_SET":
			re["result"]["content"]="好的，正在为您设置定时关闭，请稍等"
		elif intent=="TIMER_CLOSE":
			re["result"]["content"]="好的，正在为您取消空调定时，请稍等"
		elif intent=="CHANGE_COM_MOD":
			re["result"]["content"]="好的，正在为您调节到该模式"
		elif intent=="CHANGE_SMART_MOD":
			re["result"]["content"]="好的，正在为您关闭睡眠模式，请稍等"
		elif intent=="ENV_INFO_QUERY":
			#socket_client(nom_word)
			conn = sqlite3.connect("sensor.db")
			c = conn.cursor()
			c.execute('SELECT '+dic[nom_word]+' FROM data ORDER BY time desc')
			query_result=c.fetchone()[0]					#取出查询项对应数据
			re["result"]["content"]="您当前的室内"+nom_word+"为"+query_result
		else:
			re["result"]["content"]="请求失败，请重试"
		return re
		
@app.route("/unit/callback",methods=['POST'])
def callback():
	print(request.headers)
	print(request.data)
	dic=json.loads(str(request.data,encoding='utf-8'))
	intent=dic["response"]["schema"]["intent"]
	nom_word=dic["response"]["schema"]["slots"][0]["normalized_word"]
	exp1=Response(intent,nom_word)
	
	if os.path.exists("control.db"):
		conn = sqlite3.connect("control.db")
		c = conn.cursor()
	else:
		conn = sqlite3.connect("control.db")
		c = conn.cursor()
		c.execute('''CREATE TABLE commands(intent text not null primary key,nom_word)''')#第一次执行时用来创建表，第二次执行需要删掉
	c.execute('INSERT INTO commands VALUES(?,?)',(intent,nom_word))					#插入意图和归一化词槽
	conn.commit()
	conn.close()
	json_re=exp1.resp()
	json_re=json.dumps(re)
	print(json_re)
	return json_re
	
	
	
if __name__=='__main__':
	app.run(host='192.168.137.9',port=9999,debug=True)
	
