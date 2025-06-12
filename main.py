from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import io
import cv2
import numpy as np

app = FastAPI()

class ImageData(BaseModel):
    image_base64: str

# Carregando classificador pré-treinado do OpenCV (detecção de rostos)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.post("/detect-face/")
async def detect_face(data: ImageData):
    try:
        # Decodifica base64
        image_bytes = base64.b64decode(data.image_base64)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if img is None:
            raise Exception("Imagem inválida ou não pôde ser lida.")

        # Converte para escala de cinza (necessário para detecção de rosto com OpenCV)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detecta rostos
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        return {"face_detected": len(faces) > 0}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")
