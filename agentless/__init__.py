"""agentless
"""
from sys import argv
import os
import subprocess
from csv import DictWriter
from tabular_log import tabular_log
from json import loads, dumps
import ipaddress
import requests
from threading import Thread, active_count
from ping3 import ping, verbose_ping
from datetime import datetime

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2021-3-22"

class agentless:
	def __init__ (self, verbose=False, csv=False, multithread=True, adresses="192.168.1.0/24", dbenable=False, dburl=None, dbtoken=None, dbtable=None):
		"""Where it all begins
		"""
		self.setup(verbose, csv, multithread, adresses, dbenable, dburl, dbtoken, dbtable) # Setup all the requirements

		self.core()

	def setup(self, verbose, csv, multithread, adresses, dbenable, dburl, dbtoken, dbtable):
		"""Setup
		"""
		# Define main variabiles
		self.instance_code = int(datetime.now().timestamp())
		self.verbose = verbose
		self.csv = csv
		self.multithread = multithread
		self.dbenable = dbenable
		self.dburl = dburl
		self.dbtoken = dbtoken
		self.dbtable = dbtable
		self.IP = []
		self.IPs = []
		for i in adresses:
			self.IPs += [str(ip) for ip in ipaddress.ip_network(i).hosts ()]

		# Define log
		try:
			self.log = tabular_log("C:/Program Files/agentless/trace.log" if os.name == 'nt' else "~/trace.log", title = "agentless" , verbose = self.verbose, serverlink=None)
		except:
			self.log = tabular_log("trace.log", title = "agentless" ,verbose = self.verbose)
		self.log.print("Created log")

		# Headers
		self.header = "istance,IP,active"
		self.log.print("Headers inizialized")

		# If selected setup csv
		if self.csv:
			# Define files
			self.csv = "ping.csv"
			self.log.print("Defined CSV files' infos")

			open(self.csv, 'w+').write(self.header + "\n")
			
			self.log.print("Inizialized CSV files")

	def ping(self, ip):
		"""Run a single ping
		"""
		self.IP.append({"istance": int(datetime.now().timestamp()), "IP": ip, "active" : ping(ip) != None})

	def core(self):
		"""Core of all project
		"""
		# Get data
		if self.multithread:
			for ip in self.IPs:
				Thread(target=self.ping, args=(ip,)).start()
			while active_count() > 1:
				pass
		else:
			for ip in self.IPs:
				self.ping(ip)
		
		self.log.print("Pinged all")

		# If csv is enabled add data to csv
		if self.csv:
			DictWriter(open(self.csv, 'a+', newline=''), fieldnames=self.header.split(","), restval='').writerows(self.IP)
			self.log.print("Salved data on the csv")
				
		# If DB enabled try to insert infos
		if self.dbenable:
			try:
				response = requests.request("POST", f"{self.dburl}", headers={'Content-Type': 'application/json','Authorization': f'''Basic {self.dbtoken}'''}, data=dumps({"operation": "insert", "schema": "dev", "table": self.dbtable, "records": self.IP}))
				self.log.print(f"By DB: {loads(response.text)['message']}")
			except:
				self.log.print(f"Failed the DB insert")

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
	dbenable = dburl = dbtoken = dbtable = None
	multithread = "--single" not in argv
	adresses = []

	for arg in argv:
		if "--url=" in arg:
			dburl = arg.replace("--url=", "")
		if "--token=" in arg:
			dbtoken = arg.replace("--token=", "")
		if "--table=" in arg:
			dbtable = arg.replace("--table=", "")
		if "--adresses=" in arg:
			adresses.append(arg.replace("--adresses=", ""))

	if adresses == []:
		adresses = ["192.168.1.0/24"]

	# Launch the principal part of the code
	if dburl != None and dbtoken != None and dbtable != None:
		agentless(debug, csv, multithread, adresses, True, dburl, dbtoken, dbtable)
	else:
		agentless(debug, csv, multithread, adresses)
		
if __name__ == "__main__":
	laucher()
