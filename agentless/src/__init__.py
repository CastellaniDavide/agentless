"""agentless
"""
from sys import argv
import os
import subprocess
from csv import DictWriter
from tabular_log import tabular_log
from json import loads, dumps
import requests

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2021-3-22"

class agentless:
	def __init__ (self, verbose=False, csv=False, dbenable=False, dburl=None, dbtoken=None, dbOStable=None, dbNETtable=None):
		"""Where it all begins
		"""
		self.setup(verbose, csv, dbenable, dburl, dbtoken, dbOStable, dbNETtable) # Setup all the requirements

		try:
			self.core() # Try to run the core
		except:
			print("Error: make sure you have installed vbox on your PC")

	def setup(self, verbose, csv, dbenable, dburl, dbtoken, dbOStable, dbNETtable):
		"""Setup
		"""
		# Define main variabiles
		self.verbose = verbose
		self.csv = csv
		self.dbenable = dbenable
		self.dburl = dburl
		self.dbtoken = dbtoken
		self.dbOStable = dbOStable
		self.dbNETtable = dbNETtable

		# Define log
		try:
			self.log = tabular_log("C:/Program Files/agentless/trace.log" if os.name == 'nt' else "~/trace.log", title = "agentless" , verbose = self.verbose)
		except:
			self.log = tabular_log("trace.log", title = "agentless" ,verbose = self.verbose)
		self.log.print("Created log")

		# Headers
		self.OSheader = "PC_name,OS" # TODO
		self.net_header = "PC_name,network_card_name,IPv4,MAC,Attachment" # TODO
		self.log.print("Headers inizialized")

		# If selected setup csv
		if self.csv:
			# Define files
			self.OS = "OS.csv"
			self.net = "net.csv"
			self.log.print("Defined CSV files' infos")

			# Create header if needed
			try:
				if open(self.OS, 'r+').readline() == "":
					assert(False)
			except:
				open(self.OS, 'w+').write(self.OSheader + "\n")

			try:
				if open(self.net, 'r+').readline() == "":
					assert(False)
			except:
				open(self.net, 'w+').write(self.net_header + "\n")
			
			self.log.print("Inizialized CSV files")

	def core(self):
		"""Core of all project
		"""

		"""
		 # TODO
		if self.csv:
			DictWriter(open(self.OS, 'a+', newline=''), fieldnames=self.OSheader.split(","), restval='').writerow({})
				
		# If DB enabled try to insert infos
		if self.dbenable:
			try:
				response = requests.request("POST", f"{self.dburl}", headers={'Content-Type': 'application/json','Authorization': f'''Basic {self.dbtoken}'''}, data=dumps({"operation": "insert", "schema": "dev", "table": self.dbOStable, "records": [{}]}))
				self.log.print(f"By DB: {response.text}")
			except:
				self.log.print(f"Failed the DB insert")
		"""

	def get_output(self, array):
		""" Gets the output by the shell
		"""
		if os.name == 'nt': # If OS == Windows
			cmd = self.vboxmanage
			for i in array:
				if " " in i:
					i = "'" + i + "'"
				cmd += " "  + i

			return agentless.remove_b(subprocess.check_output(cmd, shell=False))
		else:
			return agentless.remove_b(subprocess.Popen([self.vboxmanage] + array, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])

	def remove_b(string):
		"""Removes b'' by string
		"""
		return str(string).replace("b'", "")[:-1:]

def laucher():
	""" Lauch all getting the params by the arguments passed on launch
	"""
	# Get all aarguments
	debug = "--debug" in argv or "-d" in argv
	csv = "--csv" in argv
	dbenable = dburl = dbtoken = dbOStable = dbNETtable = None

	for arg in argv:
		if "--url=" in arg:
			dburl = arg.replace("--url=", "")
		if "--token=" in arg:
			dbtoken = arg.replace("--token=", "")
		if "--OStable=" in arg:
			dbOStable = arg.replace("--OStable=", "")
		if "--NETtable=" in arg:
			dbNETtable = arg.replace("--NETtable=", "")

	# Launch the principal part of the code
	if dburl != None and dbtoken != None and dbOStable != None and dbNETtable != None:
		agentless(debug, csv, True, dburl, dbtoken, dbOStable, dbNETtable)
	else:
		agentless(debug, csv)
		
if __name__ == "__main__":
	laucher()
