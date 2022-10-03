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
\nFee structure and Mode of Payment for Diploma Programmes,for first semister is 695,000Tsh can be paid in two installments before the end of the semester, and for second semister is 625,000Tsh, Fee in the second semester can be paid in two installments before the end of the semester\n
\nThe fees should be paid through the BANK of  ABSA and the Account number is  002-4001687 the Account Name is  KIITEC Ltd.\n
\nmy name is Sisulu\n
\nWALTER RICHARD made me\n
\nThe institute was founded in 2004 by French engineers and has thence contrived to produce the most competent technicians in the country. The institute is financed and supported by two NGO's The Foundation for Technical Education (FTE-Swiss) and Action Development Education International (ADEI-French). In 2004, ADEI's partner FTE built the Kilimanjaro International Institute of Telecommunications, Electronics and Computers (KIITEC) introducing state of the art teaching facilities to train technicians in Arusha, Tanzania.\n
\nFollowing construction, ADEI joined FTE in its ambition to make change through technical education and has played a pivotal role in the on the ground education programming and training at KIITEC ever since. Today, KIITEC acts as the international training center where educators travel to from different corners of Africa to upgrade their skills. \n
\nResting on a 15-acre campus, KIITEC offers the most advanced targeted training technologies in the region. The innovative education model developed at KIITEC is based on a hands-on and student-centered approach to learning with full access to modern learning equipment simulating real world practical experiences. The training center is registered and accredited by the National Council for Technical Education (NACTE) and awards successful graduates with a 3-year National Technical Award Level Six (NTA-6) Diploma.\n
\nKIITEC’s specialized training programs include: Electronics & Telecommunication Engineering , Industrial Automation , Computer Engineering and Networking , Renewable Energies, Environmental Impact .\n
\nFuture training programs in development: Biomedical ,  Avionics.\n 
\nADMISSION REQUIREMENTS of ELECTRONICS AND TELECOMMUNICATION ENGINEERING, Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects or Possession of a National Vocational Award (NVA) Level III in Electrical, Electronics, Telecommunication, Mechanical and related field offered by VETA and a Certificate of Secondary Education Examination (CSEE) with at least two passes.\n
\nADMISSION REQUIREMENTS of ELECTRICAL AND INDUSTRIAL AUTOMATION ENGINEERING,Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects or Possession of a National Vocational Award (NVA) Level III in Electrical, Electronics, Telecommunication, Mechanical and related field offered by VETA and a Certificate of Secondary Education Examination (CSEE) with at least two passes.\n
\nADMISSION REQUIREMENTS of ELECTRICAL AND COMPUTER ENGINEERING PROGRAMME,Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects or Possession of a National Vocational Award (NVA) Level III in Electrical, Electronics, Telecommunication, Mechanical and related field offered by VETA and a Certificate of Secondary Education Examination (CSEE) with at least two passes.\n
\nADMISSION REQUIREMENTS of ELECTRICAL AND RENEWABLE ENERGY ENGINEERING,Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects or Possession of a National Vocational Award (NVA) Level III in Electrical, Electronics, Telecommunication, Mechanical and related field offered by VETA and a Certificate of Secondary Education Examination (CSEE) with at least two passes.\n
\nKIITEC STUDENTS wear uniforms , uniforms that are worn are light blue shirts and dark blue sweeters ,dark blue skirt and dark blue trouser.\n
\nKiitec has Vision of become a leading provider of quality technical education and training to empower the youth of Tanzania and Eastern Africa region.\n
\nKiitec has Mission of  provide quality hands-on technical training for students in ICTs, Electrical, Renewable Energies, Industrial Automation and the related disciplines, as well as to conduct quality research, and consultancy in these fields.\n
\nAlso Kiitec has Mission of promoting the development and usage of modern technology that meets national, regional, and international needs and standards through skills and practical oriented training.\n
\nKiitec has values: Hard-work and excellence ,Honesty ,Respect ,Responsibility ,Lifelong learning ,Innovation and creativity\n
\nFor contact info of kiitec Phone: +255 27 250 4384, Mobile: +255 757 845 118 , Email: info@kiitec.ac.tz P.O.Box 3172 Arusha, Tanzania.


 



"""
,
  'question':st.text_input('Question', 'what is KIITEC')

})

st.write(predictions)

