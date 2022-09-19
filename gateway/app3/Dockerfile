FROM nginx:latest

COPY . /usr/share/nginx/html/

#RUN nginx -s reload

EXPOSE 80

ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]