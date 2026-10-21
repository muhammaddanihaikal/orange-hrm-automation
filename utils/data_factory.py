import random
import uuid


def generate_username(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def generate_employee_data():
    """Generate data employee dengan ID 5 angka dan nama unik."""
    random_id = str(random.randint(10000, 99999))
    random_num = random.randint(100, 999)

    first_name = "dani"
    middle_name = "haikal"
    last_name = f"automation{random_num}"
    username = generate_username("automation")
    password = "JagungManis_9192"
    confirm_password = "JagungManis_9192"

    return {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "employee_id": random_id,
        "username": username,
        "password": password,
        "confirm_password": confirm_password,
    }
