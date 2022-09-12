FROM jenkins/jenkins
ENV JENKINS_OPTS --prefix=/jenkins
COPY ./jenkins_home /var/jenkins_home
COPY ./docker_key.pub /var/jenkins_home/.ssh/authorized_keys
