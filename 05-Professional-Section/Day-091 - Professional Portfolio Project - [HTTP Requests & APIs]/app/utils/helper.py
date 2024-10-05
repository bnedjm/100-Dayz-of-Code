ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file_type(filename):
    """Check if the uploaded file is a PDF."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
