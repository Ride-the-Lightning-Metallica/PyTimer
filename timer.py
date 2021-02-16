import sys, os
from time import sleep
import _thread as thread
from PyQt5 import QtCore, QtGui, QtWidgets
from timer_gui import *
import pygame
from functools import partial

class MyWin(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.main)
		# set min and max valus for seconds and minutes
		self.ui.spinBox_2.setRange(0, 60)
		self.ui.spinBox_3.setRange(0, 60)
		self.reminders_count = 0
		self.threads = {}

	def main(self):
		'''
		
		Controls time retrieval from input fields, time validation,
		display of validated time in GUI, timer start,
		timer expiration notification with beep
		
		'''
		if self.reminders_count == 6:
			QtWidgets.QMessageBox.about(self, 'Max Reminders', 'You can\'t append more than 6 reminders')
		else:
			self.reminders_count += 1
			self.time = self.get_time()
			self.time = self.validate_time(self.time)
			self.display_time()
			
			reminder_name = self.get_reminder_name()
			if reminder_name:
				thread.start_new_thread(self.timer, (reminder_name,))

	def get_time(self):
		'''

		Get time from all spinBox fields and return a dictionary
		with keys: seconds, minutes, hours

		'''
		time = {}
		units_of_time = ['seconds', 'minutes', 'hours'] # keys for dictionary with time

		for unit_of_time, unit_of_time_index in zip(units_of_time, ['2', '3', '4']):
			unit_of_time_value = self.ui.__getattribute__('spinBox_' + unit_of_time_index)
			time[unit_of_time] = unit_of_time_value.value()

		return time

	def validate_time(self, time):
		'''
			
		Checks minutes and seconds in the "time" dictionary.
		If they are greater than 60 or equal to 60, divides the time
		value modulo and assigns the reminder to the corresponding dictionary key.
		Increases the larger unit of time by 1

		'''
		for unit_of_time, unit_of_time_value in time.items():
			if unit_of_time_value >= 60:
				if unit_of_time == 'seconds':
					time[unit_of_time] = unit_of_time_value % 60
					time['minutes'] += 1
				elif unit_of_time == 'minutes':
					time[unit_of_time] = unit_of_time_value % 60
					time['hours'] += 1

		return time

	def display_time(self):
		'''
		
		Displays validated values of time from dictionary 'time' on 
		graphical user interface
		
		'''
		for unit_of_time, unit_of_time_index in zip(self.time.keys(), ['2', '3', '4']):
			spinBox = self.ui.__getattribute__('spinBox_' + unit_of_time_index)
			spinBox.setValue(self.time[unit_of_time])

	def load_sound(self, name, directory='sounds'):
		'''

		Loads a sound from the path and returns a new pygame.Sound object
		to play a sound to signal a reminder

		'''
		pygame.mixer.init()

		if 'win' in sys.platform:
			sound_extension = '.wav'
		else:
			sound_extension = '.ogg'

		fullname = os.path.join(directory, name)
		fullname += sound_extension

		try:
			sound = pygame.mixer.Sound(fullname)
		except pygame.error as message:
			print('Cannot load sound')
			raise SystemExit(message)
		return sound

	def convert_in_seconds(self):
		'''
		
		Converts the time from the 'time' dictionary into seconds

		'''
		all_time_seconds = 0
		all_time_seconds += self.time['seconds']
		all_time_seconds += self.time['minutes'] * 60
		all_time_seconds += self.time['hours'] * 60 * 60

		return all_time_seconds

	def get_reminder_name(self):
		'''
		
		Calls dialog window for input reminder name, if 'ok' button pressed
		deletes all spaces on the sides from reminder name and if result is not
		empty string, returns reminder name, else returns False

		'''
		my_dialog = MyDialog()
		my_dialog.show()
		my_dialog.setWindowTitle('Reminder name')
		ok = my_dialog.exec_()
		if ok:
			reminder_name = my_dialog.ui.lineEdit.text().strip()
			if reminder_name:
				return my_dialog.ui.lineEdit.text()
		return False

	def converts_from_seconds(self, all_time_seconds):
		'''
	
		Converts time from seconds in seconds, minutes, hours.
		Returns 'time' dictionary.

		'''
		time = {}
		time['seconds'] = all_time_seconds % 60
		time['minutes'] = all_time_seconds // 60
		time['hours'] = time['minutes'] // 60
		time['minutes'] -= time['hours'] * 60

		return time

	def find_free_label(self):
		'''
		
		Searches the first not busy label, append to it button and return it.

		'''
		for label_index in range(4, 10):
			label_name = 'label_' + str(label_index)
			button_name = 'button_' + str(label_index)
			if not self.ui.__getattribute__(label_name).text():
				label = self.ui.__getattribute__(label_name)
				button = self.ui.__getattribute__(button_name)
				button.setFixedWidth(35)
				button.setText('OK')
				label.button = button
				button.clicked.connect(partial(self.remove_reminder, label))
				break
		return label

	def remove_reminder(self, label):
		'''

		Removes (hides) the reminder by setting an empty line as text for the label,
		the button size to zero, and signaling the timer function to end the stream.

		'''
		self.threads[label.objectName()] = False
		label.setText('')
		label.button.setFixedWidth(0)
		
	def timer(self, reminder_name):
		'''

		It implements the logic of the timer itself - stops the execution of
		its thread for the number of previously received seconds, and emits
		a sound signal after continuing the execution of its thread.
		Displays the name of the reminder and the time to end (every second)

		'''
		all_time_seconds = self.convert_in_seconds()
		label = self.find_free_label()
		sound = self.load_sound('beep')
		self.threads[label.objectName()] = True

		while all_time_seconds >= 0 and self.threads[label.objectName()]:
			time = self.converts_from_seconds(all_time_seconds)
			hours, minutes, seconds = time['hours'], time['minutes'], time['seconds']
			format_time = f' {hours}:{minutes}:{seconds}'
			label.setText(reminder_name + format_time)
			all_time_seconds -= 1
			sleep(1)
			
		sound.play()
		self.reminders_count -= 1
		thread.exit()


class MyDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	my_app = MyWin()
	my_app.show()
	my_app.setWindowTitle('PyTimer')
	icon = QtGui.QIcon('apple.ico')
	my_app.setWindowIcon(icon)
	sys.exit(app.exec_())

