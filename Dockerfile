FROM python:3.7-buster
# Ngnix installation and configuration
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Installing app
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/Bike-pool-app
COPY requirements.txt start-server.sh /opt/app/
COPY bike_app /opt/app/Bike-pool-app/bike_app
COPY Bike_Pool_App /opt/app/Bike-pool-app/Bike_Pool_App
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN chmod 755 start-server.sh

# Exposing 8020 port so able to communicate from system
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]