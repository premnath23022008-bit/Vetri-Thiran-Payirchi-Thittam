from ai_core.gemini_generator import generate_legal_document


document = generate_legal_document(
    document_type="Rental Agreement",
    user_details="""
Landlord: Arun Kumar
Tenant: Priya
Property: Chennai, Tamil Nadu
Monthly Rent: ₹15,000
Security Deposit: ₹50,000
Agreement Date: 27 September 2026
""",
    additional_requirements="""
Include rent payment terms, security deposit,
maintenance responsibilities, termination terms,
and signature sections.
"""
)

print("\n" + "=" * 70)
print("GENERATED LEGAL DOCUMENT")
print("=" * 70)
print(document)
print("=" * 70)