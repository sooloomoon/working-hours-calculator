import datetime
from hours_calc import working_hours_calc
import streamlit as st

st.set_page_config(page_title='Working hours calculator')
st.title('Working Hours Calculator')

st.write('Time 1:')
date1 = st.date_input('Select a date', key='date1')
time1 = st.time_input('Select a time', key='time1', step=60)

st.markdown('***')

st.write('Time 2:')
date2 = st.date_input('Select a date', key='date2')
time2 = st.time_input('Select a time', key='time2', step=60)

t1 = datetime.datetime.combine(date1, time1)
t2 = datetime.datetime.combine(date2, time2)

st.markdown('***')

st.title(f'Working hours: {working_hours_calc(t1, t2)}')