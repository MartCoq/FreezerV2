FROM archlinux

RUN pacman -Sy

CMD docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

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
