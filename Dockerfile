FROM python:3.8-slim-buster
RUN apt-get update
RUN apt-get -y install tesseract-ocr python3-opencv
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]