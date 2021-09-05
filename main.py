from fastapi import FastAPI
from functools import lru_cache
import glob
import os
import pytesseract
import cv2

app = FastAPI(title="OCR Application")


def check_valid_file(fileName):
    """Checks file path and extension to prevent abuse"""
    return fileName.endswith(".png") and os.path.isfile(os.path.join("images", fileName))


@lru_cache()
def get_txt_from_image(document_id):
    """Preprocess Image and Return OCR text"""
    image_path = os.path.join("images", document_id)
    image = cv2.imread(image_path)    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshed, lang="eng")
    return text

@app.get("/get_doc_list")
async def get_doc_list():
    """Get valid PNG files from images directory"""
    fileList = []
    for file in glob.glob('images/*.png'):
        fileList.append(os.path.split(file)[1])
    return fileList


@app.get("/parse/{document_id}")
async def parse_document(document_id: str):
    """Return OCR data of sent document"""
    if not check_valid_file(document_id):
        return {"success": False, "error": "Invalid Document"}
    text = get_txt_from_image(document_id)
    return {"text": text}
