# clustershell-project


We need to add our superhost to the known hosts of all nodes using ssh to connect without requiring a password

Edit /etc/clustershell/groups to add a group (nodeset) in the following manner :

name_of_the_group: IP1, IP2, IP3

to execute a command from the commandline :
clush -w @node_all "the command"

## Setting up the project
- Run multiple VMs
- Start ssh in all VMs
- Configure the machines to connect automatically without password in the following manner :
	- **In the server (admin of the cluster)**
```bash
ssh-keygen -t rsa #run this command only once
ssh [IP] mkdir -p .ssh  #run this command for every VM
cat .ssh/id_rsa.pub | ssh [IP] 'cat >> .ssh/authorized_keys' #run this command for every VM
```

- Add the follow lines to the hosts file : ` /etc/hosts ` 
	- ip hostname;for every VM
#### Exp :
	192.168.1.1 test1
	192.168.1.2 test2 
- Edit the file ` /etc/clustershell/groups `:
	- name_of_the_group: hostname1, hostname2
#### Exp :
	node_all:  test1, test2

- To test your appliance run :
```bash
clush -w @node_all "echo hi"
```

## Interface architecture

```
├── Metaservices Handling
│   └── List Metaservices
│       ├── List Metaservices
│       ├── Show Metaservice Details
│       ├── Show Detailed Status
│       └── Show Status
└── Simple Service Handling
    ├── List Nodes
    │   └── List
    ├── List Services
    │   ├── Add Service
    │   └── Delete Service
    └── Manage Services
        ├── Start
        ├── Restart
        ├── Stop
        └── Status
```

### TODO 
- <del>learn about usefull commands for services</del>
- <del>learn the pythonic way to interact with clustershell</del>
- <del> add an HMI </del>
- add node from our program
- <del>use the hosts file to give up IPs</del>
- add colors
- add dependancy management

