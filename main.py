import streamlit as st
from logic import generate_menu

st.title("Restaurant Name Generator")

cuisine = st.text_input("Enter the type of cuisine (e.g., Indian, Americian, Korean):")

if cuisine:
    result = generate_menu(cuisine)
    st.subheader("Restaurant Name:")
    st.write(result['restaurant_name'].strip())
    
    st.subheader("Suggested Menu:")
    st.write(result['menu'].strip())


if __name__ == "__main__":
    print(generate_menu("Indian"))