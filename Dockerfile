FROM ubuntu:latest
RUN apt-get update && apt-get install python3.9 -y
RUN apt-get install -y pip python-dev build-essential
RUN rm -rf /var/lib/apt/lists
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]