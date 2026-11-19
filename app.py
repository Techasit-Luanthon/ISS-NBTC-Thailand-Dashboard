from flask import Flask, jsonify, render_template
import requests

app = Flask(__Techasit Luanthon__)
ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"
NBTC_API = "https://datacatalog.nbtc.go.th/api/3/action"
DEMO_MEMBER = {
    "id": "DEMO-NBTC-0001",
    "name": "Fictional NBTC Member",
    "role": "Demo member",
}


def request_nbtc_action(action, **params):
    response = requests.get(f"{NBTC_API}/{action}", params=params, timeout=8)
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("NBTC API returned an unexpected response.")
    return payload, response.status_code


def nbtc_api_response(action, **params):
    try:
        payload, status_code = request_nbtc_action(action, **params)
    except (requests.RequestException, ValueError):
        return jsonify(success=False, error="NBTC data is temporarily unavailable."), 502
    return jsonify(payload), status_code


@app.get("/api/nbtc/packages")
def nbtc_packages():
    return nbtc_api_response("package_list")


@app.get("/api/nbtc/packages/<package_id>")
def nbtc_package(package_id):
    return nbtc_api_response("package_show", id=package_id)


@app.get("/healthz")
def health_check():
    return jsonify(status="ok")


@app.get("/")
def home():
    iss = None
    error = None
    nbtc_packages = None
    nbtc_packages_error = None
    nbtc_dataset = None
    nbtc_dataset_error = None
    try:
        response = requests.get(ISS_API, timeout=8)
        response.raise_for_status()
        data = response.json()
        iss = {
            "latitude": round(float(data["latitude"]), 4),
            "longitude": round(float(data["longitude"]), 4),
            "altitude_km": round(float(data["altitude"]), 2),
            "velocity_kmh": round(float(data["velocity"]), 2),
            "timestamp": data.get("timestamp"),
        }
    except (requests.RequestException, KeyError, TypeError, ValueError):
        error = "ISS data is temporarily unavailable. Please refresh later."

    try:
        payload, status_code = request_nbtc_action("package_list")
        if status_code >= 400 or not payload.get("success"):
            nbtc_packages_error = "NBTC dataset list is temporarily unavailable."
        elif isinstance(payload.get("result"), list):
            nbtc_packages = payload["result"]
        else:
            nbtc_packages_error = "NBTC returned an unexpected dataset list."
    except (requests.RequestException, ValueError):
        nbtc_packages_error = "NBTC dataset list is temporarily unavailable."

    try:
        payload, status_code = request_nbtc_action("package_show", id="iot_numbers")
        if status_code == 404:
            nbtc_dataset_error = "Dataset 'iot_numbers' was not found in the NBTC catalog."
        elif status_code >= 400 or not payload.get("success"):
            nbtc_dataset_error = "NBTC dataset details are temporarily unavailable."
        elif isinstance(payload.get("result"), dict):
            nbtc_dataset = payload["result"]
        else:
            nbtc_dataset_error = "NBTC returned unexpected dataset details."
    except (requests.RequestException, ValueError):
        nbtc_dataset_error = "NBTC dataset details are temporarily unavailable."

    return render_template(
        "index.html",
        iss=iss,
        error=error,
        nbtc_packages=nbtc_packages,
        nbtc_packages_error=nbtc_packages_error,
        nbtc_dataset=nbtc_dataset,
        nbtc_dataset_error=nbtc_dataset_error,
        demo_member=DEMO_MEMBER,
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
