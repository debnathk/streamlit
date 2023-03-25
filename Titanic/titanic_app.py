import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from joblib import load

# Add image
img = Image.open('titanic-ship.jpg')
st.image(img, use_column_width = True, caption = 'Titanic - 1912')

# # Add music
# audio_file = open('titanic.mp3', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/mp3')

# Add title
st.title('Titanic Survival Prediction app!')
st.subheader(':blue[Enter information below to predict &#8628;]')

with st.form('Information form'):
    pclass = st.radio('Ticket Class',  ('1st', '2nd', '3rd'))
    sex = st.radio('Sex',  ('Male', 'Female'))
    age = st.slider('Age',  0, 100, 1)
    sibsp = st.slider('Siblings/Spouses',  0, 5, 1)
    parch = st.slider('Parents/Children',  0, 10, 1)
    fare = st.slider('Ticket fare',  0.0, 100.0, 0.1)
    embarked = st.radio('Port of Embarkation', ('Cherbourg', 'Queenstown', 'Southampton'))

    # Add predict button
    button = st.form_submit_button(label = "Predict")

sample = {}
if button:
    sample = {'Ticket Class': pclass, 'Sex': sex, 'Age': age, 'Siblings/Spouses': sibsp, 'Parents/Children': parch, 'Ticket fare': fare, 'Port of Embarkation': embarked}
    # X_test = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

st.write("Passenger details: ", sample)

# Add model
model = load('rf.joblib')

# Transform query
X_sample = list(sample.values())

if sample['Ticket Class'] == "1st":
    X_sample[0] = 1
elif sample['Ticket Class'] == "2nd":
    X_sample[0] = 2
elif sample['Ticket Class'] == "3rd":
    X_sample[0] = 3

if sample['Port of Embarkation'] == "Southampton":
    X_sample[6] = 'S'
elif sample['Port of Embarkation'] == "Queenstown":
    X_sample[6] = 'Q'
elif sample['Port of Embarkation'] == "Cherbourg":
    X_sample[6] = 'C'

# Manual one-hot encoding for a single sample
X_transformed = []
if X_sample[1] == 'Male' and X_sample[6] == 'S':
    X_transformed = [X_sample[0], 1, 0, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 1, 0, 0]
elif X_sample[1] == 'Male' and X_sample[6] == 'C':
    X_transformed = [X_sample[0], 1, 0, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 0, 1, 0]
elif X_sample[1] == 'Male' and X_sample[6] == 'Q':
    X_transformed = [X_sample[0], 1, 0, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 0, 0, 1]
elif X_sample[1] == 'Female' and X_sample[6] == 'S':
    X_transformed = [X_sample[0], 0, 1, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 1, 0, 0]
elif X_sample[1] == 'Female' and X_sample[6] == 'C':
    X_transformed = [X_sample[0], 0, 1, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 0, 1, 0]
elif X_sample[1] == 'Female' and X_sample[6] == 'Q':
    X_transformed = [X_sample[0], 0, 1, X_sample[2], X_sample[3], X_sample[4], X_sample[5], 0, 0, 1]

X_pred = {
    'Pclass' : [X_transformed[0]],
     'Age' : [X_transformed[1]],
     'SibSp' : [X_transformed[2]],
     'Parch' : [X_transformed[3]],
     'Fare' : [X_transformed[4]],
     'Sex_male' : [X_transformed[5]],
     'Sex_female' : [X_transformed[6]],
     'Embarked_S' : [X_transformed[7]],
     'Embarked_C' : [X_transformed[8]],
     'Embarked_Q' : [X_transformed[9]]
}
X_pred = pd.DataFrame.from_dict(X_pred)

prediction = model.predict(X_pred)

if prediction[0] == 0:
    st.subheader("Destiny: RIP!")
elif prediction[0] == 1:
    st.subheader("Destiny: You survived, by god's grace!")
