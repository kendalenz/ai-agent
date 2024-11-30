import re
import json
from pydantic import BaseModel, ValidationError

def extract_json(text_response):
    """
    Extracts JSON objects from a given text response.
    """
    pattern = r'\{.*?\}'
    matches = re.finditer(pattern, text_response, re.DOTALL)
    json_objects = []

    for match in matches:
        json_str = match.group(0)
        try:
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            # Log malformed JSON for debugging
            print(f"Invalid JSON found: {json_str}")
            continue

    return json_objects if json_objects else None

# Other functions remain unchanged
