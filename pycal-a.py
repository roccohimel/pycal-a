# Copyright 2025 Thermmo Tec.
# Pycal-A developed by Rocco Himel and Ken Himel
import subprocess
import time
subprocess.run("clear", shell=True)
while True:
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
	def restart():
		subprocess.run("clear", shell=True)
		subprocess.run("python3 pycal-a.py", shell=True)
	def quit():
		subprocess.run("clear", shell=True)
		subprocess.run("bash", shell=True)
	def endpmt():
		print()
		endinp = input("Continue?(y/n) ")
		if endinp == "y":
			subprocess.run("clear", shell=True)
			subprocess.run("python3 pycal-a.py", shell=True)
		if endinp == "n":
			subprocess.run("clear", shell=True)
			subprocess.run("bash", shell=True)
	print("Pycal-A beta version bv0.1 (BR0V1)")
	print()
	print("Please choose an option:")
	print()
	print("0. Basic calculator")
	print("1. Calculate the area of a circle")
	print("   using diameter. (area = PIr^2")
	print("2. Calculate the circumfrance of")
	print("   a circle using diameter.")
	print("   (circ = 2PIr)")
	print("3. Restart Pycal-A")
	print("4. Quit Pycal-A")
	print("5. Developer options")
	print()
	option = input("Number> ")
	if option == "0":
		basic_cal()
		endpmt()
	if option == "1":
		circle_area()
		endpmt()
	if option == "2":
		circle_circ()
		endpmt()
	if option == "3":
		restart()
		endpmt()
	if option == "4":
		quit()
		endpmt()
	if option == "5":
		print()
		print("Developer options: ")
		print()
		print("0. << Back")
		print("1. Test endpmt()")
		print("2. Edit source code")
		print()
		devoption = input("Number> ")
		if devoption == "0":
			subprocess.run("clear", shell=True)
			subprocess.run("python3 pycal-a.py", shell=True)
		if devoption == "1":
			print("Testing endpmt()")
			time.sleep(0.1)
			endpmt()
		if devoption == "2":
			subprocess.run("clear", shell=True)
			subprocess.run("nano pycal-a.py", shell=True)
	else:
		print("invalid input: " + option)
