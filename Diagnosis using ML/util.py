import pickle
import numpy as np

'''
Input Features-

age - age in years
sex - (1 = male, 0 = female)
cp - chest pain type (0 = No pain, 1 = low, 2 = moderate, 3 = Severe)
trestbps - resting blood pressure (in mm Hg)
chol - serum cholestoral in mg/dl
fbs - fasting blood sugar (1 = greator that 120 mg/dl; 0 = lesser that 120 mg/dl)
restecg - resting electrocardiographic results (0=normal, 1=ST-T wave abnormality, 2=left ventricular hypertrophy)
thalach - maximum heart rate achieved
exang - exercise induced angina (1 = yes, 0 = no)
oldpeak - ST depression induced by exercise relative to rest
slope - the slope of the peak exercise ST segment (0=upsloping, 1=flat, 2=downsloping)
ca - number of major vessels (0-3) colored by flourosopy
thal - (1 = normal; 2 = fixed defect; 3 = reversable defect)

sample input = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
'''

def heart_disease(inputs):
    label = ['No, you are not at risk of heart disease', 'Yes, you are at risk of heart disease']
    with open('./Saved Models/heart_disease.pickle', 'rb') as f:
        model = pickle.load(f)
    inputs = np.asarray(inputs)
    pred = model.predict(inputs.reshape(1, -1))
    return label[pred[0]]

'''
Input Features-

Pregnancies - number of times person has been pregnant
Glucose - glucose levels in Hg 
BloodPressure - blood pressure in mm hg
SkinThickness - skin thickness in mm
Insulin - insulin levels in mIU/L
BMI - Body Mass Index in Kg/m2
DiabetesPedigreeFunction - likelihood of diabetes based on family history
Age - age in years

sample input = [1, 89, 66, 23, 94, 28.1, 0.167, 21]
'''

def diabetes(inputs):
    label = ['No, you are not at risk of diabetes', 'Yes, you are at risk of diabetes']
    with open('./Saved Models/diabetes.pickle', 'rb') as f:
        model = pickle.load(f)
    inputs = np.asarray(inputs)
    pred = model.predict(inputs.reshape(1, -1))
    return label[pred[0]]

'''
Input Features-

Age - age in years
Sex - (1 = male, 0 = female)
On_thyroxine - (1 = yes, 0 = no)
Query_on_thyroxine - (1 = yes, 0 = no)
On_antithyroid_medication - (1 = yes, 0 = no)
Sick - (1 = yes, 0 = no)
Pregnant - (1 = yes, 0 = no)
Thyroid surgery - (1 = yes, 0 = no)
I131_treatment - (1 = yes, 0 = no)
Query_hypothyroid - (1 = yes, 0 = no)
Query_hyperthyroid - (1 = yes, 0 = no)
Lithium - (1 = yes, 0 = no)
Goiter - (1 = yes, 0 = no)
Tumor - (1 = yes, 0 = no)
Hypopituitary - (1 = yes, 0 = no)
Psych - (1 = yes, 0 = no)
TSH - TSH levels in mIU/mL
T3 - T3 levels in pg/dl
TT4 - TT4 levels in ng/dl
T4U - Thyroxine Utilization Rates
FTI - Free Thyroxine Index

sample input = [24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00025,0.03,0.143,0.133,0.108]
'''

def thyroid(inputs):
    inputs[0] = inputs[0]/100
    label = {1:'No, you are not at risk of thyroid', 2:'Yes, you are at risk of Hypo-thyroidism', 3:'Yes, you are at risk of Hyper-thyroidism'}
    with open('./Saved Models/thyroid.pickle', 'rb') as f:
        model = pickle.load(f)
    inputs = np.asarray(inputs)
    pred = model.predict(inputs.reshape(1, -1))
    return label[pred[0]]