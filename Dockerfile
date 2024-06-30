FROM python:3.11.0

ADD main.py .

RUN pip install --upgrade pip

CMD ["python", "./main.py"]
