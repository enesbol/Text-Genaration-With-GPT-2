import streamlit as st
from transformers import pipeline

text=st.text_input('Initial text')

len = st.slider("Length of essay", 50, 600, step=20)
num = st.slider("Number of essays to be created", 1, 5, step=1)


generator = pipeline('text-generation', model = 'gpt2')
a = generator( text , max_length = len, num_return_sequences=num)

st.write(a[0]['generated_text'])
