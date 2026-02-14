import os
import json

def parse_env_value(val):
    if key_name == "UniqueID":
        return str(val)

    val_lower = val.lower()
    if val_lower == "true":
        return True
    elif val_lower == "false":
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        pass
    return val

def replace_with_env(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                env_key = value[2:-1]
                if env_key in os.environ:
                    obj[key] = parse_env_value(os.environ[env_key])
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

print(f"Generated {output_file} from {input_file} with environment overrides. Yay?")

