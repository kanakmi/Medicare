## The folder structure is as follows - 

- Datasets - Contains Datasets that were used to train diabetes, heart disease and thyroid models. Datasets of COVID and Brain Tumor Classifier were large enough to not fit in GitHub's small space.
- Model Training - All the steps performed to train the model (including Quantization Steps with proper comments)
- Saved Models - All the Trained Models

## More about Model Training - 

1) Covid Classifier - The model classifies Chest X-Ray images as COVID-19/Viral Pneumonia/Normal
   - We have 1955 Training Images and 185 Test Images.
   - We Horizontally Flipped the images and obtained 3910 total samples out of which 15% (587 samples) formed the Validation Set and rest (3323 samples) formed the Training Set.
   - We designed a Sequential Model having 5 Convolutional Layers and 4 Dense Layers.
   - The model with least Validation Loss was saved during the training and reloaded before obtaining the final results.
   - The model was able to classify 99.45% of the samples correctly.
   - The Precision and Recall is also good for all the classes.
   - The final model was 30.1 MB in size which was reduced to 2.41 MB using Quantization Aware Training.

2) Brain Tumor Classifier - The model classifies Brain Tumor MRI images as Tumor/No Tumor
   - Dataset had 3929 total Brain MRI images
   - 2556 images belonged to the category of No Tumor
   - 1373 images belonged to the category of Tumor
   - The model was designed using 6 Convolutional Layers, 1 Dense Layer and 1 output layer (with 2 neurons)
   - The model was able to classify 96.27% of the samples correctly.
   - The final model was 2.29 MB in size which was reduced to 196.98 KB using Quantization Aware Training.

3) Diabetes Prediction -
   - Input Features -
   ```
   Pregnancies - number of times person has been pregnant
   Glucose - glucose levels in Hg 
   BloodPressure - blood pressure in mm hg
   SkinThickness - skin thickness in mm
   Insulin - insulin levels in mIU/L
   BMI - Body Mass Index in Kg/m2
   DiabetesPedigreeFunction - likelihood of diabetes based on family history
   Age - age in years
   ```
   - Outputs - Yes/No (It's more of a prediction about at Risk of Diabetes or Not)
   - The model was trained using Logistic Regression and had a accuracy of around 82%.

4) Heart Disease Prediction - 
   - Input Features - 
   ```
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
   ```
   - Outputs - Yes/No (At risk of suffering from a Heart Disease)
   - The model was trained using Logistic Regression and had a accuracy of around 93%.

5) Throid Prediction -
   - Input Features-
    ```
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
    ```
   - Outputs - No / Yes, risk of Hypo-thyroidism / Yes, risk of Hypo-thyroidism
   - The model was trained using Random Forest and had a accuracy of around 99%.
