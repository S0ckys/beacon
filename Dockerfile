FROM python:3.11.0

ADD main.py .
ADD client.py .

RUN pip install --upgrade pip
RUN pip install flask

CMD ["python", "./main.py"]
