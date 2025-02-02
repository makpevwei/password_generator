import streamlit as st 
from password_generator_cli import generate_password
from file_operations import read_passwords_from_file, write_password_to_file


st.title("Password Generator App")
st.write("Generate a secure password it to a file")

n_letters = st.number_input("Number of letters", min_value=0,  value=3)
n_numbers = st.number_input("Number of numbers", min_value=0, value=3)
n_symbols = st.number_input("Number of symbols", min_value=0, value=3)

if st.button("Generate Passord"):
    password = generate_password(n_letters,n_numbers,n_symbols)
    
    write_password_to_file(password)
    st.info("Password saved to file")
    
if st.checkbox("Show Saved Passwords"):
    passwords = read_passwords_from_file()
    
    if passwords:
        st.write("Saved Passwords:")
        st.markdown("\n".join([f"{password}" for password in passwords]))
    else:
        st.warning("No passwords saved yet")