import bcrypt

def generate_pass(user_password):
    password_string = str(user_password)
    password_raw = password_string.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_raw, salt)
    return hashed

def decode_pass(inserted_user_password, database_password):
    result = bcrypt.checkpw(inserted_user_password.encode(), database_password.encode())
    return result