from ClusterShell.Task import task_self
from ClusterShell.NodeSet import NodeSet, RangeSet

SERVICES_CONF = "services.config"
METASERVICES_CONF = "meta-services.config"

class ClusterCommander:
	
	def __init__(self):
		self.nodes = NodeSet('@node_all')
		self.services = []
		with open(SERVICES_CONF) as f:
			self.services = f.readlines()
		self.services = [x.strip() for x in self.services] 

	def execute_command(self,cmd):
		task = task_self()
		task.run(cmd, nodes=self.nodes)
		for buf, nodes in task.iter_buffers():
			print nodes, buf

	def status_services(self):
		cmd = "service --status-all"
		services_str = ""
		for s in self.services:
			services_str += " -e " + s
		greping = "grep " + services_str 
		self.execute_command(cmd + " | " + greping)

	def take_action_service(self, s, a):
		cmd = "service " + s + " " + a
		self.execute_command(cmd)
	
	def start_service(self, s):
		self.take_action_service(s,"start")
	
	def restart_service(self, s):
		self.take_action_service(s,"restart")
	
	def stop_service(self, s):
		self.take_action_service(s,"stop")

obj = ClusterCommander()
obj.status_services()


