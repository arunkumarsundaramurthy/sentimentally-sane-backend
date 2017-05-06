FROM ubuntu:latest
MAINTAINER Arun "arunkumarsundaramurthy@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV API_KEY=81c1c3b49244408bb8d8b1fa5450b9ff
ENV DEGUB=True
ENTRYPOINT ["python"]
CMD ["app.py"]