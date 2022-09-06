FROM mariadb:latest
COPY init-freezer.sql /docker-entrypoint-initdb.d/init-freezer.sql
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /
RUN chown mysql: docker-entrypoint.sh
RUN chown mysql: docker-entrypoint-initdb.d -R
RUN chmod 755 docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 3306
CMD ["mariadbd"]
