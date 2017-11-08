# clustershell-project


We need to add our superhost to the known hosts of all nodes using ssh to connect without requiring a password

Edit /etc/clustershell/groups to add a group (nodeset) in the following manner :

name_of_the_group : IP1, IP2, IP3

to execute a command from the commandline :
clush -w @node_all "the command"

## Important tasks
	- Run multiple VMs
	- Start ssh in all VMs
	- Configure the machines to connect automatically without password in the following manner :
		- In the server (admin of the cluster)
		```bash
		ssh-keygen -t rsa #run this command only once
		ssh [IP] mkdir -p .ssh  #run this command for every VM
		cat .ssh/id_rsa.pub | ssh [IP] 'cat >> .ssh/authorized_keys' #run this command for every VM
		```

### TODO 
- <del>learn about usefull commands for services</del>
- <del>learn the pythonic way to interact with clustershell</del>
- add an HMI
- add node from our program
- <del>use the hosts file to give up IPs</del>
- add colors
