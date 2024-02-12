import fitz # pip install pymupdf

def add_keywords_to_pdf_resume(resume_path, keywords, output_path):
    """Add keywords to a PDF resume in white color."""
    # Open the PDF resume
    doc = fitz.open(resume_path)
    
    # Create a new page or select the last one to add keywords
    if doc.page_count == 0:
        page = doc.new_page()
    else:
        page = doc[-1]  # Get the last page of the document
    
    # Define the position to start adding keywords (e.g., bottom of the page)
    x, y = 0, page.rect.height  # Adjust these values as needed
    
    # Add each keyword to the PDF
    for keyword in keywords:
        # Add text in white color
        text = " " + keyword  # Add a leading space for separation
        page.insert_text((x, y), text, color=(1, 1, 1), fontsize=1)  # RGB color in white
    
    # Save the modified document
    doc.save(output_path)
    print(f"Modified PDF resume saved to {output_path}")