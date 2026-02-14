import os
import json

def parse_env_value(val):
    try:
        if '.' in val:
            return float(val)
        return int(val)
    except ValueError:
        return val

def replace_with_env(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in os.environ:
                obj[key] = parse_env_value(os.environ[key])
            else:
                obj[key] = replace_with_env(value)
        return obj
    elif isinstance(obj, list):
        return [replace_with_env(item) for item in obj]
    else:
        return obj

input_file = "config.json.template"
output_file = "config.json"

with open(input_file, "r") as f:
    data = json.load(f)

data = replace_with_env(data)

with open(output_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Generated {output_file} from {input_file} with environment overrides.")

print(data)
