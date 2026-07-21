import random
import string


def generate_password(length=12):
    """
    Generates a strong random password.
    Uses uppercase, lowercase, digits and special characters.
    Default length is 12 characters, minimum recommended is 6.
    Returns the generated password as a string.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password