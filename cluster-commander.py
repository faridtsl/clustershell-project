from ClusterShell.Task import task_self
from ClusterShell.NodeSet import NodeSet, RangeSet


class ClusterCommander:
	
	def __init__(self):
		self.nodes = NodeSet('@node_all')

	def execute_command(self,cmd):
		task = task_self()
		task.run(cmd, nodes=self.nodes)

	for buf, nodes in task.iter_buffers():
		print nodes, buf
