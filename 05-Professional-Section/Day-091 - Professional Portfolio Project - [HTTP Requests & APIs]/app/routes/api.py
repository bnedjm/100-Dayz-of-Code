import os
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename
from app.utils.helper import allowed_file_type
from app.services.converter_service import extract_text_from_pdf, convert_text_to_speech, save_audio_file
from uuid import uuid4
import tempfile

api_bp = Blueprint("api", __name__)

UPLOAD_FOLDER = '05-Professional-Section/Day-091 - Professional Portfolio Project - [HTTP Requests & APIs]/app/static/assets/pdf/'
MP3_SAVE_FOLDER = '05-Professional-Section/Day-091 - Professional Portfolio Project - [HTTP Requests & APIs]/app/static/assets/mp3/'

@api_bp.route("/", methods=['GET']) # type: ignore
def home():
    return jsonify({'response': 'Server is Live'})

@api_bp.route("/convert", methods=['POST']) # type: ignore
def pdf_to_mp3():
    """
    Endpoint to receive a PDF, convert it to an audiobook, and return the audio file.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file and allowed_file_type(file.filename):
        if file.filename:
            secure_filename(file.filename)
        pdf_filename = f"pdf_{uuid4()}.mp3"
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
        file.save(pdf_path)

        try:
            text = extract_text_from_pdf(pdf_path)

            if len(text.strip()) == 0:
                return jsonify({'error': 'No text extracted from the PDF file'}), 400

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
                audio_path = temp_audio_file.name

            convert_text_to_speech(text, output_audio_file_path=audio_path)

            audio_filename = f"audiobook_{uuid4()}.mp3"
            audio_file_path = os.path.join(MP3_SAVE_FOLDER, audio_filename)
            save_audio_file(audio_path, audio_file_path)

            return send_file(audio_path, as_attachment=True, download_name=audio_filename)

        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500

        finally:
            # if os.path.exists(pdf_path):
            #     os.remove(pdf_path)
            if os.path.exists(audio_path):
                os.remove(audio_path)

    else:
        return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

