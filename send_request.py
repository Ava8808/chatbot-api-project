# send_request.py
import requests
import json

def send_post_request(url, data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(data))

        print("\n📨 Sending request to:", url)
        print("📦 Payload:", json.dumps(data, indent=2))
        print("\n📬 Response:")
        print(f"🔢 Status code: {response.status_code}")
        print(f"🧾 Body: {response.text}")
    except Exception as e:
        print("❌ Error sending request:", str(e))

# فقط برای تست مستقیم
if __name__ == "__main__":
    sample_url = "https://httpbin.org/post"  # آدرس تستی رایگان
    sample_data = {
        "staff_id": "123",
        "task_description": "Fix the grinder",
        "due_date": "2025-07-15"
    }
    send_post_request(sample_url, sample_data)
