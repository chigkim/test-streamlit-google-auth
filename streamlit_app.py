import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

if not st.user.get("is_logged_in", False):
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}!")
    st.user
    st.button("Log out", on_click=st.logout)