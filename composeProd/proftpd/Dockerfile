from ubuntu

RUN apt-get -y update
RUN apt-get install -y -q proftpd-basic

COPY proftpd.conf /etc/proftpd/proftpd.conf
COPY modules.conf /etc/proftpd/modules.conf

# pour ajouter la conf TLS on peut rajouter les docs suivants :
#COPY tls.conf /etc/proftpd/tls.conf
#COPY proftpd.crt /etc/ssl/certs/proftpd.crt
#COPY proftpd.key /etc/ssl/private/proftpd.key

RUN useradd freezer
RUN echo "freezer:freezer" | chpasswd
RUN mkdir -p /home/freezer/music
RUN mkdir -p /home/cgi
RUN chown freezer: -R /home/freezer/music
RUN chown freezer:1000 -R /home/cgi
RUN chmod 775 -R /home/cgi

EXPOSE 21
EXPOSE 30001
EXPOSE 30002
EXPOSE 30003

CMD proftpd --nodaemon -c /etc/proftpd/proftpd.conf


