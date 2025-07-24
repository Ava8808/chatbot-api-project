# modules/extract_endpoints.py

def extract_endpoints(swagger_data):
    endpoints = []
    paths = swagger_data.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            summary = details.get("summary", "")
            description = details.get("description", "")
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": summary,
                "description": description
            })
    return endpoints





#############################
# import json

# def extract_endpoints(filepath):
#     with open(filepath, "r", encoding="utf-8") as f:
#         swagger_data = json.load(f)

#     paths = swagger_data.get("paths", {})
#     if not paths:
#         print("No endpoints found in Swagger file.")
#         return

#     print("✅ Extracted Endpoints:\n")

#     for endpoint, methods in paths.items():
#         print(f"📌 Endpoint: {endpoint}")
#         for method, details in methods.items():
#             print(f"  └ Method: {method.upper()}")
#             print(f"     Summary: {details.get('summary')}")
#             print(f"     Description: {details.get('description')}")
#             request_body = details.get("requestBody", {})
#             if request_body:
#                 content = request_body.get("content", {})
#                 json_schema = content.get("application/json", {}).get("schema", {})
#                 required_fields = json_schema.get("required", [])
#                 props = json_schema.get("properties", {})
#                 print("     Required fields:")
#                 for field in required_fields:
#                     field_info = props.get(field, {})
#                     field_type = field_info.get("type", "unknown")
#                     print(f"       - {field}: {field_type}")
#             else:
#                 print("     No request body required.")
#         print("")

# if __name__ == "__main__":
#     extract_endpoints("swagger_specs/industrial_platform.json")





# import json

# def extract_endpoints_from_swagger(filepath):
#     with open(filepath, "r") as f:
#         swagger_data = json.load(f)

#     paths = swagger_data.get("paths", {})
#     for endpoint, methods in paths.items():
#         print(f"\nEndpoint: {endpoint}")
#         for method, details in methods.items():
#             print(f"  Method: {method.upper()}")
#             print(f"  Summary: {details.get('summary')}")
#             request_body = details.get("requestBody", {})
#             if request_body:
#                 content = request_body.get("content", {})
#                 app_json = content.get("application/json", {})
#                 schema = app_json.get("schema", {})
#                 required = schema.get("required", [])
#                 properties = schema.get("properties", {})
#                 print("  Required parameters:")
#                 for name in required:
#                     field = properties.get(name, {})
#                     print(f"    - {name} ({field.get('type')})")
#             else:
#                 print("  No request body required.")

# # استفاده:
#     # print("Swagger data loaded successfully.")
#     # print("Available paths:", list(paths.keys()))

# if __name__ == "__main__":
#     extract_endpoints_from_swagger("swagger_specs/industrial_platform.json")
