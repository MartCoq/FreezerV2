FROM jenkins/jenkins
USER jenkins
ENV JENKINS_OPTS --prefix=/jenkins
RUN chown jenkins:jenkins -R /var
COPY ./jenkins_home /var/jenkins_home
COPY ./docker_key.pub /var/jenkins_home/.ssh/authorized_keys
