"""
PDF Reader Module
Extracts text and contact information from PDF files
"""

import PyPDF2
import re

class PDFReader:
    """Extract text and contact information from PDF files"""
    
    @staticmethod
    def extract_text(pdf_path):
        """
        Extract all text from PDF file
        
        Args:
            pdf_path (str): Path to PDF file
            
        Returns:
            str: Extracted text from all pages
        """
        try:
            text = []
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Extract text from each page
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    text.append(page_text)
            
            # Join all pages
            full_text = '\n'.join(text)
            
            # Clean the text
            cleaned_text = PDFReader.clean_text(full_text)
            
            return cleaned_text
        
        except Exception as e:
            print(f"Error reading PDF: {str(e)}")
            return ""
    
    @staticmethod
    def clean_text(text):
        """
        Clean extracted text by removing special characters and extra whitespace
        
        Args:
            text (str): Raw extracted text
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove special characters but keep important ones
        # Keep alphanumeric, spaces, dots, commas, hyphens, plus signs, and @
        text = re.sub(r'[^\w\s@.\-+,#:]', '', text)
        
        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    @staticmethod
    def extract_contact_info(text):
        """
        Extract email and phone number from text
        
        Args:
            text (str): Text to search for contact information
            
        Returns:
            dict: Dictionary with email and phone
        """
        contact_info = {
            'email': None,
            'phone': None
        }
        
        try:
            # Extract email
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            email_match = re.search(email_pattern, text)
            if email_match:
                contact_info['email'] = email_match.group(0)
            
            # Extract phone number (basic patterns)
            phone_patterns = [
                r'\+1\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}',  # +1 (XXX) XXX-XXXX
                r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}',         # (XXX) XXX-XXXX
                r'\+\d{1,3}\s?\d{4,14}',                         # International format
            ]
            
            for pattern in phone_patterns:
                phone_match = re.search(pattern, text)
                if phone_match:
                    contact_info['phone'] = phone_match.group(0)
                    break
        
        except Exception as e:
            print(f"Error extracting contact info: {str(e)}")
        
        return contact_info


def extract_pdf_text(pdf_path):
    """
    Wrapper function to extract text from PDF
    
    Args:
        pdf_path (str): Path to PDF file
        
    Returns:
        str: Extracted and cleaned text
    """
    return PDFReader.extract_text(pdf_path)


def get_contact_info(text):
    """
    Wrapper function to extract contact information
    
    Args:
        text (str): Text to search
        
    Returns:
        dict: Contact information (email, phone)
    """
    return PDFReader.extract_contact_info(text)
