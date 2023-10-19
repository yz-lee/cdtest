FROM ubuntu
USER root

RUN apt update
RUN apt install python3 python3-pip -y
RUN apt-get install -y python3-pip
RUN pip install flask
RUN pip install flask-wtf
EXPOSE 5000
COPY myformcsrf.py .
COPY templates ./templates
ENTRYPOINT [ "python3" ]
CMD [ "myformcsrf.py" ]