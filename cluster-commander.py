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
		r = ""
		for buf, nodes in task.iter_buffers():
			r += str(nodes) + " " +  str(buf) + "\n"
		return r
		

	def status_services(self):
		cmd = "service --status-all"
		services_str = ""
		for s in self.services:
			services_str += " -e " + s
		greping = "grep " + services_str 
		return self.execute_command(cmd + " | " + greping)

	def take_action_service(self, s, a):
		cmd = "service " + s + " " + a
		return self.execute_command(cmd)
	
	def start_service(self, s):
		return self.take_action_service(s,"start")
	
	def restart_service(self, s):
		return self.take_action_service(s,"restart")
	
	def stop_service(self, s):
		return self.take_action_service(s,"stop")

	def get_service_status(self, s):
		task = task_self()
		cmd = "service " + s + " status | grep Active"
		task.run(cmd, nodes=self.nodes)
		r = ""
		for buf, nodes in task.iter_buffers():
			r += str(nodes) + " " +  str(buf) + "\n"
		return r

obj = ClusterCommander()
print(obj.get_service_status("ntp"))


