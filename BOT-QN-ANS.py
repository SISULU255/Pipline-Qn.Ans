import streamlit as st
from transformers import pipeline
st.title("KIITEC VIRTUAL ASSISTANT")
qa_model = pipeline("question-answering")
question = st.text_input('Question', 'where is kiitec found')
context = """KIITEC is a technical institution registered by NACTE (REG/EOS/027) based in Moshono, Arusha next to Masai Camp. The institute was founded in 2004 by French engineers and has thence contrived to produce the most competent technicians in the country. The institute is financed and supported by two NGO's The Foundation for Technical Education (FTE-Swiss) and Action Development Education International (ADEI-French). In 2004, ADEI's partner FTE built the Kilimanjaro International Institute of Telecommunications, Electronics and Computers (KIITEC) introducing state of the art teaching facilities to train technicians in Arusha, Tanzania. Following construction, ADEI joined FTE in its ambition to make change through technical education and has played a pivotal role in the on the ground education programming and training at KIITEC ever since. Today, KIITEC acts as the international training center where educators travel to from different corners of Africa to upgrade their skills. KIITEC is the home base for ADEI's international volunteers.

Resting on a 15-acre campus, KIITEC offers the most advanced targeted training technologies in the region. The innovative education model developed at KIITEC is based on a hands-on and student-centered approach to learning with full access to modern learning equipment simulating real world practical experiences. The training center is registered and accredited by the National Council for Technical Education (NACTE) and awards successful graduates with a 3-year National Technical Award Level Six (NTA-6) Diploma.
KIITEC’s specialized training programs include: Electronics & Telecommunication Engineering, Industrial Automation, Computer Engineering and Networking , Renewable Energies, Environmental Impact
Future training programs in development:  Biomedical , Avionics.
ELECTRICAL AND INDUSTRIAL AUTOMATION ENGINEERINg this  programme focuses on combined skills that are in Electrical and Industrial Automation engineering. it has been noted that Tanzania has about 81% of population (43,621,499) own and uses mobile phone for their daily activities in 2018 compared to 61% (27,607,822) in 2013. Also number of electricity connection in Tanzania mainland has increased to 73% in 2018 compared to 13% in 2007. Furthermore, the country has been constructing stiegler-gorge hydropower plant that is expected to be finalized in 42 months and should have the capacity to produce 2,115 MW by April 2022, dramatically increasing the country’s current power production capacity of 1,553.96 MW to 3668.96MW. Therefore, improvement airports, construction of standard gauge railways, establishment of TV and Radio stations, shall increase of industries and extension of National grid to rural community will increase the demand of technician in this cadre. The programme will admit students with ordinary level of education with any two passes in science subjects.
requirements of ELECTRICAL AND INDUSTRIAL AUTOMATION ENGINEERINg is Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects
or
Possession of a National Vocational Award (NVA) Level III in Electrical, Electronics, Telecommunication, Mechanical and related field offered by VETA and a Certificate of Secondary Education Examination (CSEE) with at least two passes.
Diploma in Telecommunication Engineering,this course reflects the role of a technician with a range of telecommunications skills who can install and maintain enterprise network in emerging and converging technologies, optical and wireless equipment for high speed broadband network infrastructure, internet protocol (IP), MPLS based network telecommunications equipment, IP based networks in home networks and small and medium enterprises, telecommunications access network cabling and infrastructure, systems and basic customer premises equipment, assess installation requirements of converging voice, video and data IP networks, plan and performing installations, test installed equipment and fault find.
requirements of Diploma in Telecommunication Engineering is Possession of a Certificate of Secondary Education Examinations (CSEE) with a minimum of FOUR passes of which TWO must be among the following subjects: Mathematics, Physics / Engineering science, Biology and Chemistry; excluding religious subjects
My name is SISULU and my creator is WALTER RICHARD.





"""

st.write(qa_model(question = question, context = context))
## {'answer': 'İstanbul', 'end': 39, 'score': 0.953, 'start': 31}
