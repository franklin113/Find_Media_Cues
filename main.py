import re
from tkinter import *

class search_gui(object):

	def __init__(self, master):

		self.master = master

		self.instructionText = Label(self.master, text='Enter filename below:')
		self.searchButton = Button(self.master, text='Search', command=self.search_callback)

		self.filenameStringVar = StringVar()
		self.filenameEntry = Entry(self.master, textvariable=self.filenameStringVar)

		#this changes after you search
		self.auxNameVariable = StringVar()
		self.auxNameReturned = Label(textvariable = self.auxNameVariable )
		self.auxNameVariable.set('') #start it blank

		self.setup_grid()

		#keyboard shortcuts
		self.master.bind("<Return>", self.enter_callback)

		#when you open it you can immediately type
		self.filenameEntry.focus_force()

	def setup_grid(self):
		self.instructionText.grid(row=1,column=1)
		self.filenameEntry.grid(row=2, column=1,padx=10)
		self.searchButton.grid(row = 2,column=2)

		self.auxNameReturned.grid(row=3,column=1)

	def search_callback(self):
		clipboard = self.get_clipboard().splitlines()
		currentEntry = self.filenameStringVar.get()

		print("Entry: ",currentEntry)

		textScanner = scanner(currentEntry,clipboard)
		auxName = textScanner.perform_search()
		print('Aux name string: ', auxName)
		self.auxNameVariable.set(auxName)


		print("Auxname string var: " ,self.auxNameVariable.get())

	def get_clipboard(self):
		return self.master.clipboard_get()

	def enter_callback(self,event):
		#so i didn't have to do a lambda
		self.search_callback()

class scanner(object):

	'''
	scans data for a set of tokens-

	1) keep track of when a new timeline starts
	2) find the aux timeline name
	3) find the filename

	'''

	def __init__(self,filename,listOfStringsToSearch):
		#takes a list of strings (splitlines)

		'''

		:param filename:  the name to search for
		:param listOfStringsToSearch:  the watchout data, split into list of strings

		must search line by line
		'''


		self.splitLinesData = listOfStringsToSearch
		self.beginAuxObjectPattern = ', // mTaskNum'
		self.auxTimelineNamePattern = r'(["])(.*)(", // mName)'  # we need to get group(2)
		self.filename = filename
		self.cueIDPattern = r'(\d)(, // mCueID)'

		self.beginAuxRe = re.compile(self.beginAuxObjectPattern)
		self.auxTimelineNameRe = re.compile(self.auxTimelineNamePattern)
		self.filenameRe = re.compile(self.filename)
		self.cueIDRe = re.compile(self.cueIDPattern)


		self.currentTimeline = ''

		#self.perform_search(self.splitLinesData)

	def find_aux_start_token(self, curLine):

		mo = self.beginAuxRe.search(curLine)

		if mo != None:
			return True
		else:
			return False

	def find_aux_timeline_name(self, curLine):

		mo = self.auxTimelineNameRe.search(curLine)

		if mo != None:
			return mo.group(2) #return the name as a string
		else:
			return None

	def find_filename(self,curLine):

		mo = self.filenameRe.search(curLine,re.IGNORECASE)

		if mo is not None:
			return mo.group()
		else:
			return None

	def perform_search(self):

		foundAux = False
		foundTimelineName = False
		foundFileName = False


		for line in self.splitLinesData:
			#find aux start token
			if self.find_aux_start_token(line) == True:
				foundAux = True

			timelineName = self.find_aux_timeline_name(line)

			if foundAux == True and timelineName is not None:
				self.currentTimeline = timelineName
				foundTimelineName = True
				foundAux = False

			filename = self.find_filename(line)

			if filename is not None:

				foundAux = False
				foundTimelineName = False
				foundFileName = False
				print("Found File:\n%s" % (filename), "\nTimelines:\n\n%s" % (self.currentTimeline))
				return self.currentTimeline


if __name__ == '__main__':
	root = Tk()
	root.title('')
	root.geometry("200x80")
	search_gui(root)

	root.mainloop()

