FROM python:3.6-alpine

MAINTAINER wule61 <wule61@live.com>

RUN mkdir /app

ADD ./ /app

WORKDIR /app

ENV TZ "Asia/Shanghai"

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.10/main" > /etc/apk/repositories

RUN apk add --update \
      bash \
      vim \
      musl-dev \
      gcc \
      g++ \
      libxml2-dev \
      libxslt-dev \
      && rm -rf /var/cache/apk/*

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 10086

ENTRYPOINT ["python3","main.py"]