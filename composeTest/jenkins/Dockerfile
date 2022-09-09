FROM jenkins/jenkins
ENV JENKINS_OPTS --prefix=/jenkins
COPY ./docker_key.pub /var/jenkins_home/.ssh/authorized_keys
COPY ./jenkins_home /var/

