from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pdf_utils import personalize_pdf
from email_utils import send_email
from code_check import is_valid_code, mark_code_used
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://rethinkmoney.github.io"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send")
async def send_pdf(email: str = Form(...), code: str = Form(...)):
    if not is_valid_code(code):
        return {"status": "error", "message": "Ungültiger oder verbrauchter Gutscheincode."}

    output_path = f"output/{email}.pdf"
    personalize_pdf("template.pdf", output_path, email)
    mark_code_used(code)
    send_email(
        email,
        "Buch ReThink Money",
        "Im Anhang findest du dein Exemplar des Buches. Bitte beachte, dass dies eine noreply Mail ist. Kontaktaufnahme bitte via Threema. ThreemaID: E7T69HDV",
        output_path
    )

    return {"status": "ok", "message": "Das PDF wurde an deine E-Mailadresse gesendet."}
