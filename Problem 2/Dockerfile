FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
ADD . /usr/src/app
CMD ["python", "./program.py"]
