import streamlit as st

pages= st.navigation({
    "Project": [
        st.Page("pages\description.py", title="Description"),
        st.Page("pages\predict.py", title="Prediction" , icon="🏎️"),
    ]
})

pages.run()