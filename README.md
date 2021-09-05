# OCRAPI

This is my submission for ClassForma Internship.  

As per my problem statement, I had to build a API Service that will run OCR on given images.  

### My Approach  
- Received the document_id on /parse endpoint.
- Verified document_id is a valid file in the images directory.
- Started Preprocessing the Image.
  - Converted it to grayscale
  - Thresholded Image
- Pass image to pytesseract
- Return ocr text.

As it was said to return the text directly on call, it takes time to respond. A better approach would have been to create a Job and run it as a BackgroundTask.  
To avoid late response on the given approach lru_cache was used to cache the results.  

I have used pytesseract as its a Python Wrapper on Tesseract OCR by Google. As Tesseract is considered as one of the most accurate open source OCR engine, I decided to use it.

## Deploy
#### With Docker
- Make sure `docker-compose` is installed.
- Type `sudo docker-compose up -d` 
- Now the API should be live at `http://localhost:5000`
#### Without Docker
- Make sure to install tesseract-ocr.
- Type `pip3 install -r requirements.txt`
- Now deploy by typing `uvicorn main:app --port 5000`
- Now the API should be live at `http://localhost:5000`
