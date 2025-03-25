import matplotlib
matplotlib.use('Agg')  # ✅ Use non-GUI backend
import matplotlib.pyplot as plt
import google.generativeai as genai
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify, send_file
from flask_pymongo import PyMongo

app = Flask(__name__)

# ✅ Manually Enter Your Google Gemini API Key Here
genai_api_key = "AIzaSyDqBP7O_2r5KvUm1CZYk6GRKP0MyMak3pg"  # 🔹 Replace with your actual API key

# ✅ Configure Google Gemini AI
genai.configure(api_key=genai_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Connect to Local MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/doctors_db"
mongo = PyMongo(app)

# ✅ Function to generate simple responses
def generate_simple_response(query, patient):
    ai_prompt = f"""
    You are a helpful AI medical assistant. Provide **short and clear** responses based on patient details.

    Patient Details:
    - Name: {patient['name']}
    - Age: {patient['age']}
    - Medical History: {', '.join(patient['medical_history'])}
    - Medications: {', '.join([m['name'] for m in patient['current_medications']])}
    - Health Metrics: Blood Sugar: {patient['health_metrics']['blood_sugar']} mg/dL, 
      Blood Pressure: {patient['health_metrics']['blood_pressure']}, BMI: {patient['health_metrics']['bmi']}, 
      Cholesterol: {patient['health_metrics']['cholesterol']} mg/dL, Heart Rate: {patient['health_metrics']['heart_rate']} bpm.

    User Query: "{query}"
    Provide **brief**, doctor-friendly responses.
    """

    response = model.generate_content(ai_prompt)
    return response.text.strip()

# ✅ Function to fetch patient details
def get_patient_info(query, patient_id):
    patient = mongo.db.patients.find_one({"patient_id": int(patient_id)}, {"_id": 0})

    if not patient:
        return f"No details found for Patient ID {patient_id}."

    return generate_simple_response(query, patient)

# ✅ Function to Generate Graph for Patient Health Metrics
def generate_graph(patient_id):
    patient = mongo.db.patients.find_one({"patient_id": int(patient_id)}, {"_id": 0})

    if not patient:
        return None

    health_metrics = patient["health_metrics"]

    # Data for the graph
    labels = ["Blood Sugar", "Blood Pressure (Systolic)", "BMI", "Cholesterol", "Heart Rate"]
    values = [
        health_metrics["blood_sugar"],
        int(health_metrics["blood_pressure"].split("/")[0]),  # Take systolic value
        health_metrics["bmi"],
        health_metrics["cholesterol"],
        health_metrics["heart_rate"],
    ]

    # Generate graph
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["blue", "red", "green", "purple", "orange"])
    plt.ylabel("Values")
    plt.title(f"Health Metrics for {patient['name']}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the graph as an image
    graph_path = f"static/health_graph_{patient_id}.png"
    plt.savefig(graph_path)
    plt.close()

    return graph_path

# ✅ Route to Serve the Chatbot UI
@app.route("/")
def index():
    return render_template("index.html")

# ✅ API Route for Chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("message", "")
    patient_id = request.json.get("patient_id", "").strip()

    if not patient_id.isdigit():
        return jsonify({"response": "Please enter a valid Patient ID."})

    bot_response = get_patient_info(user_query, patient_id)
    return jsonify({"response": bot_response})

# ✅ Route to Get Patient Health Graph
@app.route("/graph/<patient_id>")
def graph(patient_id):
    graph_path = generate_graph(patient_id)
    if graph_path:
        return send_file(graph_path, mimetype="image/png")
    return "Graph not available for this patient."

if __name__ == "__main__":
    app.run(debug=True)
