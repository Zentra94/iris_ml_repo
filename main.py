import streamlit as st
import pandas as pd
import joblib
from configs import PATH_DATA_MODELS, PATH_STATICS
from data.utils import get_dict
from PIL import Image

# Title
st.header("Streamlit Machine Learning App")

# Input bar 1
sepal_length = st.number_input("Enter Sepal Length (cm)")

# Input bar 2
sepal_width = st.number_input("Enter Sepal Width (cm) ")

# Input bar 3
petal_length = st.number_input("Enter Petal Length (cm) ")

# Input bar 4
petal_width = st.number_input("Enter Petal Width (cm) ")

# If button is pressed
if st.button("Submit"):
    # Unpickle classifier
    model = joblib.load(PATH_DATA_MODELS / "model.sav")
    features = model.feature_names_in_

    # Store inputs into dataframe
    X = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                     columns=[features])
    labels = get_dict("target_labels.json")

    # Get prediction
    prediction = model.predict(X)[0]
    pred = ""
    for name in labels:
        if prediction == labels[name]:
            pred = name
    # Output prediction
    path_img = PATH_STATICS / "{}_iris.jpg".format(pred)
    image = Image.open(path_img)
    st.image(image, caption="The flower is a {}".format(pred))

