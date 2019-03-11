FROM centos:7.6.1810

RUN yum -y install rsync openssh-clients epel-release
ADD oc-3.10.111-linux.tar.gz /usr/bin/
RUN yum install -y python python-urllib3 python-requests python-pip && yum clean all && rm -rf /var/cache/yum/*
RUN pip install --upgrade pip
COPY app /app
RUN mkdir /backups && chmod 777 /backups
