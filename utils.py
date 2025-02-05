import re

def to_snake_case(col_name: str) -> str:
    col_name = re.sub(r"[\s\-]", "_", col_name)  # Replace spaces and hyphens with underscores
    col_name = re.sub(r"([a-z])([A-Z])", r"\1_\2", col_name)  # Insert underscore before capital letters
    return col_name.lower()