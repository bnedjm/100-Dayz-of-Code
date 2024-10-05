import os
import PyPDF2
import PyPDF2.errors
from gtts import gTTS
import concurrent.futures
from pydub import AudioSegment

def extract_text_from_pdf(pdf_file_path: str) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_file_path (str): The path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF file, or an error message if extraction fails.
    """
    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            if len(pdf_reader.pages) == 0:
                raise ValueError("The PDF file contains no pages.")
            
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                extracted_text = page.extract_text()
                
                if extracted_text:
                    text += extracted_text
                else:
                    print(f"Warning: No text found on page {page_num + 1}")
            
            return text
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file '{pdf_file_path}' was not found.")
    
    except PermissionError:
        raise PermissionError(f"Error: Permission denied for file '{pdf_file_path}'.")
    
    except PyPDF2.errors.PdfReadError as e:
        raise Exception(f"Error reading PDF file: {e}")

def convert_text_to_speech(text: str, language: str = 'en', output_audio_file_path: str = 'output.mp3') -> bool:
    """
    Convert text to speech using Google Text-to-Speech and save as MP3.
    
    Args:
        text (str): The text to convert to speech.
        language (str): The language of the text (default is English: 'en').
        output_audio_file_path (str): The path to save the output MP3 file.
        
    Returns:
        bool: True if successful, Raises an Exception if an error occurred.
    """
    try:
        if not text.strip():
            raise ValueError("No text provided for speech conversion.")
        
        chunks = chunk_text(text)
        audio_files = []
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i, chunk in enumerate(chunks):
                chunk_file = f"temp_chunk_{i}.mp3"
                futures.append(executor.submit(convert_text_to_speech_chunk, chunk, language, chunk_file))
                audio_files.append(chunk_file)

            concurrent.futures.wait(futures)
        combine_audio_files(audio_files, output_audio_file_path)

        for file in audio_files:
            os.remove(file)
            
        return True
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def chunk_text(text, chunk_size=1000):
    """Divide text into chunks of the specified size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def convert_text_to_speech_chunk(text, language, output_file):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)

def combine_audio_files(audio_files, output_audio_file_path):
    from pydub import AudioSegment

    combined = AudioSegment.empty()
    for file in audio_files:
        combined += AudioSegment.from_mp3(file)

    combined.export(output_audio_file_path, format="mp3")

def save_audio_file(temp_file_path: str, output_file_path: str):
    """
    Save the audio file from a temporary path to the specified output path.
    """
    audio = AudioSegment.from_mp3(temp_file_path)
    audio.export(output_file_path, format="mp3")
