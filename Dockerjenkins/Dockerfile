FROM jenkins/jenkins:lts

#COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

COPY https.pem /var/lib/jenkins/cert
COPY https.key /var/lib/jenkins/pk
#ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8083 --httpsCertificate=/var/lib/jenkins/cert --httpsPrivateKey=/var/lib/jenkins/pk
#EXPOSE 8083
#CMD chmod -R 777 /home/jmy/Jenkins/response

#CMD docker pull jenkins/jenkins:lts

#ENV JENKINS_SLAVE_AGENT_PORT 50001


#COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
#RUN pacman -Sy



#RUN pacman -S openssh --noconfirm

#RUN pacman -S jenkins --noconfirm

#RUN useradd remote_user && \
#    echo "1234" | passwd remote_user --stdin && \
#    mkdir /home/remote_user/.ssh && \
#    chmod 700 /home/remote_user/.ssh
#RUN useradd remote_user && \
#    mkdir -p /home/remote_user/.ssh

#COPY remote-key.pub /home/remote_user/.ssh/authorized_keys

#RUN chown remote_user:remote_user -R /home/remote_user/ && \
#    chmod 600 /home/remote_user/.ssh/authorized_keys



#EXPOSE 22


#RUN pacman -S jdk11-openjdk --noconfirm

#RUN archlinux-java set java-11-openjdk 


#CMD /usr/sbin/sshd -D
