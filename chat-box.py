elif page == "Chat":
    st.header("💬 Ask UniGuide AI")

    user_input = st.text_input("Enter your question:")

    if st.button("Submit"):
        if user_input:
            response = ""

            if "subjects" in user_input.lower():
                response = "Most universities require at least 5 CSEC subjects including English and Math."
            elif "cheapest" in user_input.lower():
                response = "UCC and NCU are generally more affordable options in Jamaica."
            elif "uwi" in user_input.lower():
                response = "UWI is one of the top universities in Jamaica with strong academic programs."
            elif "sports" in user_input.lower():
                response = "Many universities offer football, track & field, and clubs for student life."
            else:
                response = "I'm still learning! Try asking about universities, tuition, or subjects."

            st.markdown(f"""
            <div class="card">
                <b>🧑 You:</b> {user_input}<br><br>
                <b>🤖 UniGuide:</b> {response}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.warning("Please enter a question.")
