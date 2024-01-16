import streamlit as st


name = st.text_input("Enter Your Name :- ")
father = st.text_input("Enter Your Father's Name :-")
Mother = st.text_input("Enter Your Mother's Name :- ")
Add = st.text_area("Enter Your Address:-")
email = st.text_input("Enter Your Email:-")


button = st.button("DONE")
if button:
    st.markdown(f"""
        Name: {name},
        father: {father},
        mother: {Mother},
        address: {Add},
        email: {email},
    """)