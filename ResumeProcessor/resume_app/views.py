



import io
import tempfile  # Add this import statement
import fitz  # PyMuPDF to extract text from PDF
import os  # For file removal after processing
from django.core.files.storage import default_storage
from django.conf import settings
from django.shortcuts import render
from .forms import ResumeForm
from .models import Candidate
import re

from django.contrib import messages  # Import the messages framework
from django.contrib import messages  # Import the messages framework

def upload_resume(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        resume = request.FILES['resume']
        
        # Process the resume (extract name, email, phone, etc.)
        extracted_data = extract_data_from_pdf(resume)
        
        # Save extracted data to the database
        if extracted_data:
            candidate = Candidate(
                name=extracted_data['name'],
                email=extracted_data['email'],
                phone_number=extracted_data['phone_number'],
                resume=resume  # Ensure the resume is saved properly in the FileField
            )
            candidate.save()

            # Add a success message
            messages.success(request, 'Resume uploaded and data saved successfully!')
        else:
            # Add a failure message if data extraction fails
            messages.error(request, 'Failed to extract data from the resume.')

    return render(request, 'resume_app/upload_resume.html')
def extract_data_from_pdf(pdf_file):
    # Convert the in-memory file to a file-like object using io.BytesIO
    file_data = io.BytesIO(pdf_file.read())

    # Create a temporary file to save the PDF content
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(file_data.read())
        tmp_file_path = tmp_file.name  # Get the temporary file path

    # Open the temporary file using fitz (PyMuPDF)
    doc = fitz.open(tmp_file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Extracting name, email, and phone number from the text
    name = extract_name(text)
    email = extract_email(text)
    phone_number = extract_phone_number(text)

    # Check if the extracted data is valid
    if name and email and phone_number:
        os.remove(tmp_file_path)  # Clean up temporary file
        return {'name': name, 'email': email, 'phone_number': phone_number}
    
    os.remove(tmp_file_path)  # Clean up temporary file
    return None

import re

def extract_name(text):
    # Regular expression to match an email and phone number
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d{1,2}?)?(\(?\d{3}\)?|\d{3})[\s-]?\d{3}[\s-]?\d{4}'
    
    # Find the first occurrence of email or phone number in the text
    email_match = re.search(email_pattern, text)
    phone_match = re.search(phone_pattern, text)
    
    # If both email and phone number exist, find the earliest one in the text
    if email_match and phone_match:
        first_match_pos = min(email_match.start(), phone_match.start())
    elif email_match:
        first_match_pos = email_match.start()
    elif phone_match:
        first_match_pos = phone_match.start()
    else:
        # If neither email nor phone number is found, return the whole text
        return text.strip()

    # Extract everything before the first email or phone number as the name
    name = text[:first_match_pos].strip()
    return name
def extract_email(text):
    # Simple regex for email
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    if email_match:
        return email_match.group(0)
    return "Unknown Email"

def extract_phone_number(text):
    # Simple regex for phone numbers (adjust based on format you expect)
    phone_match = re.search(r'(\+?\d{1,2}?)?(\(?\d{3}\)?|\d{3})[\s-]?\d{3}[\s-]?\d{4}', text)
    if phone_match:
        return phone_match.group(0)
    return "Unknown Phone Number"
