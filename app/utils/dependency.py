current_user = None

def set_current_user(person):
    global current_user
    current_user = person

def get_current_user():
    return current_user

