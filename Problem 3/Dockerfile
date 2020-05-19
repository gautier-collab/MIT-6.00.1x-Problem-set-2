FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
COPY . /usr/src/app
CMD ["python", "./program.py"]
