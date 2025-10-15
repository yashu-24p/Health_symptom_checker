from flask import Flask, render_template, request

app = Flask(__name__)

# Symptom dictionary (50+ common symptoms)
symptom_dict = {
    "headache": {
        "conditions": "Tension headache, Migraine, Dehydration",
        "steps": "Rest, Drink water, OTC pain relief, See a doctor if persistent"
    },
    "fever": {
        "conditions": "Flu, Infection, COVID-19",
        "steps": "Stay hydrated, Monitor temperature, Take paracetamol if needed, Consult a doctor if high fever"
    },
    "cough": {
        "conditions": "Common cold, Bronchitis, COVID-19",
        "steps": "Drink warm fluids, Use cough syrup if necessary, See a doctor if severe"
    },
    "motion": {
        "conditions": "Motion sickness, Inner ear disturbance",
        "steps": "Sit still, Focus on the horizon, Take anti-nausea medicine, Avoid reading while moving"
    },
    "fatigue": {
        "conditions": "Anemia, Hypothyroidism, Sleep deprivation",
        "steps": "Get enough sleep, Eat iron-rich foods, Consult a doctor for blood tests"
    },
    "nausea": {
        "conditions": "Food poisoning, Stomach flu, Pregnancy",
        "steps": "Drink fluids, Rest, Eat light meals, See a doctor if persistent"
    },
    "dizziness": {
        "conditions": "Low blood pressure, Dehydration, Inner ear issues",
        "steps": "Sit or lie down, Drink water, Avoid sudden movements, See a doctor if frequent"
    },
    "shortness of breath": {
        "conditions": "Asthma, COVID-19, Heart conditions",
        "steps": "Rest, Seek medical attention immediately if severe, Avoid exertion"
    },
    "chest pain": {
        "conditions": "Heart attack, Angina, Muscle strain",
        "steps": "Call emergency services if severe, Rest, Consult a doctor urgently"
    },
    "sore throat": {
        "conditions": "Common cold, Strep throat, Flu",
        "steps": "Drink warm fluids, Gargle with salt water, Take pain relief, See a doctor if severe"
    },
    "runny nose": {
        "conditions": "Common cold, Allergies",
        "steps": "Stay hydrated, Use nasal sprays if needed, Avoid allergens"
    },
    "vomiting": {
        "conditions": "Food poisoning, Stomach flu, Migraine",
        "steps": "Drink fluids, Rest, Eat light foods, See a doctor if persistent"
    },
    "diarrhea": {
        "conditions": "Food poisoning, Infection, Irritable bowel syndrome",
        "steps": "Drink fluids, Eat bland foods, See a doctor if severe or prolonged"
    },
    "constipation": {
        "conditions": "Low fiber diet, Dehydration, IBS",
        "steps": "Eat fiber-rich foods, Drink water, Exercise, See a doctor if chronic"
    },
    "back pain": {
        "conditions": "Muscle strain, Herniated disc, Poor posture",
        "steps": "Rest, Stretching exercises, Pain relief, See a doctor if severe"
    },
    "joint pain": {
        "conditions": "Arthritis, Injury, Gout",
        "steps": "Rest, Apply ice or heat, Pain relief, See a doctor if persistent"
    },
    "blurred vision": {
        "conditions": "Eye strain, Diabetes, Glaucoma",
        "steps": "Rest eyes, Consult an eye specialist, Check blood sugar if diabetic"
    },
    "rash": {
        "conditions": "Allergic reaction, Infection, Skin condition",
        "steps": "Avoid irritants, Use soothing creams, See a doctor if severe"
    },
    "itching": {
        "conditions": "Allergy, Dry skin, Infection",
        "steps": "Avoid scratching, Moisturize, Use anti-itch creams, See a doctor if persistent"
    },
    "chills": {
        "conditions": "Flu, Infection, Hypothermia",
        "steps": "Keep warm, Rest, Drink fluids, See a doctor if severe"
    },
    "sweating": {
        "conditions": "Fever, Anxiety, Hyperhidrosis",
        "steps": "Stay hydrated, Rest, Consult doctor if excessive"
    },
    "loss of appetite": {
        "conditions": "Flu, Infection, Depression",
        "steps": "Eat light, Nutritious meals, See doctor if prolonged"
    },
    "weight loss": {
        "conditions": "Thyroid issues, Diabetes, Cancer",
        "steps": "Monitor diet, Consult a doctor for tests"
    },
    "weight gain": {
        "conditions": "Diet imbalance, Hypothyroidism, Fluid retention",
        "steps": "Check diet, Exercise, Consult a doctor if rapid"
    },
    "anxiety": {
        "conditions": "Stress, Generalized anxiety disorder",
        "steps": "Relaxation techniques, Exercise, Consult mental health professional"
    },
    "depression": {
        "conditions": "Major depressive disorder, Stress",
        "steps": "Seek counseling, Exercise, Consult mental health professional"
    },
    "insomnia": {
        "conditions": "Stress, Sleep disorder",
        "steps": "Maintain sleep hygiene, Relaxation techniques, Consult doctor if chronic"
    },
    "palpitations": {
        "conditions": "Anxiety, Arrhythmia, Thyroid issues",
        "steps": "Relax, Avoid caffeine, Consult doctor if persistent"
    },
    "numbness": {
        "conditions": "Nerve compression, Diabetes, Stroke",
        "steps": "Consult doctor urgently, Monitor other symptoms"
    },
    "tingling": {
        "conditions": "Peripheral neuropathy, Nerve compression",
        "steps": "Avoid pressure on nerves, Consult doctor if persistent"
    },
    "swelling": {
        "conditions": "Injury, Infection, Heart or kidney issues",
        "steps": "Rest, Elevate area, Consult doctor if severe"
    },
    "abdominal pain": {
        "conditions": "Gastritis, Appendicitis, Infection",
        "steps": "Rest, Avoid heavy meals, See doctor if severe"
    },
    "heartburn": {
        "conditions": "Acid reflux, Ulcer, Indigestion",
        "steps": "Avoid spicy foods, Eat small meals, Consult doctor if persistent"
    },
    "frequent urination": {
        "conditions": "Diabetes, Urinary tract infection",
        "steps": "Drink fluids, Consult doctor for tests"
    },
    "thirst": {
        "conditions": "Dehydration, Diabetes",
        "steps": "Drink water, Monitor for other symptoms, Consult doctor if persistent"
    },
    "dry mouth": {
        "conditions": "Dehydration, Medication side effect",
        "steps": "Drink water, Consult doctor if persistent"
    },
    "hair loss": {
        "conditions": "Stress, Thyroid issues, Nutritional deficiency",
        "steps": "Eat nutritious foods, Consult dermatologist"
    },
    "brittle nails": {
        "conditions": "Nutritional deficiency, Thyroid issues",
        "steps": "Eat nutritious foods, Consult doctor if persistent"
    },
    "joint swelling": {
        "conditions": "Arthritis, Injury",
        "steps": "Rest, Apply ice, Consult doctor if persistent"
    },
    "muscle cramps": {
        "conditions": "Dehydration, Electrolyte imbalance",
        "steps": "Stretch, Drink fluids, Ensure proper nutrition"
    },
    "cold hands/feet": {
        "conditions": "Poor circulation, Hypothyroidism",
        "steps": "Keep warm, Consult doctor if persistent"
    },
    "blurred vision": {
        "conditions": "Diabetes, Eye strain, Hypertension",
        "steps": "Consult ophthalmologist, Monitor blood sugar or BP"
    },
    "earache": {
        "conditions": "Ear infection, Wax build-up",
        "steps": "Consult ENT specialist, Avoid inserting objects"
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        symptom_input = request.form.get("symptom").strip().lower()
        if symptom_input in symptom_dict:
            info = symptom_dict[symptom_input]
            result = f"Probable conditions: {info['conditions']} | Recommended next steps: {info['steps']}"
        else:
            result = "Symptom not recognized. Please try another symptom."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)



