from email_validator import validate_email, EmailNotValidError

def check_email(e):
    ''' check if an email is valid or not

        Parameters
        ----------
        e : string

        Return
        ------
        True : if email is valid
        False : if email is not valid
    '''
    try:
        v = validate_email(e)
        return True
    except EmailNotValidError as e:
        return False