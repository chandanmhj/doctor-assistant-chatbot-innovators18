# doctor-assistant-chatbot-innovators18
An AI powered chat bot that interacts with the doctor to minimize the time consumed for the history reading





mongo db comapass local data input
database name - "doctors_db", collection name - "patients"








[
  {
    "patient_id": 101,
    "name": "John Doe",
    "age": 45,
    "medical_history": ["Hypertension", "Diabetes Type 2"],
    "current_medications": [
      {"name": "Metformin", "dosage": "500mg", "frequency": "Twice daily"},
      {"name": "Lisinopril", "dosage": "10mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 120,
      "blood_pressure": "130/85",
      "bmi": 27.5,
      "cholesterol": 200,
      "heart_rate": 72
    }
  },
  {
    "patient_id": 102,
    "name": "Jane Smith",
    "age": 38,
    "medical_history": ["Asthma"],
    "current_medications": [
      {"name": "Albuterol", "dosage": "90mcg", "frequency": "As needed"},
      {"name": "Fluticasone", "dosage": "110mcg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 95,
      "blood_pressure": "120/80",
      "bmi": 22.0,
      "cholesterol": 190,
      "heart_rate": 70
    }
  },
  {
    "patient_id": 103,
    "name": "Emily Johnson",
    "age": 60,
    "medical_history": ["Osteoarthritis", "Hypertension"],
    "current_medications": [
      {"name": "Ibuprofen", "dosage": "200mg", "frequency": "Twice daily"},
      {"name": "Amlodipine", "dosage": "5mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 110,
      "blood_pressure": "140/90",
      "bmi": 30.2,
      "cholesterol": 210,
      "heart_rate": 78
    }
  },
  {
    "patient_id": 104,
    "name": "Michael Brown",
    "age": 50,
    "medical_history": ["Hyperlipidemia", "Gout"],
    "current_medications": [
      {"name": "Atorvastatin", "dosage": "20mg", "frequency": "Once daily"},
      {"name": "Colchicine", "dosage": "0.6mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 105,
      "blood_pressure": "125/82",
      "bmi": 29.0,
      "cholesterol": 240,
      "heart_rate": 76
    }
  },
  {
    "patient_id": 105,
    "name": "Olivia White",
    "age": 33,
    "medical_history": ["Anxiety", "Chronic migraines"],
    "current_medications": [
      {"name": "Sertraline", "dosage": "50mg", "frequency": "Once daily"},
      {"name": "Topiramate", "dosage": "25mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 98,
      "blood_pressure": "118/75",
      "bmi": 21.5,
      "cholesterol": 180,
      "heart_rate": 80
    }
  },
  {
    "patient_id": 106,
    "name": "Christopher Green",
    "age": 42,
    "medical_history": ["Back pain"],
    "current_medications": [
      {"name": "Hydrocodone", "dosage": "5mg", "frequency": "As needed"},
      {"name": "Pregabalin", "dosage": "150mg", "frequency": "Twice daily"}
    ],
    "health_metrics": {
      "blood_sugar": 120,
      "blood_pressure": "130/88",
      "bmi": 26.0,
      "cholesterol": 220,
      "heart_rate": 74
    }
  },
  {
    "patient_id": 107,
    "name": "Sophia Black",
    "age": 29,
    "medical_history": ["Hypothyroidism"],
    "current_medications": [
      {"name": "Levothyroxine", "dosage": "75mcg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 100,
      "blood_pressure": "118/76",
      "bmi": 23.0,
      "cholesterol": 190,
      "heart_rate": 68
    }
  },
  {
    "patient_id": 108,
    "name": "David Wilson",
    "age": 55,
    "medical_history": ["COPD", "Smoking history"],
    "current_medications": [
      {"name": "Tiotropium", "dosage": "18mcg", "frequency": "Once daily"},
      {"name": "Fluticasone", "dosage": "250mcg", "frequency": "Twice daily"}
    ],
    "health_metrics": {
      "blood_sugar": 130,
      "blood_pressure": "140/92",
      "bmi": 31.0,
      "cholesterol": 230,
      "heart_rate": 82
    }
  },
  {
    "patient_id": 109,
    "name": "Isabella Martinez",
    "age": 63,
    "medical_history": ["Rheumatoid arthritis", "Depression"],
    "current_medications": [
      {"name": "Methotrexate", "dosage": "10mg", "frequency": "Once weekly"},
      {"name": "Citalopram", "dosage": "20mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 105,
      "blood_pressure": "120/78",
      "bmi": 25.5,
      "cholesterol": 205,
      "heart_rate": 70
    }
  },
  {
    "patient_id": 110,
    "name": "Lucas Hernandez",
    "age": 37,
    "medical_history": ["Seasonal allergies"],
    "current_medications": [
      {"name": "Loratadine", "dosage": "10mg", "frequency": "Once daily"}
    ],
    "health_metrics": {
      "blood_sugar": 95,
      "blood_pressure": "122/80",
      "bmi": 24.2,
      "cholesterol": 180,
      "heart_rate": 72
    }
  }
]
