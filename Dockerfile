#Dockerfile, Image, Container
FROM python:3.9

COPY imports.txt .

RUN pip install -r imports.txt

COPY . .
EXPOSE 5000

CMD ["python", "./main.py"]
