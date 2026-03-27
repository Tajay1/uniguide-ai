import streamlit as st

st.set_page_config(page_title="UniGuide AI", layout="wide")

# Title
st.title("🎓 UniGuide AI")
st.write("Your smart assistant for universities in Jamaica 🇯🇲")

# Sidebar
page = st.sidebar.radio("Navigation", ["Home", "Chat", "About", "Documentation"])

# ---------------- HOME ----------------
if page == "Home":
    st.header("Welcome to UniGuide AI")
    st.write("""
    This AI helps students:
    - Find universities in Jamaica
    - Understand entry requirements
    - Explore programs
    - Compare tuition
    """)

# ---------------- CHAT ----------------
elif page == "Chat":
    st.header("💬 Ask UniGuide AI")

    user_input = st.text_input("Enter your question:")

    if st.button("Submit"):
        if user_input:
            # SIMPLE LOGIC (temporary AI)
            if "subjects" in user_input.lower():
                st.success("Most universities require at least 5 CSEC subjects including English and Math.")
            elif "cheapest" in user_input.lower():
                st.success("UCC and NCU are generally more affordable options.")
            elif "uwi" in user_input.lower():
                st.success("UWI is one of the top universities in Jamaica.")
            else:
                st.success("This AI will provide more detailed answers soon.")
        else:
            st.warning("Please enter a question.")

# ---------------- ABOUT ----------------
elif page == "About":
    st.header("About UniGuide AI")
    st.write("""
    UniGuide AI is designed to help students make informed decisions
    about universities in Jamaica.
    """)

# ---------------- DOCUMENTATION ----------------
elif page == "Documentation":
    st.header("How to Use")
    st.write("""
    1. Go to Chat  
    2. Ask questions  
    3. Get answers  

    Note: This AI provides general guidance only.
    """)
