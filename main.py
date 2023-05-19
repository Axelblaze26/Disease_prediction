from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model=pickle.load(open("rf.pkl", "rb"))
@app.route("/",methods=["POST","GET"])
def home():
    symptom1 = request.form.get("s1")
    symptom2 = request.form.get("s2")
    symptom3 = request.form.get("s3")
    symptom4 = request.form.get("s4")
    symptom5 = request.form.get("s5")
    l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
          'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
          'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
          'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
          'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
          'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
          'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
          'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
          'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
          'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
          'family_history', 'mucoid_sputum',
          'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
          'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']
    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
               'Impetigo']


    l2 = []
    for i in range(len(l1)):
        l2.append(0)

    inputQuery = np.array([symptom1, symptom2, symptom3, symptom4, symptom5])
    for k in range(len(l1)):
        for z in inputQuery:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = model.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(len(disease)):
        if predicted == a:
            h = 'yes'
            break

    prognosis = {
        "Fungal infection": {
            "introduction": "Fungal infection is a common skin condition caused by fungi. It can affect various parts of the body, such as the skin, nails, and hair.",
            "precautions": "Keep the affected area clean and dry, avoid sharing personal items, wear loose and breathable clothing."
        },
        "Allergy": {
            "introduction": "Allergy refers to an exaggerated immune response to substances that are usually harmless. It can cause various symptoms, including sneezing, itching, and rashes.",
            "precautions": "Identify and avoid allergens, keep the living environment clean, use air filters, take prescribed medications."
        },
        "GERD": {
            "introduction": "GERD (Gastroesophageal Reflux Disease) is a chronic digestive disorder that occurs when stomach acid flows back into the esophagus, causing irritation and discomfort.",
            "precautions": "Maintain a healthy weight, avoid trigger foods and beverages, eat smaller meals, don't lie down immediately after eating."
        },
        "Chronic cholestasis": {
            "introduction": "Chronic cholestasis is a condition characterized by the impaired flow of bile from the liver. It can lead to various complications and liver damage.",
            "precautions": "Follow a low-fat diet, avoid alcohol and tobacco, take prescribed medications, get regular exercise."
        },
        "Drug Reaction": {
            "introduction": "Drug reaction refers to an adverse reaction to a medication or drug. It can manifest in various ways, such as skin rashes, itching, and swelling.",
            "precautions": "Take medications as prescribed, be aware of potential drug interactions, consult a healthcare professional."
        },
        "Peptic ulcer disease": {
            "introduction": "Peptic ulcer disease is a condition characterized by the formation of open sores in the lining of the stomach or the upper part of the small intestine. It can cause abdominal pain and discomfort.",
            "precautions": "Avoid spicy and acidic foods, limit alcohol and caffeine intake, quit smoking, manage stress."
        },
        "AIDS": {
            "introduction": "AIDS (Acquired Immunodeficiency Syndrome) is a chronic condition caused by the human immunodeficiency virus (HIV). It weakens the immune system and makes individuals more susceptible to infections and diseases.",
            "precautions": "Practice safe sex, use clean needles for injections, take antiretroviral therapy, get vaccinated for opportunistic infections."
        },
        "Diabetes": {
            "introduction": "Diabetes is a chronic metabolic disorder characterized by high blood sugar levels. It can lead to various complications if not properly managed.",
            "precautions": "Monitor blood sugar levels, follow a balanced diet, engage in regular physical activity, take prescribed medications."
        },
        "Gastroenteritis": {
            "introduction": "Gastroenteritis, commonly known as the stomach flu, is an inflammation of the stomach and intestines. It is usually caused by viral or bacterial infections.",
            "precautions": "Wash hands frequently, avoid contaminated food and water, practice good hygiene, stay hydrated."
        },
        "Bronchial Asthma": {
            "introduction": "Bronchial asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways. It can cause breathing difficulties, coughing, and wheezing.",
            "precautions": "Identify and avoid triggers, take prescribed medications regularly, use inhalers as instructed."
        },
        "Hypertension": {
            "introduction": "Hypertension, or high blood pressure, is a common cardiovascular condition. It can increase the risk of heart disease, stroke, and other complications.",
            "precautions": "Maintain a healthy weight, reduce sodium intake, exercise regularly, manage stress, take prescribed medications."
        },
        "Migraine": {
            "introduction": "Migraine is a neurological condition characterized by severe headaches, often accompanied by other symptoms such as nausea, sensitivity to light and sound, and visual disturbances.",
            "precautions": "Identify and avoid triggers, establish a regular sleep schedule, manage stress, take prescribed medications."
        },
        "Cervical spondylosis": {
            "introduction": "Cervical spondylosis is a degenerative condition that affects the cervical spine (neck). It can cause neck pain, stiffness, and reduced range of motion.",
            "precautions": "Maintain good posture, avoid lifting heavy weights, practice neck exercises, use a supportive pillow."
        },
        "Paralysis (brain hemorrhage)": {
            "introduction": "Paralysis due to brain hemorrhage is a condition in which there is a loss of muscle function or movement in certain parts of the body due to bleeding in the brain.",
            "precautions": "Follow a rehabilitation program, use assistive devices if necessary, take prescribed medications."
        },
        "Jaundice": {
            "introduction": "Jaundice is a condition characterized by yellowing of the skin and eyes. It occurs when there is a buildup of bilirubin, a yellow pigment, in the blood.",
            "precautions": "Avoid alcohol and fatty foods, maintain hydration, practice good hygiene, get vaccinated for hepatitis."
        },
        "Malaria": {
            "introduction": "Malaria is a mosquito-borne infectious disease caused by parasites. It can cause flu-like symptoms, including fever, chills, and body aches.",
            "precautions": "Use mosquito repellents, sleep under insecticide-treated nets, take prescribed antimalarial medications."
        },
        "Chickenpox": {
            "introduction": "Chickenpox is a highly contagious viral infection. It causes an itchy rash with small, fluid-filled blisters. Most people recover without any complications.",
            "precautions": "Avoid close contact with infected individuals, maintain good hygiene, use calamine lotion, take antiviral medications."
        },
        "Dengue": {
            "introduction": "Dengue fever is a mosquito-borne viral infection. It can cause high fever, severe headache, joint and muscle pain, and a rash.",
            "precautions": "Prevent mosquito breeding, use mosquito repellents, wear protective clothing, stay hydrated."
        },
        "Typhoid": {
            "introduction": "Typhoid fever is a bacterial infection caused by Salmonella typhi. It spreads through contaminated food and water and can cause high fever and gastrointestinal symptoms.",
            "precautions": "Practice good hygiene, drink clean water, eat thoroughly cooked food, get vaccinated."
        },
        "Hepatitis A": {
            "introduction": "Hepatitis A is a viral infection that affects the liver. It spreads through contaminated food and water and can cause jaundice, fatigue, and digestive symptoms.",
            "precautions": "Maintain good hygiene, practice safe food and water habits, get vaccinated."
        },
        "Hepatitis B": {
            "introduction": "Hepatitis B is a viral infection that affects the liver. It spreads through contact with infected blood, bodily fluids, or from mother to child during childbirth.",
            "precautions": "Get vaccinated, practice safe sex, avoid sharing needles or personal items, get regular check-ups."
        },
        "Hepatitis C": {
            "introduction": "Hepatitis C is a viral infection that affects the liver. It spreads through contact with infected blood, often due to sharing needles or other drug paraphernalia.",
            "precautions": "Avoid sharing needles or personal items, practice safe sex, get regular check-ups, consider hepatitis C screening."
        },
        "Hepatitis D": {
            "introduction": "Hepatitis D is a viral infection that only occurs in individuals who are already infected with hepatitis B. It can cause severe liver damage.",
            "precautions": "Get vaccinated for hepatitis B, practice safe sex, avoid sharing needles or personal items, get regular check-ups."
        },
        "Hepatitis E": {
            "introduction": "Hepatitis E is a viral infection that primarily spreads through contaminated water. It can cause acute liver disease and is usually self-limiting.",
            "precautions": "Drink clean water, practice good hygiene, avoid consuming raw or undercooked shellfish, get vaccinated if available."
        },
        "Alcoholic hepatitis": {
            "introduction": "Alcoholic hepatitis is inflammation of the liver caused by excessive alcohol consumption. It can lead to liver damage and cirrhosis.",
            "precautions": "Avoid or limit alcohol consumption, seek treatment for alcohol dependence, follow a balanced diet, get regular check-ups."
        },
        "Tuberculosis": {
            "introduction": "Tuberculosis (TB) is a bacterial infection that primarily affects the lungs. It can cause coughing, chest pain, and fatigue.",
            "precautions": "Take prescribed medications regularly, cover the mouth while coughing or sneezing, maintain good ventilation."
        },
        "Common Cold": {
            "introduction": "The common cold is a viral infection of the upper respiratory tract. It is characterized by symptoms such as a runny nose, sneezing, and sore throat.",
            "precautions": "Practice good hygiene, wash hands frequently, avoid close contact with infected individuals, get plenty of rest."
        },
        "Pneumonia": {
            "introduction": "Pneumonia is an infection that inflames the air sacs in one or both lungs. It can cause coughing, fever, and difficulty breathing.",
            "precautions": "Practice good hygiene, get vaccinated for pneumonia, avoid close contact with infected individuals, take prescribed antibiotics."
        },
        "Dimorphic hemorrhoids (piles)": {
            "introduction": "Dimorphic hemorrhoids, also known as piles, are swollen blood vessels in the rectum or anus. They can cause discomfort, pain, and bleeding.",
            "precautions": "Eat a high-fiber diet, drink plenty of fluids, avoid straining during bowel movements, exercise regularly."
        },
        "Heart attack": {
            "introduction": "A heart attack, also known as a myocardial infarction, occurs when blood flow to the heart is blocked, leading to damage to the heart muscle.",
            "precautions": "Maintain a healthy lifestyle, eat a balanced diet, exercise regularly, manage stress, take prescribed medications."
        },
        "Varicose veins": {
            "introduction": "Varicose veins are enlarged, twisted veins that usually occur in the legs. They can cause pain, swelling, and aching discomfort.",
            "precautions": "Exercise regularly, elevate legs while resting, avoid standing or sitting for long periods, wear compression stockings."
        },
        "Hypothyroidism": {
            "introduction": "Hypothyroidism is a condition in which the thyroid gland doesn't produce enough thyroid hormones. It can cause fatigue, weight gain, and depression.",
            "precautions": "Take prescribed thyroid medication, follow a balanced diet, exercise regularly, get regular check-ups."
        },
        "Hyperthyroidism": {
            "introduction": "Hyperthyroidism is a condition in which the thyroid gland produces too much thyroid hormone. It can cause weight loss, rapid heartbeat, and irritability.",
            "precautions": "Take prescribed medication, follow a balanced diet, manage stress, get regular check-ups."
        },
        "Hypoglycemia": {
            "introduction": "Hypoglycemia is a condition characterized by low blood sugar levels. It can cause symptoms such as dizziness, confusion, and sweating.",
            "precautions": "Monitor blood sugar levels regularly, eat regular meals and snacks, carry glucose tablets or snacks, wear a medical alert bracelet."
        },
        "Osteoarthritis": {
            "introduction": "Osteoarthritis is a degenerative joint disease characterized by the breakdown of cartilage. It can cause joint pain, stiffness, and reduced range of motion.",
            "precautions": "Manage weight, exercise regularly, avoid excessive joint stress, use assistive devices if needed, take prescribed medications."
        },
        "Arthritis": {
            "introduction": "Arthritis is a term that refers to inflammation of the joints. There are different types of arthritis, including rheumatoid arthritis and osteoarthritis.",
            "precautions": "Maintain a healthy weight, exercise regularly, apply hot or cold packs, take prescribed medications, consider physical therapy."
        },
        "(Vertigo) Paroxysmal Positional Vertigo": {
            "introduction": "Paroxysmal positional vertigo (BPPV) is a type of vertigo that occurs when there is a problem with the inner ear. It can cause episodes of dizziness and a spinning sensation.",
            "precautions": "Avoid sudden head movements, sleep with your head elevated, avoid bending or extending the neck excessively."
        },
        "Acne": {
            "introduction": "Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells. It can cause pimples, blackheads, and whiteheads.",
            "precautions": "Keep the affected area clean, avoid squeezing or picking at pimples, use non-comedogenic skincare products, manage stress."
        },
        "Urinary tract infection": {
            "introduction": "A urinary tract infection (UTI) is an infection that affects any part of the urinary system, including the kidneys, bladder, and urethra. It can cause symptoms such as frequent urination and a burning sensation.",
            "precautions": "Drink plenty of water, urinate before and after sexual activity, practice good hygiene, take prescribed antibiotics."
        },
        "Psoriasis": {
            "introduction": "Psoriasis is a chronic autoimmune condition that affects the skin. It causes red, scaly patches that can be itchy and painful.",
            "precautions": "Keep the skin moisturized, avoid triggers such as stress and certain medications, use prescribed medications or topical treatments."
        },
        "Impetigo": {
            "introduction": "Impetigo is a highly contagious bacterial skin infection. It causes red sores that can break open and form a yellowish crust.",
            "precautions": "Keep the affected area clean, avoid touching or scratching the sores, wash hands frequently, take prescribed antibiotics."
        },
        "Fungal nail infection": {
            "introduction": "Fungal nail infection, also known as onychomycosis, is a fungal infection of the nails. It can cause thickened, discolored nails that may be brittle or crumbly.",
            "precautions": "Keep nails clean and dry, wear breathable footwear, avoid sharing nail clippers or files, use antifungal treatments."
        }
    }
    if h == 'yes':
        # return jsonify({"Disease": disease[a]})
        return jsonify({"disease":disease[a], "info": prognosis[disease[a]]})
    else:
        return jsonify({"disease": "Not found"})


if __name__ == "__main__":
    app.run(debug=True)