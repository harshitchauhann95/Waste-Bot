import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="WasteBot - AI Waste Segregation", layout="centered")

st.title("♻️ WasteBot - AI Waste Segregation")
st.markdown("### Upload an image or describe the waste item to classify it correctly.")

# Image Upload Section
uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)  # ✅ Fixed warning

    if st.button("Classify Image"):
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post("http://127.0.0.1:5000/classify_image", files=files)
            if response.status_code == 200:
                data = response.json()
                st.success(f"**Category:** {data['category']}")
                st.info(f"**Instructions:** {data['instructions']}")
            else:
                st.error("⚠️ Failed to classify image. Please try again.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Text Input Section
st.markdown("---")
st.markdown("### Or describe the waste item")
text_input = st.text_input("Enter a description of the waste item")
if st.button("Classify Text") and text_input:
    try:
        response = requests.post("http://127.0.0.1:5000/classify_text", json={"description": text_input})
        if response.status_code == 200:
            data = response.json()
            st.success(f"**Category:** {data['category']}")
            st.info(f"**Instructions:** {data['instructions']}")
        else:
            st.error("⚠️ Failed to classify text. Please try again.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# Leaderboard Section
st.markdown("---")
st.markdown("### 🌟 Leaderboard")
try:
    leaderboard_response = requests.get("http://127.0.0.1:5000/leaderboard")
    if leaderboard_response.status_code == 200:
        leaderboard_data = leaderboard_response.json()
        for user in leaderboard_data:
            st.write(f"**{user['name']}**: {user['points']} points")
    else:
        st.error("⚠️ Failed to load leaderboard.")
except Exception as e:
    st.error(f"❌ Error: {e}")

# Reward Section
st.markdown("---")
st.markdown("### 🎁 Claim Your Reward")
reward_name = st.text_input("Enter your name to claim reward")
if st.button("Claim Reward") and reward_name:
    try:
        reward_response = requests.post("http://127.0.0.1:5000/reward", json={"user": reward_name})
        if reward_response.status_code == 200:
            reward_data = reward_response.json()
            st.success(f"{reward_data['message']} You earned {reward_data['points_awarded']} points!")
        else:
            st.error("⚠️ Failed to claim reward.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

st.markdown("---")
st.markdown("🌍 *Let's make sustainability simple and rewarding!* 🚀")