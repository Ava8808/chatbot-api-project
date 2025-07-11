from difflib import SequenceMatcher
import json

def extract_endpoints(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        swagger = json.load(f)

    endpoints = []
    for path, methods in swagger.get("paths", {}).items():
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

def find_best_match(user_input, endpoints):
    def similarity(a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    scored = []
    for ep in endpoints:
        score = max(
            similarity(user_input, ep["summary"]),
            similarity(user_input, ep["description"])
        )
        scored.append((score, ep))

    best_match = max(scored, key=lambda x: x[0])
    return best_match

if __name__ == "__main__":
    user_input = input("💬 User says: ")

    endpoints = extract_endpoints("swagger_specs/industrial_platform.json")
    score, match = find_best_match(user_input, endpoints)

    print("\n🔍 Best Match:")
    print(f"📌 Endpoint: {match['path']}")
    print(f"📥 Method: {match['method']}")
    print(f"📄 Summary: {match['summary']}")
    print(f"📝 Description: {match['description']}")
    print(f"✅ Similarity Score: {score:.2f}")

