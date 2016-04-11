from subprocess import call
import time

# File for making radio frequency calls, requires having rfoutlet code setup.

# Turn off an outlet
def on(num):
	rfCode = ""
	if num == 1:
		rfCode = "1381683"
	elif num == 2:
		rfCode = "1381827"
	elif num == 3:
		rfCode = "1382147"
	elif num == 4:
		rfCode = "1383683"
	elif num == 5:
		rfCode = "1389827"

	call(["../rfoutlet/codesend", rfCode])


# Turn on an outlet
def off(num):
	rfCode = ""
	if num == 1:
		rfCode = "1381692"
	elif num == 2:
		rfCode = "1381836"
	elif num == 3:
		rfCode = "1382156"
	elif num == 4:
		rfCode = "1383692"
	elif num == 5:
		rfCode = "1389836"


	call(["../rfoutlet/codesend", rfCode])

