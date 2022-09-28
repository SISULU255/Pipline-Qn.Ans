import streamlit as st
from transformers import pipeline
st.title("KIITEC VIRTUAL ASSISTANT")
qa_model = pipeline("question-answering")
question = st.text_input('Question', 'where is kiitec found')
context = """KIITEC is a technical institution registered by NACTE (REG/EOS/027) based in Moshono, Arusha next to Masai Camp. The institute was founded in 2004 by French engineers and has thence contrived to produce the most competent technicians in the country. The institute is financed and supported by two NGO's The Foundation for Technical Education (FTE-Swiss) and Action Development Education International (ADEI-French). In 2004, ADEI's partner FTE built the Kilimanjaro International Institute of Telecommunications, Electronics and Computers (KIITEC) introducing state of the art teaching facilities to train technicians in Arusha, Tanzania. Following construction, ADEI joined FTE in its ambition to make change through technical education and has played a pivotal role in the on the ground education programming and training at KIITEC ever since. Today, KIITEC acts as the international training center where educators travel to from different corners of Africa to upgrade their skills. KIITEC is the home base for ADEI's international volunteers.

Resting on a 15-acre campus, KIITEC offers the most advanced targeted training technologies in the region. The innovative education model developed at KIITEC is based on a hands-on and student-centered approach to learning with full access to modern learning equipment simulating real world practical experiences. The training center is registered and accredited by the National Council for Technical Education (NACTE) and awards successful graduates with a 3-year National Technical Award Level Six (NTA-6) Diploma.
KIITEC’s specialized training programs include: Electronics & Telecommunication Engineering, Industrial Automation, Computer Engineering and Networking , Renewable Energies, Environmental Impact

Future training programs in development:  Biomedical , Avionics"""

qa_model(question = question, context = context)
## {'answer': 'İstanbul', 'end': 39, 'score': 0.953, 'start': 31}
