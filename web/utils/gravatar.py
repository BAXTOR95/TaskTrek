from hashlib import md5

def gravatar_url(email, size=100, rating='g', default='retro', force_default=False):
    """Generates a gravatar URL for a given email.
    Args:
        email (str): The user's email address.
        size (int): Size of the gravatar image.
        rating (str): Rating of the gravatar image.
        default (str): Default gravatar image style.
        force_default (bool): Whether to force the default image or not.
    Returns:
        str: The gravatar URL.
    """
    hash_value = md5(email.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_value}?s={size}&d={default}&r={rating}&f={force_default}"
