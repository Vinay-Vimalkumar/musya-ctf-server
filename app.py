import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","DELETE","HEAD","OPTIONS","PATCH"])
@app.route("/<path:path>",          methods=["GET","POST","PUT","DELETE","HEAD","OPTIONS","PATCH"])
def catch_all(path):
    print("=== INCOMING REQUEST ===", flush=True)
    print(f"Method:  {request.method}", flush=True)
    print(f"Path:    /{path}", flush=True)
    print(f"Headers: {dict(request.headers)}", flush=True)
    print(f"Args:    {dict(request.args)}", flush=True)
    body = request.get_data(as_text=True)
    print(f"Body:    {body!r}", flush=True)
    print("========================", flush=True)

    # Respond as "Musya" — adjust once we see what the server expects
    return "Musya", 200, {"Content-Type": "text/plain", "X-Courier": "Musya"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
