FROM ubuntu

MAINTAINER Harsh Reddy <vnsharshavardhanreddy@gmail.com>

RUN apt update -y && apt install python3 -y

COPY duplicate.py /opt/

COPY folder/ /opt/

COPY entrypoint.sh /opt/

RUN chmod 777 /opt/

WORKDIR /opt/

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
