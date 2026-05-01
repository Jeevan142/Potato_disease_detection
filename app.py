import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Potato AI", page_icon="🥔", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #56ab2f, #a8e063);
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🥔 Potato Disease Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered leaf disease detection system</div>', unsafe_allow_html=True)

st.write("")

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("potato_model.h5", compile=False)

model = load_model()

class_names = ["Early Blight", "Late Blight", "Healthy"]
disease_info = {
    "Early Blight": {
        "desc": "Fungal disease causing brown spots with concentric rings.",
        "solution": "Remove infected leaves, use fungicide, avoid overhead watering."
    },
    "Late Blight": {
        "desc": "Serious disease causing dark lesions and rapid decay.",
        "solution": "Apply fungicides immediately, remove infected plants, ensure good airflow."
    },
    "Healthy": {
        "desc": "No disease detected. Plant is healthy.",
        "solution": "Maintain proper care, watering, and sunlight."
    }
}
# Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📤 Upload Image")
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

with col2:
    st.markdown("### 🧠 Prediction")

    if uploaded_file:
        img = image.resize((224, 224))
        img_array = np.array(img) / 255.0   # ✅ FIXED
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        score = tf.nn.softmax(prediction[0])

        predicted_class = class_names[np.argmax(score)]
        confidence = np.max(score) * 100

        # Create data for chart
        chart_data = {
         "Disease": class_names,
        "Confidence": [float(s * 100) for s in score]
        }

        fig = px.bar(
       chart_data,
       x="Disease",
       y="Confidence",
       color="Disease",
       text="Confidence",
       title="Prediction Probability"
       )

        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(yaxis_range=[0,100])

        st.plotly_chart(fig, use_container_width=True)

        st.success(f"🌿 {predicted_class}")
        st.progress(int(confidence))
        st.write(f"Confidence: {confidence:.2f}%")
        st.markdown("### 🌿 Disease Information")

        st.info(f"🧾 Description: {disease_info[predicted_class]['desc']}")

        if predicted_class == "Healthy":
         st.success(f"✅ Solution: {disease_info[predicted_class]['solution']}")
        else:
         st.warning(f"💊 Solution: {disease_info[predicted_class]['solution']}")

        # Show all probabilities
        st.markdown("### 📊 All Predictions")
        for i, cls in enumerate(class_names):
            st.write(f"{cls}: {score[i]*100:.2f}%")

        # Disease info
        if predicted_class == "Early Blight":
            st.warning("🦠 Early Blight detected. Use fungicides and remove infected leaves.")
        elif predicted_class == "Late Blight":
            st.error("⚠️ Late Blight detected. Immediate treatment required.")
        else:
            st.success("✅ Plant is Healthy!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | AI Project")