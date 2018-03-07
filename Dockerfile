FROM uzzal2k5/nginx-ssl-python3.5
MAINTAINER uzzal

#RUN apt-get install vim
COPY req/requirements.txt /
RUN chmod +x ./requirements.txt
RUN pip3 install -r ./requirements.txt

COPY ssl/ssl_web.sh /
RUN chmod +x ./ssl_web.sh
RUN sh ./ssl_web.sh


