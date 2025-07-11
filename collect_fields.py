import json

def load_swagger(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def get_required_fields(swagger, path, method):
    method = method.lower()
    endpoint = swagger["paths"].get(path, {}).get(method, {})
    schema = endpoint.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})
    required_fields = schema.get("required", [])
    properties = schema.get("properties", {})
    return [(field, properties[field].get("type", "string")) for field in required_fields]

def collect_user_input(fields):
    user_data = {}
    for field, ftype in fields:
        value = input(f"📝 Enter value for '{field}' ({ftype}): ")
        user_data[field] = value
    return user_data

if __name__ == "__main__":
    # مرحله قبلی رو فرض می‌گیریم: user گفت "assign a task" → endpoint انتخاب شد
    endpoint_path = "/tasks"
    http_method = "POST"

    swagger = load_swagger("swagger_specs/industrial_platform.json")
    fields = get_required_fields(swagger, endpoint_path, http_method)
    
    print(f"\n📌 Required fields for {http_method} {endpoint_path}:")
    for field, ftype in fields:
        print(f" - {field} ({ftype})")

    user_input = collect_user_input(fields)

    print("\n✅ Final data preview (to be sent):")
    print(json.dumps(user_input, indent=4))
