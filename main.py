from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import io
from PIL import Image
import face_recognition

app = FastAPI()

class ImageData(BaseModel):
    image_base64: str

@app.post("/detect-face/")
async def detect_face(data: ImageData):
    try:
        # Decode base64
        image_bytes = base64.b64decode(data.image_base64)
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

        # Detect face
        image_np = face_recognition.load_image_file(io.BytesIO(image_bytes))
        face_locations = face_recognition.face_locations(image_np)

        return {"face_detected": bool(face_locations)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")
