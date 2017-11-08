from DistServiceHandler import DistServiceHandler
from MetaServiceHandler import MetaServiceHandler
import MetaServicesCfg as config


class ClusterHandlingMenu:
	
	def __init__(self):
		self.config = config.meta 
	


	#### Metaservices Menu
	def print_metaservices(self):
		c = 1
	 	for k in self.config.keys():
			print str(c) + "- " + k;
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
		print "got : " + str(s)
		
		
	def list_metaservice_menu(self):
		print "1- List Metaservices"
		print "2- Show Metaservices Details"
		print "3- Show Detailed Status"
		print "4- Show Status"
		i = raw_input("Your Choice [1-4] : ")
		if i == "1":
			self.print_metaservices()
		elif i == "2":
			self.show_metaservices_details_submenu()
		elif i == "3":
			self.show_detailed_status_submenu()
		elif i == "4":
			self.show_status_submenu()
		else:
			print "Please choose a valid option"




obj = ClusterHandlingMenu()
obj.list_metaservice_menu()
