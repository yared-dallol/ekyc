from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Base URL
BASE_URL = "0.0.0.0"

# Temporary storage for uploaded files
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Helper function to save uploaded files
def save_file(file, user_id):
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{user_id}_{filename}")
        file.save(file_path)
        return file_path
    return None

# 1. SendFace
@app.route("/sendFace", methods=["POST"])
@app.route("/sendFace", methods=["POST"])
def send_face():
    user_id = 12345  # Example user ID
    files = request.files.getlist("face1") + request.files.getlist("face2") + \
            request.files.getlist("face3") + request.files.getlist("face4") + \
            request.files.getlist("face5")
    for file in files:
        save_file(file, user_id)
    return jsonify({
        "user_id": user_id,
        "status_code": "1000",
        "status_message": "success"
    })

# 2. ScanDocument
@app.route("/scanDocument", methods=["POST"])
def scan_document():
    user_id = request.form.get("user_id")
    id_front = request.files.get("id_front")
    id_back = request.files.get("id_back")
    save_file(id_front, user_id)
    save_file(id_back, user_id)
    return jsonify({
        "basic_info": {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "sex": "Male",
            "nationality": "US",
            "dob": "1990-01-01",
            "doe": "2030-01-01"
        },
        "status_code": "1000",
        "status_message": "success"
    })

# 3. getByFCN
@app.route("/getByFCN", methods=["POST"])
def get_by_fcn():
    user_id = request.form.get("user_id")
    fcn_number = request.files.get("fcn_number")
    save_file(fcn_number, user_id)
    return jsonify({
        "basic_info": {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "sex": "Male",
            "nationality": "US",
            "dob": "1990-01-01",
            "doe": "2030-01-01"
        },
        "status_code": "1000",
        "status_message": "success"
    })

# 4. registerUser
@app.route("/registerUser", methods=["POST"])
def register_user():
    data = request.get_json()
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })


# 5. findNumber
@app.route("/findNumber", methods=["POST"])
def find_number():
    data = request.get_json()
    return jsonify({
        "msisdn_list": {
            "msisdn1": "1234567890",
            "msisdn2": "0987654321",
            "msisdn3": "1122334455",
            "msisdn4": "5566778899",
            "msisdn5": "9988776655"
        },
        "status_code": "1000",
        "status_message": "success"
    })

# 6. getUsersMSISDN
@app.route("/getUsersMSISDN", methods=["POST"])
def get_users_msisdn():
    data = request.get_json()
    return jsonify({
        "msisdn_list": {
            "msisdn1": "1234567890",
            "msisdn2": "0987654321",
            "msisdn3": "1122334455",
            "msisdn4": "5566778899",
            "msisdn5": "9988776655"
        },
        "status_code": "1000",
        "status_message": "success"
    })

# 7. assignMSISDN
@app.route("/assignMSISDN", methods=["POST"])
def assign_msisdn():
    data = request.get_json()
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })
# 8. validateFace API
@app.route("/validateFace", methods=["POST"])
def validate_face():
    face = request.files.get("face")
    save_file(face, "validate_face")
    return jsonify({
        "basic_info": {
            "similarity_score": 95.5,
            "distance": 0.045,
            "match": True,
            "time_spent": "2.3s"
        },
        "status_code": "1000",
        "status_message": "success"
    })


# 9. suspendMSISDN
@app.route("/suspendMSISDN", methods=["POST"])
def suspend_msisdn():
    data = request.get_json()
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })

# 10. validateFaceUserId
@app.route("/validateFaceUserId", methods=["POST"])
def validate_face_user_id():
    user_id = request.form.get("user_id")
    face = request.files.get("face")
    save_file(face, user_id)
    return jsonify({
        "basic_info": {
            "similarity_score": 95.5,
            "distance": 0.045,
            "match": True,
            "time_spent": "2.3s"
        },
        "status_code": "1000",
        "status_message": "success"
    })

# 11. validateBarcode
@app.route("/validateBarcode", methods=["POST"])
def validate_barcode():
    data = request.get_json()
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })


# 12. getOTP API
@app.route("/getOTP", methods=["POST"])
def get_otp():
    data = request.get_json()
    msisdn = data.get("msisdn")
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })

# 13. validateOTP API
@app.route("/validateOTP", methods=["POST"])
def validate_otp():
    data = request.get_json()
    msisdn = data.get("msisdn")
    otp_number = data.get("OTP_number")
    return jsonify({
        "status_code": "1000",
        "status_message": "success"
    })
	

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
