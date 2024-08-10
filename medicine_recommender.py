# Define a dictionary of diseases with their symptoms
disease_symptoms = {
    "Flu": ["fever", "cough", "sore throat", "runny nose"],
    "Cold": ["runny nose", "sneezing", "cough"],
    "Headache": ["headache", "nausea", "sensitivity to light"],
    "Stomachache": ["stomach pain", "nausea", "vomiting"],
}

# Define a dictionary of medicines for each disease
medicine_recommendations = {
    "Flu": ["Paracetamol", "Cough syrup"],
    "Cold": ["Decongestant", "Antihistamine"],
    "Headache": ["Ibuprofen", "Acetaminophen"],
    "Stomachache": ["Antacids", "Pepto-Bismol"],
}

def recommend_medicine(symptoms):
    # Find matching disease
    matched_disease = None
    for disease, disease_symps in disease_symptoms.items():
        if all(symptom in disease_symps for symptom in symptoms):
            matched_disease = disease
            break
    
    if matched_disease:
        medicines = medicine_recommendations.get(matched_disease, [])
        return f"Recommended medicines for {matched_disease}: {', '.join(medicines)}"
    else:
        return "No matching disease found for the given symptoms."

def main():
    print("Welcome to the Medicine Recommendation System")
    
    # Get symptoms from the user
    symptoms = input("Enter your symptoms (comma-separated): ").strip().lower().split(",")
    symptoms = [symptom.strip() for symptom in symptoms]
    
    # Get recommendations
    recommendation = recommend_medicine(symptoms)
    print(recommendation)

if __name__ == "__main__":
    main()
