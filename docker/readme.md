#build the docker image
docker build --rm -t centos7systemd /path/to/this/directory

#run a container
docker run -itd --privileged --name=pythontask1 centos7systemd

#log in 
docker exec -it pythontask1 /bin/bash

#execute
systemctl enable pythontask.service
systemctl start pythontask.service
