from fastapi import APIRouter, UploadFile, File
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

router = APIRouter()


@router.post("/speech_to_text")
async def speech_to_text(file: UploadFile = File(...)):
    recognizer = sr.Recognizer()

    if file.filename.lower().endswith((".mp3", ".ogg", ".wav", ".flac", ".aac", ".wma", ".m4a", ".aiff", ".au")):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_file_name = temp_file.name

            audio = AudioSegment.from_file(file.file)
            audio.export(temp_file_name, format="wav")

            with sr.AudioFile(temp_file_name) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
    else:
        text = "Unsupported file format."

    return {"text": text}
