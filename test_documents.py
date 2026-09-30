from utils.document_generator import (
    create_docx,
    create_pdf,
    create_txt,
)


sample_document = """
**RENTAL AGREEMENT**

This Rental Agreement is made on 27 September 2026.

### 1. PARTIES

The agreement is between the Landlord and Tenant.

### 2. MONTHLY RENT

The monthly rent shall be ₹15,000.

### 3. SECURITY DEPOSIT

The security deposit shall be ₹50,000.

### 4. TERMS AND CONDITIONS

* Rent shall be paid on or before the agreed date.
* The tenant shall maintain the property.
* Either party may terminate the agreement with the required notice.

### 5. TERMINATION

Either party may terminate this agreement subject to the agreed terms.

DISCLAIMER

This document is an AI-generated draft for informational and drafting purposes only. It is not legal advice and should be reviewed by a qualified legal professional before use.

LANDLORD SIGNATURE: ______________________

TENANT SIGNATURE: ______________________
"""


docx_file = create_docx(
    sample_document,
    "test_rental_agreement.docx"
)

pdf_file = create_pdf(
    sample_document,
    "test_rental_agreement.pdf"
)

txt_file = create_txt(
    sample_document,
    "test_rental_agreement.txt"
)


print()
print("=" * 60)
print("DOCUMENT GENERATION TEST")
print("=" * 60)

print("DOCX:")
print(docx_file)

print()

print("PDF:")
print(pdf_file)

print()

print("TXT:")
print(txt_file)

print()

print("SUCCESS")
print("=" * 60)