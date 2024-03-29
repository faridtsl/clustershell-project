from DistServiceHandler import DistServiceHandler
from MetaServiceHandler import MetaServiceHandler
import MetaServicesCfg as config
from const import *
import subprocess as sp


class ClusterHandlingMenu:
	
	def __init__(self):
		self.config = config.meta
		self.services = []
		with open(SERVICES_CONF) as f:
			self.services = f.readlines()
		self.services = [x.strip() for x in self.services]
		self.serviceHandler = DistServiceHandler()
		self.nodes = self.serviceHandler.nodes
		self.metaHandler = MetaServiceHandler()

	
	#### Metaservices Menu
	def print_metaservices(self):
		c = 1
	 	for k in self.config.keys():
			print "\t" + str(c) + "- " + k;
			c += 1

	def get_service(self):
		l = self.config.keys()
		i = raw_input("Your choice by name or index : ")
		s = i
		try:
			idx = int(i)
			if idx < 1 or idx > len(l):
				print "Please enter a valid index"
				return None
			else:
				s = l[idx-1]
		except:
			if s not in l:
				print "Please enter a valid name"
				return None
		return s

	def show_metaservices_details_submenu(self):
		self.print_metaservices()
		s = self.get_service()
		if s == None:
			return 0
		print self.metaHandler.config[s]
		print "1- Start"
		print "2- Restart"
		print "3- Stop"
		print "4- Back"
		i = raw_input("Your choice [1-4] : ")
		if i == "1":
			print self.metaHandler.start_meta(s)
		elif i == "2":
			print self.metaHandler.restart_meta(s)
		elif i == "3":
			print self.metaHandler.stop_meta(s)
		elif i == "4":
			return 0
		else:
			print "Please choose a valid option"
		return 1
	
	def show_detailed_status_submenu(self):
		self.print_metaservices()
		s = self.get_service()
		if s == None:
			return 0
		print self.metaHandler.status_meta_details(s)

	def show_status_submenu(self):
		self.print_metaservices()
		s = self.get_service()
		if s == None:
			return 0
		print self.metaHandler.status_meta(s)
		
	def list_metaservice_menu(self):
		print "1- List Metaservices"
		print "2- Show Metaservices Details (Start|Restart|Stop)"
		print "3- Show Detailed Status"
		print "4- Show Status"
		print "5- Back"
		i = raw_input("Your Choice [1-4] : ")
		if i == "1":
			self.print_metaservices()
		elif i == "2":
			self.show_metaservices_details_submenu()
		elif i == "3":
			self.show_detailed_status_submenu()
		elif i == "4":
			self.show_status_submenu()
		elif i == "5":
			return 0
		else:
			print "Please choose a valid option"
		return 1

	
	# Simple services handling
	def print_list_nodes(self):
		c = 1
		for n in self.nodes:
			print "\t" + str(c) + "- " + n
			c += 1

	def print_list_services(self):
		c = 1
		for s in self.services:
			print "\t" + str(c) + "- " + s
			c+=1

	def write_list_services(self):
		self.services = list(set(self.services))
		f = open('services.config', 'w')
		for s in self.services:
			f.write(s+"\n")
		f.close() 
	
	def add_service(self, s):
		self.services.append(s)
		self.write_list_services()

	def remove_service(self, s):
		self.services.remove(s)
		self.write_list_services()

	def get_simple_service(self, can_all=False):
		l = self.services
		i = raw_input("Your choice by name or index : ")
		s = i
		try:
			idx = int(i)
			if idx < 1 or idx > len(l):
				if can_all and idx == (len(l) + 1):
					return "all"
				print "Please enter a valid index"
				return None
			else:
				s = l[idx-1]
		except:
			if s not in l:
				print "Please enter a valid name"
				return None
		return s

	def manage_services_submenu(self):
		self.print_list_services()
		print "\t" + str(len(self.services)+1) + "- all"
		s = self.get_simple_service(can_all=True)
		if s == "all":
			self.serviceHandler.set_services(self.services)
		elif s != None:
			self.serviceHandler.set_services([s])
		else:
			return 0
		print "1- Start"
		print "2- Restart"
		print "3- Stop"
		print "4- Status"
		print "5- Back"
		i = raw_input("Your Choice [1-5] : ")
		if i == "1":
			print "Starting ..."
			try :
				print self.serviceHandler.start_all()
			except:
				print "[-] Failed"
				return -1
			print "[+] Success" 
		elif i == "2":
			print "Restarting ..."
			try :
				print self.serviceHandler.restart_all()
			except:
				print "[-] Failed"
				return -1
			print "[+] Success" 
		elif i == "3":
			print "Stopping ..."
			try :
				print self.serviceHandler.stop_all()
			except:
				print "[-] Failed"
				return -1
			print "[+] Success" 
		elif i == "4":
			print self.serviceHandler.status_all()
		elif i == "5":
			return 0
		else:
			print "Please choose a valid option"
		return 1
	
	def list_services_submenu(self):
		self.print_list_services()
		print "1- Add"
		print "2- Remove"
		print "3- Back"
		i = raw_input("Your Choice [1-3] : ")
		if i == "1":
			s = raw_input("Service name : ")
			self.add_service(s)
		elif i == "2":
			s = self.get_simple_service()
			if s != None:
				self.remove_service(s)
		elif i ==  "3":
			return 0
		else:
			print "Please choose a valid option"
		return 1

	def list_simple_service_handling(self):
		print "1- List Nodes"
		print "2- List Services"
		print "3- Manage Services"
		print "4- Back"
		i = raw_input("Your Choice [1-4] : ")
		if i == "1":
			self.print_list_nodes()
		elif i == "2":
			self.list_services_submenu()
		elif i == "3":
			self.manage_services_submenu()
		elif i == "4":
			return 0
		else:
			print "Please choose a valid option"
		return 1

	# General menu
	def general_menu(self):
		print "1- Simple Service Handling"
		print "2- Metaservice Handling"
		print "3- Exit"
		i = raw_input("Your choice [1-3] : ")
		tmp = sp.call('clear',shell=True)
		if i == "1":
			while self.list_simple_service_handling() == 1:
				#tmp = sp.call('clear',shell=True)
				pass
		elif i == "2":
			while self.list_metaservice_menu() == 1:
				#tmp = sp.call('clear',shell=True)
				pass
		elif i == "3":
			return 0
		else:
			print "Please choose a valid option"
		return 1

obj = ClusterHandlingMenu()
while obj.general_menu() == 1:
	tmp = sp.call('clear',shell=True)
	pass
