import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("AI Story Generator")

prompt = st.text_area("Enter  story prompt:")

if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Crafting your story... ✨"):
            result = generator(prompt, max_length=250, num_return_sequences=1)
            story = result[0]["generated_text"]
            st.subheader("Here's your story is Ready:")
            st.write(story)
