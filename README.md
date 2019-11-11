**Systemd Service**  

Tested using  
python version 2.7.5  
also works with pyhon3  

The service is running a python file named updatemotd.py  
There is a service.timer in place which runs the service once a day and 1 minute after booting.

***
**REST Api using flask/python**  
You can get the info using a curl request like  
```curl http://178.62.9.210:5000/info```  
There is a sysmted service in place to run the api file apigetinfo.py  
Keep in mind the host IP is hardcoded.  

***

**DOCKER**  
Tested using  
Ubuntu 18.04.3  
Docker version 19.03.1  

build the image  
```docker build --rm -t nameofimage /path/to/dockerfile/directory```

run a container with it  
```docker run -itd --privileged --name=chooseyourname nameofimage```

access console on container  
```docker exec -it chooseyourname /bin/bash```  

Run the service  
```systemctl start pythontask.service```  

Check if it worked  
```cat /etc/motd```  

***

**PACKER image using qemu+kickstart+ansible**

Tested using  
CentOS 7.7  
Packer version 1.4.3  
QEMU emulator version 2.0.0  
libvirtd 4.5.0  
ansible 2.8.5  

Build the image using something like  

buid the image  
```PACKER_LOG=1 /usr/local/bin/packer build centos7-base.json```

to use the newly created qcow2 image do something like  
```virt-customize -a /home/packer-image/centos7-base-img-server4a/testserver4a --root-password password:usesamepasswordasksfile --uninstall cloud-init```

and then actually create a vm using  
```virt-install --name testserver2a --memory 512 --vcpus 1 --os-type linux --os-variant centos7.0 --disk '/home/packer-image/centos7-base-img-server4a/testserver4a' --import --network network=default --graphics none```

**Ansible**

There are two roles present at the moment. 

One is adding the pythontask systemd service while the other is instating the Api and the relative service it runs under. 
Some of the shell commands are executed in the kickstarter file under ```"provisioners":``` ```"type": "shell"``` while others from within Ansible just to show 2 different ways of achieving the same goal. Same goes for adding files - some using  ```"provisioners":``` ```"type": "file"``` while others via ansible.


***

**Prometheus and Grafana**  
Monitoring is setup and the dashboard can be accessed here (you will need login credentials)  

http://178.128.39.165:3000/d/1PGBpR1Zz/pythontask-service?orgId=1&from=1572993245396&to=1573036445396&refresh=30s  

http://178.128.39.165:9090/targets  

Alerting is actually setup for the pythontask.timer as the service runs once and goes inactive

***
