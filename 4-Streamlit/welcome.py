import streamlit as st

#st.set_page_config(page_title="Description", layout="wide")

pages= st.navigation({
    "Project": [
        st.Page("pages/description.py", title="Description"),
        st.Page("pages/predict.py", title="Prediction" , icon="🏎️"),
    ]
})

pages.run()