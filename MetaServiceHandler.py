from DistServiceHandler import DistServiceHandler
import MetaServicesCfg as meta_config

class MetaServiceHandler:

	def __init__(self):
		self.config = meta_config.meta

	def start_meta(self, name):
		nodes = self.config[name].keys()
		r = ""
		for n in nodes:
			dsh = DistServiceHandler(nodes=n)
			for s in self.config[name][n]['services']:
				r += dsh.start_service(s)
		return r

	def restart_meta(self, name):
		nodes = self.config[name].keys()
		r = ""
		for n in nodes:
			dsh = DistServiceHandler(nodes=n)
			for s in self.config[name][n]['services']:
				r += dsh.restart_service(s)
		return r
	
	def stop_meta(self, name):
		nodes = self.config[name].keys()
		r = ""
		for n in nodes:
			dsh = DistServiceHandler(nodes=n)
			for s in self.config[name][n]['services']:
				r += dsh.stop_service(s)
		return r
	
	def status_meta_details(self, name):
		nodes = self.config[name].keys()
		r = ""
		for n in nodes:
			dsh = DistServiceHandler(nodes=n,services=self.config[name][n]['services'])
			r += dsh.status_services()
		return r
	
	def status_meta(self,name):
		st = self.status_meta_details(name)
		code = ""
		if "[ - ]" in st:
			code = "[ - ]"
		elif "[ ? ]" in st:
			code = "[ ? ]"
		else:
			code = "[ + ]"
		return code + " " + name

