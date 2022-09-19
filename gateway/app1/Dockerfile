FROM nginx:latest

COPY index.html /usr/share/nginx/html/

#RUN nginx -s reload

EXPOSE 80

ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]