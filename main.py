# main.py

from modules.extract_endpoints import extract_endpoints
from modules.match_intent import find_best_match
from modules.collect_fields import load_swagger, get_required_fields, build_payload
from send_request import send_post_request

SWAGGER_PATH = "swagger_specs/industrial_platform.json"
MOCK_API_URL = "https://httpbin.org/post"

def run_pipeline(user_input, swagger_path=SWAGGER_PATH):
    """
    این تابع pipeline اصلی پروژه است که
    1. تشخیص endpoint
    2. استخراج فیلدهای مورد نیاز
    3. دریافت داده‌های کاربر به صورت پارامتری
    4. پیش‌نمایش و ارسال درخواست
    را انجام می‌دهد.
    """

    swagger = load_swagger(swagger_path)
    endpoints = extract_endpoints(swagger)
    score, matched_endpoint = find_best_match(user_input, endpoints)

    print("\n🔍 Best Match Found:")
    print(f"📌 Endpoint: {matched_endpoint['path']}")
    print(f"📥 Method: {matched_endpoint['method']}")
    print(f"📝 Description: {matched_endpoint['description']}")
    print(f"✅ Similarity Score: {score:.2f}")

    fields = get_required_fields(swagger, matched_endpoint["path"], matched_endpoint["method"])
    print("\n📋 Required Fields:")
    for field, ftype in fields:
        print(f" - {field} ({ftype})")

    # در اینجا فرض می‌کنیم داده‌ها به صورت دیکشنری به تابع داده شده‌اند.
    # برای تست می‌تونیم از ورودی کاربر بگیریم یا مستقیم دیکشنری بسازیم.
    user_values = {}
    print("\n📝 Please provide values for the fields:")
    for field, ftype in fields:
        value = input(f"{field} ({ftype}): ")
        user_values[field] = value

    # ساخت payload نهایی
    payload = build_payload(fields, user_values)

    print("\n🧾 Data Preview (to be sent):")
    print(payload)

    confirm = input("\n🟢 Do you want to send this request? (yes/no): ").strip().lower()
    if confirm in ("yes", "y"):
        response = send_post_request(MOCK_API_URL, payload)
        return response
    else:
        print("❌ Request cancelled.")
        return None

if __name__ == "__main__":
    print("🤖 Swagger Chatbot Pipeline\n")
    user_query = input("💬 What do you want to do? ")
    run_pipeline(user_query)










#################
 # main.py

# from modules.extract_endpoints import extract_endpoints
# from modules.match_intent import find_best_match
# from modules.collect_fields import load_swagger, get_required_fields, collect_user_input
# from send_request import send_post_request
# import json

# SWAGGER_PATH = "swagger_specs/industrial_platform.json"
# MOCK_API_URL = "https://httpbin.org/post"

# def main():
#     print("🤖 Welcome to the Swagger-based Chatbot!\n")

#     # 1. دریافت ورودی کاربر
#     user_input = input("💬 What would you like to do? ").strip()

#     # 2. لود کردن فایل Swagger
#     swagger = load_swagger(SWAGGER_PATH)

#     # 3. تشخیص intent
#     endpoints = extract_endpoints(swagger)
#     score, matched_endpoint = find_best_match(user_input, endpoints)

#     print("\n🔍 Best Match Found:")
#     print(f"📌 Endpoint: {matched_endpoint['path']}")
#     print(f"📥 Method: {matched_endpoint['method']}")
#     print(f"📝 Description: {matched_endpoint['description']}")
#     print(f"✅ Similarity Score: {score:.2f}")

#     # 4. دریافت فیلدهای لازم برای آن endpoint
#     fields = get_required_fields(swagger, matched_endpoint["path"], matched_endpoint["method"])

#     print("\n📋 Required Fields:")
#     for field, ftype in fields:
#         print(f" - {field} ({ftype})")

#     # 5. گرفتن مقادیر هر فیلد از کاربر
#     user_data = collect_user_input(fields)

#     print("\n🧾 Data Preview (to be sent):")
#     print(json.dumps(user_data, indent=4))

#     # 6. گرفتن تأیید برای ارسال
#     confirm = input("\n🟢 Do you want to send this request? (yes/no): ").strip().lower()
#     if confirm in ("yes", "y"):
#         send_post_request(MOCK_API_URL, user_data)
#     else:
#         print("❌ Request cancelled.")

# if __name__ == "__main__":
#     main()
# #