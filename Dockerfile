FROM ubuntu
MAINTAINER Lars Yencken
ADD . /wide-language-demo
RUN sed -i 's/main restricted/main restricted universe/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y make curl
RUN cd /wide-language-demo && make bootstrap
