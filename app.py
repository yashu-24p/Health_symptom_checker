from flask import Flask, render_template, request

app = Flask(__name__)

# Symptom -> Probable conditions + next steps
disease_data = {
    "headache": {
        "conditions": ["Tension headache", "Migraine", "Dehydration"],
        "steps": ["Rest", "Drink water", "OTC pain relief", "See a doctor if persistent"]
    },
    "fever": {
        "conditions": ["Flu", "Infection", "COVID-19"],
        "steps": ["Stay hydrated", "Monitor temperature", "Take paracetamol if needed", "Consult doctor if high fever"]
    },
    "cough": {
        "conditions": ["Common cold", "Bronchitis", "COVID-19"],
        "steps": ["Drink warm fluids", "Use cough syrup if necessary", "See doctor if severe"]
    },
    "fatigue": {
        "conditions": ["Anemia", "Hypothyroidism", "Sleep deprivation"],
        "steps": ["Get enough sleep", "Eat iron-rich foods", "Consult doctor for blood tests"]
    },
    "nausea": {
        "conditions": ["Food poisoning", "Stomach flu", "Pregnancy"],
        "steps": ["Drink fluids", "Rest", "Eat light meals", "See doctor if persistent"]
    }
    # Add more symptoms here
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        symptom = request.form.get("symptom").strip().lower()
        if symptom in disease_data:
            cond = ", ".join(disease_data[symptom]["conditions"])
            steps = ", ".join(disease_data[symptom]["steps"])
            result = f"Probable conditions: {cond} | Recommended next steps: {steps}"
        else:
            result = "Symptom not recognized. Please try another symptom."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


