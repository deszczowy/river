import uuid

def new_id():
    return str(uuid.uuid4().hex)