FROM nginx:latest

COPY grintric.conf /etc/nginx/sites-available/grintric.conf

RUN mkdir -p /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/grintric.conf /etc/nginx/sites-enabled/

RUN rm /etc/nginx/conf.d/default.conf # Remove default config

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]