from flask import Flask, request, jsonify
import openai

app = Flask(_name_)

openai.api_key = "YOUR_API_KEY_HERE"

@app.route("/check", methods=["POST"])
def check_symptoms():
    data = request.json
    symptoms = data.get("symptoms", "")

    prompt = f"""
    User symptoms: {symptoms}

    Based on these symptoms, suggest possible medical conditions and next steps.
    Include a disclaimer that this is for educational purposes only and not a medical diagnosis.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"result": response["choices"][0]["message"]["content"]})

if _name_ == "_main_":
    app.run(debug=True)