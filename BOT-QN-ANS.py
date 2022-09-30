import streamlit as st
from PIL import Image
image = Image.open('kiitec logo.png')
from transformers import pipeline
st.image(image,  width=100)
st.title("KIITEC VIRTUAL ASSISTANT")
st.write("Sorry! am still learning but ask any Question about kiitec i may help you now")
qa_pipeline = pipeline(
  "question-answering",
  model="csarron/bert-base-uncased-squad-v1",
  tokenizer="csarron/bert-base-uncased-squad-v1"
)

predictions = qa_pipeline({
  'context': """
KIITEC is a technical institution registered by NACTE (REG/EOS/027) based in Moshono, Arusha next to Masai Camp. The institute was founded in 2004 by French engineers and has thence contrived to produce the most competent technicians in the country. The institute is financed and supported by two NGO's The Foundation for Technical Education (FTE-Swiss) and Action Development Education International (ADEI-French). In 2004, ADEI's partner FTE built the Kilimanjaro International Institute of Telecommunications, Electronics and Computers (KIITEC) introducing state of the art teaching facilities to train technicians in Arusha, Tanzania. Following construction, ADEI joined FTE in its ambition to make change through technical education and has played a pivotal role in the on the ground education programming and training at KIITEC ever since. Today, KIITEC acts as the international training center where educators travel to from different corners of Africa to upgrade their skills. KIITEC is the home base for ADEI's international volunteers.
Resting on a 15-acre campus, KIITEC offers the most advanced targeted training technologies in the region. The innovative education model developed at KIITEC is based on a hands-on and student-centered approach to learning with full access to modern learning equipment simulating real world practical experiences. The training center is registered and accredited by the National Council for Technical Education (NACTE) and awards successful graduates with a 3-year National Technical Award Level Six (NTA-6) Diploma.
KIITEC’s specialized training programs include: Electronics & Telecommunication Engineering, Industrial Automation, Computer Engineering and Networking,  Renewable Energies, Environmental Impact.Future training programs in development are Biomedical and Avionics
To reach kiitec adminstration CONTACT INFO
P.O.Box 3172 Arusha, Tanzania.
Phone: +255 27 250 4384 
Mobile: +255 757 845 118
Email: info@kiitec.ac.tz
 
My name is SISULU and my creator is WALTER RICHARD.
my name is SISULU and WALTER RICHARD is the one buit me.
"""
,
  'question':st.text_input('Question', 'what is kiitec')
})

st.write(predictions)
