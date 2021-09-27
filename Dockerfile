#Dockerfile, Image, Container
FROM python:3.9

COPY imports.txt .

RUN pip install -r imports.txt

ADD dining_hall.py .

ADD menu.py .

CMD ["python", "./dining_hall.py"]