# Copyright (C) 2025 Thermmo Tec.
# Pycal-A developed by Rocco Himel and Ken Himel
# Pycal-A beta version 0.2 (BR0V2)
import subprocess
import time
import os
subprocess.run("clear", shell=True)
while True:
	def open():
		subprocess.run("python3 pycal-a.py", shell=True)
	def clear():
		subprocess.run("clear", shell=True)
	def update_linuxmac():
		clear()
		subprocess.run("sudo rm pycal-a.py", shell=True)
		subprocess.run("wget https://raw.githubusercontent.com/roccohimel/pycal-a/refs/heads/main/pycal-a.py", shell=True)
	def update_windows():
		os.system('del /f "pycal-a.py"')
		os.system("wget https://raw.githubusercontent.com/roccohimel/pycal-a/refs/heads/main/pycal-a.py")
	def basic_cal():
		eq = input("Calculate> ")
		print(eval(eq))
	def circle_area():
		dmtr0 = int(input("Diameter> "))
		rds0 = dmtr0 / 2
		rds0E2 = rds0 * rds0
		area0 = rds0E2 * 3.14
		print(area0)
	def circle_circ():
		dmtr1 = int(input("Diameter> "))
		rds1 = dmtr1 / 2
		xPI1 = 2 * 3.14
		circ1 = xPI1 * rds1
		print(circ1)
	def stopwatch():
		seconds = 0
		while True:
			clear()
			print("Press CTRL + C to quit")
			print()
			seconds += 1
			print(seconds, "seconds")
			time.sleep(1)
	def timer():
		clear()
		timer_seconds = int(input("Set timer seconds> "))
		timer_seconds += 1
		clear()
		while timer_seconds > 0:
			timer_seconds -= 1
			print(timer_seconds, "seconds left")
			time.sleep(1)
			clear()
		print()
		print("Timer done!")
		time.sleep(1)
		endpmt()
	def dateandtime():
		clear()
		print("Options:")
		print()
		print("0. << Back")
		print()
		print("1. GNU Bash (Or any UNIX/Linux Shell)")
		print("2. Windows Command Prompt")
		print("3. Windows PowerShell")
		print()
		datepmt = input("Number>> ")
		if datepmt == "1":
			clear()
			subprocess.run("date", shell=True)
			endpmt()
		if datepmt == "2":
			clear()
			os.system("echo %date% %time%")
			endpmt()
		if datepmt == "3":
			clear()
			os.system("Get-Date")
			endpmt()
	def restart():
		clear()
		open()
	def quit():
		clear()
		subprocess.run("bash", shell=True)
	def update():
		clear()
		print("Update options:")
		print()
		print("1. Update for Linux and Mac")
		print("2. Update for Windows")
		print()
		upop = input("Number> ")
		if upop == "1":
			update_linuxmac()
		if upop == "2":
			update_windows()
	def endpmt():
		print()
		endinp = input("Continue?(y/n) ")
		if endinp == "y":
			restart()
		if endinp == "n":
			quit()
	def startpmt():
		clear()
		print("Pycal-A beta version bv0.2 (BR0V2)")
		print()
		print("Please choose an option:")
		print()
		print("1. Basic calculator")
		print("2. Calculate the area of a circle")
		print("   using diameter. (area = PIr^2")
		print("3. Calculate the circumfrance of")
		print("   a circle using diameter.")
		print("   (circ = 2PIr)")
		print("4. Clock")
		print("r. Restart Pycal-A")
		print("q. Quit Pycal-A")
		print("d. Developer options")
		print("u. Update Pycal-A")
		print()
		option = input("Number> ")
		if option == "1":
			clear()
			basic_cal()
			endpmt()
		if option == "2":
			clear()
			circle_area()
			endpmt()
		if option == "3":
			clear()
			circle_circ()
			endpmt()
		if option == "4":
			clear()
			print()
			print("Options:")
			print()
			print("0. << Back")
			print("1. View date and time")
			print("2. Stopwatch")
			print("3. Timer")
			print()
			coption = input("Number> ")
			if coption == "0":
				startpmt()
			if coption == "1":
				dateandtime()
			if coption == "2":
				stopwatch()
			if coption == "3":
				timer()
			else:
				print("Invalid input")
		if option == "r":
			clear()
			restart()
			endpmt()
		if option == "q":
			quit()
			endpmt()
		if option == "d":
			clear()
			print()
			print("Developer options: ")
			print()
			print("0. << Back")
			print("1. Test endpmt()")
			print("2. Edit source code (DO NOT PUBLISH: SEE GNU LICENCE IN GITHUB REPO)")
			print()
			devoption = input("Number> ")
			if devoption == "0":
				clear()
				startpmt()
			if devoption == "1":
				clear()
				print("Testing endpmt()")
				time.sleep(0.1)
				endpmt()
			if devoption == "2":
				clear()
				subprocess.run("nano pycal-a.py", shell=True)
		if option == "u":
			update()
			endpmt()
		else:
			print("invalid input: " + option)
			clear()
			startpmt()
	startpmt()
