import streamlit as st
from PIL import Image
image = Image.open('kiitec logo.png')
st.image(image,  width=100)
st.title("KIITEC VIRTUAL ASSISTANT")
st.write("Sorry! am still learning but ask any Question about kiitec i may help you now")
from transformers import pipeline
qa_pipeline = pipeline(
  "question-answering",
  model="csarron/bert-base-uncased-squad-v1",
  tokenizer="csarron/bert-base-uncased-squad-v1"
)
predictions = qa_pipeline({
  'context': """
KIITEC is a technical institution registered by NACTE (REG/EOS/027) based in Moshono, Arusha next to Masai Camp.\n
\nFee structure and Mode of Payment for Diploma Programmes,for first semister is 	695,000Tsh and for second semister is 625,000Tsh, Fee in the second semester can be paid in two installments before the end of the semester,The fees should be paid through the BANK of  ABSA and the Account number is  002-4001687 the Account Name is  KIITEC Ltd.\n
\n my name is Sisulu
"""
#Fee structure and Mode of Payment for Diploma Programmes,for first semister is 	695,000Tsh and for second semister is 625,000Tsh, Fee in the second semester can be paid in two installments before the end of the semester,The fees should be paid through the BANK of  ABSA and the Account number is  002-4001687 the Account Name is  KIITEC Ltd.

,
  'question':st.text_input('Question', 'what is KIITEC')

})

st.write(predictions)

