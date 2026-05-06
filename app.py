import streamlit as st

st.title("AI CHATBOT")

user_input = st.text_input("Ask your question:")

if user_input:

    if user_input.lower() == "thermal":
        st.write("Thermal energy is the energy that comes from heat.")

    elif user_input.lower() == "kinetic":
        st.write("Kinetic energy is the energy of motion.")

    elif user_input.lower() == "potential":
        st.write("Potential energy is stored energy.")

    elif user_input.lower() == "chemical":
        st.write("Chemical energy is stored in chemical bonds.")

    else:
        st.write("Sorry, I don't understand that question.")

    st.write(f"You asked: {user_input}")