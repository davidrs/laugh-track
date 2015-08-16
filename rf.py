from subprocess import call

# File for making radio frequency calls, requires having rfoutlet code setup.

# Turn off an outlet
def on(num):
	rfCode = ""
	if num == 5:
		rfCode = "1389827"

	call(["../rfoutlet/codesend", rfCode])


# Turn on an outlet
def off(num):
	rfCode = ""
	if num == 5:
		rfCode = "1389836"

	call(["../rfoutlet/codesend", rfCode])

