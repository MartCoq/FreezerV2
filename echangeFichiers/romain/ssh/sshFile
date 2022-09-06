FROM archlinux
RUN useradd jenkins
RUN mkdir -p /home/jenkins/deploy/spark
RUN pacman -Sy
RUN pacman -S openssh --noconfirm
RUN pacman -S vim --noconfirm
RUN pacman -S net-tools --noconfirm
RUN pacman -S jre11-openjdk --noconfirm
RUN pacman -S git --noconfirm
RUN pacman -Sy maven --noconfirm
RUN ssh-keygen -A
COPY ./docker_key.pub /home/jenkins/.ssh/authorized_keys
RUN chown -R jenkins /home/jenkins/
EXPOSE 22
CMD /usr/sbin/sshd -D
