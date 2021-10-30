# Medicare

## 💡 Inspiration
Our inspiration was to create an all-in-one health platform where people can ask for the blood of a particular blood group when needed, can self-diagnose some common diseases (and some not-so-common diseases as well), read health blogs and also create/join chat rooms and interact with other random people online aiming at improving their mental health.

## 💻 What it does
- Users can check if they are infected with any kind of heart disease, diabetes, thyroid, or not.
- They can also diagnose their Chest X-Ray Scans for COVID-19/Viral Pneumonia
- They can also diagnose their Brain MRI Scans for Tumor
- They can offer to donate blood
- They will get notified when blood is available
- There is also a chatroom for sharing your thoughts with the world

## ⚙️How we built it

- ML: Python, Skikit-Learn, TensorFlow (want to know more? [Click Here](https://github.com/kanakmi/Medicare/tree/main/Diagnosis%20using%20ML))
- Frontend: HTML, CSS, JS
- Backend: Django
- Database: CockroachDB
- Authentication: Auth0
- Sending an email once the blood is available and sending the reports of disease prediction: (Twilio API)

## Use of CockroachDB

- We have used CockroachDB as a primary database because it is an easy-to-use, open-source and indestructible SQL database.

## 🔑 Auth0

- We have used Auth0 for secure user authentication

## Twilio

- People can request blood from their nearest hospital and they will get a message on their registered email-id once blood is available.
- Hospitals will also get an email if someone requests blood from them
- Users will also get an email if someone wants to donate their blood or money.
- The reports of disease prediction will also be sent to User's email.

## 🧠 Challenges we ran into

- Reducing the size of the trained model was challenging for us. Bigger size meant that users have to wait a long time for obtaining prediction results and we would not be able to upload it on GitHub as well. We researched about the ways we can use to reduce model's size and found Quantization Aware Training to be useful and effective and we are glad it worked.

## 🏅 Accomplishments that we're proud of

- Achieving 80%+ accuracy on all three ML models (specifically 97%+ on Thyroid, Covid Chest X-Ray, Brain Tumor) is a feat we are definitely proud of.
- Completing all these features in just two days is another.

## 📖 What we learned

- Using Quantization Aware Training to reduce size of the model
- Integrate ML models directly without creating an API with Django 
- collaboration.

## 🚀 What's next for Medicare

Improving the accuracy of the models and adding more self-diagnosis models.
