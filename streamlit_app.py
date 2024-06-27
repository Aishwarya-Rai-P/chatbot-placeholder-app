import streamlit as st
from urllib.parse import urlencode

def main():
    name = st.query_params.get('name', '')
    query = st.query_params.get('query', '')

    st.title(f"Hello, {name}!")
    st.write(f"Your search query is - {query}. Please give me more details about your search query:")
    
    response = st.text_area("Enter your response:")
    if st.button("Submit"):
        params = urlencode({'response': response})
        flask_url = f"http://127.0.0.1:5000/result?{params}"
        st.markdown(f"[Click here to return to the main app]({flask_url})")
        st.success("Response submitted! Click the link above to return to the main app.")

if __name__ == "__main__":
    main()
