import json

CODES_FILE = "codes.json"

def load_codes():
    with open(CODES_FILE, "r") as f:
        return json.load(f)

def save_codes(codes):
    with open(CODES_FILE, "w") as f:
        json.dump(codes, f)

def is_valid_code(code):
    codes = load_codes()
    return code in codes and codes[code] < 20

def mark_code_used(code):
    codes = load_codes()
    if code in codes:
        codes[code] += 1
        save_codes(codes)
