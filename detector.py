import re

patterns = {

    "Email":
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

    "Phone":
    r"\b[6-9]\d{9}\b",

    "PAN":
    r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",

    "Aadhaar":
    r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "Credit Card":
    r"\b(?:\d[ -]*?){13,16}\b",

    "Password":
    r"(?i)(password\s*[:=]\s*\S+)",

    "API Key":
    r"(?i)(api[_-]?key\s*[:=]\s*\S+)",

    "Employee ID":
    r"\bEMP\d{3,6}\b",

    "Bank Account":
    r"\b\d{9,18}\b"

}


def detect_sensitive_data(text):

    results = {}

    total = 0

    for key, pattern in patterns.items():

        matches = re.findall(pattern, text)

        if matches:
            results[key] = matches
            total += len(matches)

    return results, total


def classify_risk(total):

    if total <= 2:
        return "Low Risk"

    elif total <= 7:
        return "Medium Risk"

    return "High Risk"