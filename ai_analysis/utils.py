from django.db.models.expressions import result
from django.shortcuts import render
import os
import requests
import docx
import fitz
from django.conf import settings
import google.generativeai as genai


# Create your views here.
def extract_text_from_file(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == '.docx':
        return extract_text_from_docx(file)
    elif ext == '.pdf':
        return extract_text_from_pdf(file)
    else:
        return "Formato no valido. Solo PDF y DOCX"


def extract_text_from_pdf(file):
    text = ""
    file.open()
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()


def extract_text_from_docx(file):
    text = ""
    file.open()
    doc = docx.Document(file)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text.strip()


def analyze_contract_text(text):
    genai.configure(api_key=settings.GOOGLE_AI_API_KEY)

    model = genai.GenerativeModel("gemini-2.0-flash")

    text_chunk = text[:1500] if len(text) > 1500 else text
    prompt = f"""
    Hola, necesito que leas y analices el siguiente contrato.
    Quiero que actúes como un asistente legal claro y directo, sin usar lenguaje demasiado técnico.
    Por favor, responde de manera estructurada, fácil de entender y con un tono conversacional.

    Indícame:
    
    1. ¿Hay alguna cláusula que imponga condiciones importantes, como exclusividad, no competencia, o renovación automática?
    2. ¿Detectas algo que pueda representar un riesgo para alguna de las partes? Si es así, ¿por qué podría ser problemático?
    3. Haz un resumen general del contrato: tipo de contrato, duración, obligaciones, pagos, jornada, prestaciones u otros puntos clave.
    4. ¿Recomendarías que esta persona consulte a un abogado antes de firmarlo? Si es así, explica brevemente por qué.
    
    Puedes usar viñetas o secciones para hacerlo más fácil de leer.
    
    Contrato: {text_chunk}
        """

    try:
        response = model.generate_content(prompt, generation_config=genai.GenerationConfig(temperature=0.2,
                                                                                           max_output_tokens=1500))
        return response.text
    except Exception as e:
        return f"Error al analizar el contrato: {e}"

def answer_question(contract_text,question,chat_context=""):

    genai.configure(api_key=settings.GOOGLE_AI_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    Estás actuando como un asistente legal inteligente.

    Este es el contrato en discusión:
    
    {contract_text}
    Aquí está el historial reciente de preguntas y respuestas con el usuario:
    {chat_context}
    Nueva pregunta del usuario:
    {question}
    Responde con claridad, lenguaje sencillo y estilo conversacional. Si no hay suficiente información en el contrato, acláralo.
    """

    try:
        response = model.generate_content(prompt, generation_config=genai.GenerationConfig(temperature=0.2,
                                                                                           max_output_tokens=1500))
        return response.text
    except Exception as e:
        return f"Error al analizar el contrato: {e}"



