FROM centos:7
ENV container=docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*; \
mkdir /home/python;
WORKDIR /home
COPY updatemotd.py .
WORKDIR /etc/systemd/system
COPY pythontask.service .
WORKDIR /etc/systemd/system
COPY pythontask.timer . 
VOLUME /run /tmp
RUN yum -y install nano
CMD ["/usr/sbin/init"]

