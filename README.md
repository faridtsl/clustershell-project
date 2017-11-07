# clustershell-project


We need to add our superhost to the known hosts of all nodes using ssh to connect without requiring a password

Edit /etc/clustershell/groups to add a group (nodeset) in the following manner :

name_of_the_group : IP1, IP2, IP3

to execute a command from the commandline :
clush -w @node_all "the command"

### TODO 
	- learn about usefull commands for services
	- learn the pythonic way to interact with clustershell
	- add an HMI
	- add node from our program
	- use the hosts file to give up IPs
