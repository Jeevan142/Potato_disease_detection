import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("potato_model.h5", compile=False)

model = load_model()

class_names = ["Early Blight", "Late Blight", "Healthy"]

disease_info = {
    "Early Blight": {
        "desc": "Brown spots with rings",
        "solution": "Use fungicide, remove leaves"
    },
    "Late Blight": {
        "desc": "Dark lesions, spreads fast",
        "solution": "Immediate treatment required"
    },
    "Healthy": {
        "desc": "Plant is healthy",
        "solution": "Maintain care"
    }
}

st.title("🔍 Disease Prediction")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload leaf image", type=["jpg","png","jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

with col2:
    if uploaded_file:
        img = image.resize((224,224))
        img = np.array(img)/255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        score = tf.nn.softmax(prediction[0])

        predicted_class = class_names[np.argmax(score)]
        confidence = np.max(score)*100

        st.success(f"Prediction: {predicted_class}")
        st.progress(int(confidence))
        st.write(f"Confidence: {confidence:.2f}%")

        # Chart
        fig = px.bar(
            x=class_names,
            y=[float(s*100) for s in score],
            labels={'x':'Disease','y':'Confidence'},
            title="Prediction Probability"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.info(disease_info[predicted_class]["desc"])
        st.warning(disease_info[predicted_class]["solution"])