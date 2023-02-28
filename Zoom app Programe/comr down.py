from threading import *
import datetime
import time
import winsound
def alarm():
	# Infintite Loop
	while True:
		# Set Alarm
		set_alarm_time = "16:22:00"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:

			print("Time to Wake up")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
			time.sleep(1)
			break
def Threading():
	t1=Thread(target=alarm)
	t1.start()
Threading()