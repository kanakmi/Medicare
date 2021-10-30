import pickle
import numpy as np
from PIL import Image
import numpy as np
import tensorflow as tf

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

'''
COVID Chest X-Ray Classifier
It accepts the path of the image as input.
It returns two things -
1) The class of the image (COVID-19/Viral Pneumonia/Normal)
1) The probability of the image being COVID-19/Viral Pneumonia/Normal
'''

# global variable that will be used to store the interpreter
covid_interpreter = None

def input_covid_classifier():
    # function to read the model from disk
    global covid_interpreter
    covid_interpreter = tf.lite.Interpreter(model_path='./Saved Models/covid_classifier.tflite')
    covid_interpreter.allocate_tensors()

def covid(path):

    labels = {0: "covid", 1: "viral_pneumonia", 2: "normal"}

    if covid_interpreter==None:
        input_covid_classifier()

    input_details = covid_interpreter.get_input_details()
    output_details = covid_interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    output_shape = output_details[0]['shape']
    
    image = Image.open(path)
    image = image.convert("RGB")
    image = image.resize((256, 256))
    image = np.array(image)

    img = image.astype('Float32')
    img = img/255
    img = img.reshape((1, 256, 256, 3))
    covid_interpreter.set_tensor(input_details[0]['index'], img)
    covid_interpreter.invoke()
    predictions = covid_interpreter.get_tensor(output_details[0]['index'])
    pred = np.argmax(predictions[0])
    result = {
        'class': labels[pred],
        'class_probablity': np.round(predictions[0][pred]*100,2)
    }
    return result

'''
Brain Tumor MRI Classifier
It accepts the path of the image as input.
It returns two things -
1) The class of the image (Tumor/No Tumor)
1) The probability of the image being Tumor/No Tumor
'''

# global variable that will be used to store the interpreter
tumor_interpreter = None

def input_tumor_classifier():
    # function to read the model from disk
    global tumor_interpreter
    tumor_interpreter = tf.lite.Interpreter(model_path='./Saved Models/brain_tumor_classifier.tflite')
    tumor_interpreter.allocate_tensors()

def tumor(path):

    labels = {0: 'No Tumor', 1: 'Tumor'}

    if tumor_interpreter==None:
        input_tumor_classifier()

    input_details = tumor_interpreter.get_input_details()
    output_details = tumor_interpreter.get_output_details()

    input_shape = input_details[0]['shape']
    output_shape = output_details[0]['shape']
    
    image = Image.open(path)
    image = image.convert("RGB")
    image = image.resize((128, 128))
    image = np.array(image)

    img = image.astype('Float32')
    img = img/255
    img = img.reshape((1, 128, 128, 3))
    tumor_interpreter.set_tensor(input_details[0]['index'], img)
    tumor_interpreter.invoke()
    predictions = tumor_interpreter.get_tensor(output_details[0]['index'])
    pred = np.argmax(predictions[0])
    result = {
        'class': labels[pred],
        'class_probablity': np.round(predictions[0][pred]*100,2)
    }
    return result