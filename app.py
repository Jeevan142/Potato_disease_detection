import streamlit as st

# Page Config
st.set_page_config(page_title="Potato AI", page_icon="🥔", layout="wide")

# ------------------- CSS -------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e6ffe6, #f0fff0);
}

.hero {
    background: linear-gradient(to right, #56ab2f, #a8e063);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 50px;
}

.hero p {
    font-size: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    text-align: center;
}

.footer {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ------------------- HERO SECTION -------------------
st.markdown("""
<div class="hero">
    <h1>🥔 Smart Potato Disease Detection</h1>
    <p>AI-powered system to detect Early Blight, Late Blight & Healthy crops</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ------------------- BANNER IMAGE -------------------
st.image("assets/banner.png", use_container_width=True)

st.write("")

# ------------------- IMAGE GROUP -------------------
st.markdown("## 🌿 Understanding Potato Leaf Conditions")





# ------------------- INFO SECTION -------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.success("✅ Healthy Leaf")
    st.write("Green, fresh, no spots. Plant is healthy.")

with col2:
    st.warning("🦠 Early Blight")
    st.write("Brown spots with concentric rings.")

with col3:
    st.error("⚠️ Late Blight")
    st.write("Dark lesions, spreads very fast.")

st.write("")

# ------------------- FEATURES -------------------
st.markdown("## 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    📸 <h3>Upload Image</h3>
    Detect disease instantly from leaf image
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    🧠 <h3>AI Prediction</h3>
    Deep learning powered classification
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    💊 <h3>Solutions</h3>
    Get treatment suggestions instantly
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ------------------- HOW TO USE -------------------
st.markdown("## 📌 How to Use")

st.info("""
1. Go to the **Prediction page** from sidebar 👉  
2. Upload a potato leaf image 📤  
3. Get instant AI prediction 🧠  
4. Follow suggested treatment 💊  
""")

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown('<div class="footer">🌱 Built for Smart Agriculture | AI Project</div>', unsafe_allow_html=True)