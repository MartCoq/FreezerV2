FROM mariadb:latest
COPY init-freezer.sql /docker-entrypoint-initdb.d/init-freezer.sql
RUN chown mysql: docker-entrypoint-initdb.d -R
EXPOSE 3306
CMD ["mariadbd"]
