# main.py

from modules.extract_endpoints import extract_endpoints
from modules.match_intent import find_best_match
from modules.collect_fields import load_swagger, get_required_fields, collect_user_input
from send_request import send_post_request
import json

SWAGGER_PATH = "swagger_specs/industrial_platform.json"
MOCK_API_URL = "https://httpbin.org/post"

def main():
    print("🤖 Welcome to the Swagger-based Chatbot!\n")

    # 1. دریافت ورودی کاربر
    user_input = input("💬 What would you like to do? ").strip()

    # 2. لود کردن فایل Swagger
    swagger = load_swagger(SWAGGER_PATH)

    # 3. تشخیص intent
    endpoints = extract_endpoints(swagger)
    score, matched_endpoint = find_best_match(user_input, endpoints)

    print("\n🔍 Best Match Found:")
    print(f"📌 Endpoint: {matched_endpoint['path']}")
    print(f"📥 Method: {matched_endpoint['method']}")
    print(f"📝 Description: {matched_endpoint['description']}")
    print(f"✅ Similarity Score: {score:.2f}")

    # 4. دریافت فیلدهای لازم برای آن endpoint
    fields = get_required_fields(swagger, matched_endpoint["path"], matched_endpoint["method"])

    print("\n📋 Required Fields:")
    for field, ftype in fields:
        print(f" - {field} ({ftype})")

    # 5. گرفتن مقادیر هر فیلد از کاربر
    user_data = collect_user_input(fields)

    print("\n🧾 Data Preview (to be sent):")
    print(json.dumps(user_data, indent=4))

    # 6. گرفتن تأیید برای ارسال
    confirm = input("\n🟢 Do you want to send this request? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        send_post_request(MOCK_API_URL, user_data)
    else:
        print("❌ Request cancelled.")

if __name__ == "__main__":
    main()
