from datetime import date
import numpy as np
import streamlit as st

@st.cache_data
def bio_compat(your_birth, other_birth):
    T = {'Emotional':28, 'Intellectual':33, 'Physical':23}
    t = your_birth - other_birth
    cycle_data = {}
    for cycle, value in T.items():
        form = np.cos(np.pi * t.days / value)
        cycle_data[cycle] = abs(form)
        form_final = form * 100
        st.write(f"{cycle} Cycle Percent Compatibility: {abs(form_final):.2f}")
    #return cycle_data, np.array([*cycle_data.values()]).mean() * 100
    cycle_mean = round(np.array([*cycle_data.values()]).mean() * 100,2)
    st.write(f'Overall Compatibility: {cycle_mean} Percent')
  
## -- MAIN DISPLAY CODE -- ##
st.title('Biorhythm Compatibility Checker')

birth_date = st.date_input('Select your birthdate',
                           #value=date(2000,1,1),
                           min_value=date(1900,1,1),
                           max_value=date.today(),
                           key='your_birhdate',
                           format='YYYY-MM-DD')
other_date = st.date_input('Select other birthdate',
                           #value=date(2000,1,1),
                           min_value=date(1900,1,1),
                           max_value=date.today(),
                           key='other_birthdate',
                           format='YYYY-MM-DD')

bio_compat(birth_date,other_date)
