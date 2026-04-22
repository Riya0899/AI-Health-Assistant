# HEALTH DATASET


health_data = [
    {
        "disease": "Fever",
        "symptoms": ["fever", "headache", "body pain"],
        "medicines": ["Paracetamol"],
        "age_group": "adult",
        "dosage": "500mg",
        "warnings": "Avoid overdose",
        "precautions": "Drink fluids and take rest"
    },
    {
        "disease": "Cold",
        "symptoms": ["cough", "sneezing", "runny nose"],
        "medicines": ["Cetirizine"],
        "age_group": "adult",
        "dosage": "10mg",
        "warnings": "May cause drowsiness",
        "precautions": "Stay warm and hydrated"
    },
    {
        "disease": "Headache",
        "symptoms": ["headache", "stress"],
        "medicines": ["Ibuprofen"],
        "age_group": "adult",
        "dosage": "200mg",
        "warnings": "Avoid empty stomach",
        "precautions": "Take proper rest"
    },

    # CHILD EXAMPLES
    {
        "disease": "Mild Fever",
        "symptoms": ["fever", "weakness"],
        "medicines": ["Paracetamol"],
        "age_group": "child",
        "dosage": "250mg",
        "warnings": "Use pediatric dose only",
        "precautions": "Keep child hydrated"
    },
    {
    "disease": "Flu",
    "symptoms": ["fever", "cough", "body pain", "fatigue"],
    "medicines": ["Paracetamol"],
    "age_group": "adult",
    "dosage": "500mg",
    "warnings": "Avoid overdose",
    "precautions": "Rest and fluids"
},
{
    "disease": "Allergy",
    "symptoms": ["sneezing", "runny nose", "itching"],
    "medicines": ["Cetirizine"],
    "age_group": "adult",
    "dosage": "10mg",
    "warnings": "May cause drowsiness",
    "precautions": "Avoid allergens"
},

    #  SENIOR EXAMPLES
    {
        "disease": "Arthritis (Possible Joint Inflammation)",
        "symptoms": ["joint pain", "stiffness"],
        "medicines": ["Ibuprofen"],
        "age_group": "senior",
        "dosage": "200mg",
        "warnings": "Consult doctor for long-term use",
        "precautions": "Avoid heavy activity"
    },
    {
    "disease": "Osteoarthritis",
    "symptoms": ["joint pain", "stiffness", "reduced mobility"],
    "medicines": ["Ibuprofen"],
        "age_group": "senior",
        "dosage": "200mg",
        "warnings": "Consult doctor for long-term use",
        "precautions": "Avoid heavy activity"
},
{
    "disease": "Rheumatoid Arthritis",
    "symptoms": ["joint pain", "swelling", "fatigue"],
    "medicines": ["Ibuprofen"],
        "age_group": "senior",
        "dosage": "200mg",
        "warnings": "Consult doctor for long-term use",
        "precautions": "Avoid heavy activity"
}
]

# DRUG INTERACTION DATABASE

drug_interactions = {
    ("Paracetamol", "Alcohol"): {
        "severity": "high",
        "message": "❌ Can cause liver damage"
    },
    ("Ibuprofen", "Alcohol"): {
        "severity": "high",
        "message": "❌ Risk of stomach bleeding"
    },
    ("Ibuprofen", "BP_Medicine"): {
        "severity": "medium",
        "message": "⚠️ May increase blood pressure"
    },
    ("Cetirizine", "Alcohol"): {
        "severity": "low",
        "message": "⚠️ Causes drowsiness"
    }
}

# AGE GROUP FUNCTION

def get_age_group(age):
    if age <= 12:
        return "child"
    elif age <= 59:
        return "adult"
    else:
        return "senior"