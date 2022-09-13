FROM nginx
RUN mkdir /etc/nginx/ssl
RUN mkdir /home/cgi
RUN mkdir /var/log/nginx/jenkins
RUN apt update -yq
RUN apt install python3-pip -yq
RUN apt install libmariadb3 libmariadb-dev -yq
RUN pip3 install mariadb --no-input -q
RUN pip3 install cgi-tools --no-input -q
COPY nginx_cert.crt /etc/nginx/ssl
COPY nginx_key.key /etc/nginx/ssl
COPY passphrase_key_rsa /etc/nginx/ssl
#COPY static-html-directory/index.html /usr/share/nginx/html/index.html
COPY index.cgi /home/cgi/index.cgi
COPY afficher.cgi /home/cgi/afficher.cgi
COPY streaming.cgi /home/cgi/streaming.cgi
COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN apt-get install -y spawn-fcgi fcgiwrap \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


RUN sed -e '/^fastcgi_param  DOCUMENT_ROOT/ s/^#*/#/' -i /etc/nginx/fastcgi_params 
RUN sed -e '/^fastcgi_param  SCRIPT_NAME/ s/^#*/#/' -i /etc/nginx/fastcgi_params 
RUN chmod 755 -R /usr/share/nginx/
RUN chown nginx -R /usr/
RUN chown nginx:1000 -R /home/cgi
RUN chmod 775 -R /home/cgi

EXPOSE 2121
EXPOSE 80

STOPSIGNAL SIGTERM

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]




