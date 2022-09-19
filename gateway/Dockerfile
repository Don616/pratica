FROM nginx:latest

COPY ./index.html /usr/share/nginx/html/

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]