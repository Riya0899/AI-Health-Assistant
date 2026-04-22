from dataset import health_data, get_age_group, drug_interactions
import json  # for storing history
import os    # file paths
import plotly.express as px  # graphs
from collections import Counter  # for counting frequency
import re

FILE_NAME = "history.json"  # create file handler


# ---------------- HISTORY ----------------

def load_history():  # it loads the history from file
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_history(history):
    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)


# ---------------- SYMPTOM EXTRACTION ----------------

def extract_symptoms(text):
    text = text.lower()

    symptom_keywords = [
        "fever", "headache", "cough", "sneezing", "runny nose",
        "body pain", "weakness", "fatigue", "stress",
        "joint pain", "stiffness"
    ]

    found = []

    for symptom in symptom_keywords:
        if symptom in text:
            found.append(symptom)

    return list(set(found))


# synonym intelligence
symptom_map = {
    "head pain": "headache",
    "head hurts": "headache",
    "high temperature": "fever",
    "tired": "fatigue",
    "body ache": "body pain",
    "nose running": "runny nose"
}


def normalize_symptoms(symptoms):
    normalized = []
    for s in symptoms:
        s = s.lower()
        if s in symptom_map:
            normalized.append(symptom_map[s])
        else:
            normalized.append(s)
    return normalized


# ---------------- PREDICTION ----------------

def predict_category(user_symptoms, age):
    results = []  # ✅ FIX: initialize results

    # converting age into category
    age_group = get_age_group(age)

    # loop through dataset
    for entry in health_data:

        # age filter
        if entry["age_group"] != age_group:
            continue

        # match symptoms
        matched = [s for s in user_symptoms if s in entry['symptoms']]

        match_count = len(matched)
        total = len(entry["symptoms"])

        # confidence calculation
        confidence = (match_count / total) * 100 if total > 0 else 0

        # filtering weak matches
        if match_count >= 1 and confidence > 20:
            results.append({
                "disease": entry["disease"],
                "confidence": round(confidence, 1),
                "medicines": entry["medicines"],
                "precautions": entry["precautions"],
                "warnings": entry["warnings"],
                "dosage": entry["dosage"],
                "matched": matched  # ✅ IMPORTANT
            })

    # no result case
    if not results:
        return []

    # sort by confidence
    results = sorted(results, key=lambda x: x['confidence'], reverse=True)

    # 👉 return TOP 3
    return results[:3]


# ---------------- DRUG INTERACTION ----------------

# checking medicine combinations
def check_interaction(medicines, other_inputs):
    # other inputs are user habits like alcohol or daily medicine like bp sugar meds
    results = []

    for med in medicines:
        for item in other_inputs:
            pair = (med, item)
            reverse_pair = (item, med)

            if pair in drug_interactions:
                results.append(drug_interactions[pair])

            elif reverse_pair in drug_interactions:
                results.append(drug_interactions[reverse_pair])

    return results


# ---------------- REPORT ----------------

def generate_report(res, interactions, age, symptoms, habits):

    risk = "Low"
    if res['confidence'] < 40:
        risk = "High"
    elif res['confidence'] < 70:
        risk = "Moderate"

    report = f"""
🏥 **AI HEALTH REPORT**

-------------------------------------

👤 **Patient Details**
- Age: {age}
- Symptoms Entered: {", ".join(symptoms)}
- Habits: {", ".join(habits) if habits else "None"}

-------------------------------------

🧠 **Primary Diagnosis**
- Suspected Condition: {res['disease']}
- Confidence: {res['confidence']}%

-------------------------------------

💊 **Treatment**
- Medicines: {", ".join(res['medicines'])}
- Dosage: {res['dosage']}

-------------------------------------

⚠️ **Warnings**
- {res['warnings']}

🛡️ **Precautions**
- {res['precautions']}

-------------------------------------

🚨 **Risk Level**
- {risk}

-------------------------------------

🔬 **AI Explanation**
- Matched Symptoms: {", ".join(res.get('matched', []))}

"""

    return report


# ---------------- HISTORY TRACK ----------------

def track_history(symptoms, result):
    history = load_history()  # load old data

    entry = {
        "symptoms": symptoms,
        "disease": result['disease'],
        "confidence": result.get('confidence', 0)
    }

    history.append(entry)
    save_history(history)


# ---------------- ANALYTICS ----------------

def analyze_trend():
    history = load_history()

    if len(history) < 2:
        return "\n📊 Not enough data to analyze trend."

    last = history[-1]
    previous = history[-2]

    # if same disease continues the condition is worsening
    if last['disease'] == previous['disease']:
        return "\n⚠️ Condition seems consistent. Monitor closely."
    else:
        return "\n✅ Condition changing. May be improving."


def show_history():
    history = load_history()

    text = "\n📊 Health History:\n"
    for h in history:
        text += f"- {h['symptoms']} → {h['disease']}\n"

    return text


# ---------------- GRAPHS ----------------

# 1. symptoms frequency graph -> which symptoms occur most
def plot_symptom_frequency():
    history = load_history()

    if not history:
        return None

    all_symptoms = []
    for entry in history:
        all_symptoms.extend(entry['symptoms'])

    count = Counter(all_symptoms)

    fig = px.bar(
        x=list(count.keys()),
        y=list(count.values()),
        title="Symptom Frequency",
        labels={'x': 'Symptoms', 'y': 'Count'}
    )

    fig.update_layout(template="plotly_dark", title_x=0.3)
    return fig


# confidence graph
def plot_confidence_graph():
    history = load_history()

    if not history:
        return None

    confidence = []
    visits = []

    for i, entry in enumerate(history):
        confidence.append(entry['confidence'])
        visits.append(i + 1)

    fig = px.line(
        x=visits,
        y=confidence,
        markers=True,
        title="Prediction Confidence Trend"
    )

    fig.update_layout(template="plotly_dark")
    return fig


# disease frequency graph
def plot_disease_frequency():
    history = load_history()

    if not history:
        return None

    diseases = [entry['disease'] for entry in history]
    count = Counter(diseases)

    fig = px.pie(
        names=list(count.keys()),
        values=list(count.values()),
        title="Disease Distribution"
    )

    fig.update_layout(template="plotly_dark")
    return fig


# health improvement graph
def plot_health_improvement():
    history = load_history()

    if not history:
        return None

    confidences = [entry['confidence'] for entry in history]
    visits = list(range(1, len(confidences) + 1))

    fig = px.area(
        x=visits,
        y=confidences,
        title="Health Improvement Over Time"
    )

    fig.update_layout(template="plotly_dark")
    return fig


# ---------------- FINAL OUTPUT ----------------

def format_output(result, interactions=None):
    # interactions are safety warnings list
    # result is predicted disease dictionary

    if result is None:
        return "❌ No matching disease found."

    output = f"""
🩺 Disease: {result['disease']}
💊 Medicine: {", ".join(result['medicines'])}
📏 Dosage: {result['dosage']}
⚠️ Warning: {result['warnings']}
💡 Precautions: {result['precautions']}
📊 Confidence: {result.get('confidence', 'N/A')}%
"""

    # add interaction warnings
    if interactions:
        output += "\n🚫 Drug Interactions:\n"

        for i in interactions:
            if i["severity"] == "high":
                output += f"❌ HIGH: {i['message']}\n"
            elif i["severity"] == "medium":
                output += f"⚠️ MEDIUM: {i['message']}\n"
            else:
                output += f"✅ LOW: {i['message']}\n"
    else:
        output += "\n✅ No dangerous interactions found"

    return output