from email_validator import validate_email, EmailNotValidError

def check_email(e):
    try:
        v = validate_email(e)
        return True
    except EmailNotValidError as e:
        return False