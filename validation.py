import re

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@university\.com$"
PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

def validate_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None

def validate_password(password):
    return re.fullmatch(PASSWORD_PATTERN, password) is not None