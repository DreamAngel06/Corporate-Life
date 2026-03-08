import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Please enter your full name:")
birth_year = st.text_input("What is your birth year?")
place = st.text_input("Where do you live?")
profession = st.text_input("What do you do professionally?")
your_thought = st.text_input("What do you think about your boss?")
your_choice = st.text_input(
    "If you have the chance to take a choice, what do you want to do with your boss?"
)

if st.button("Submit"):
    st.write(
        f"""
        I am **{name}**.  
        I was born in **{birth_year}**.  
        I live in **{place}**.  
        I work as **{profession}**.  
        I think my boss is **{your_thought}**.  
        If I had a choice: **{your_choice}**.
        """
    )