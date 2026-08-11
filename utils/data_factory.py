import uuid

def generate_username(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"