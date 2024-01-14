import math
import numpy as np
import pickle
import streamlit as st
st.set_page_config(page_title='T20I Score Predictor',layout="centered")
filename="T20I.pkl"
model = pickle.load(open(filename,'rb'))
st.markdown("<h1 style='text-align: center; color: white;'> T20I score predictor </h1><text>Made with love by Aditya Khambete</text>", unsafe_allow_html=True)


with st.expander("Description"):
    st.info("""ML model made by me for my WiDS project which calculates the predicted score of a given T20 match between top 10 teams
    
 """)
batting_team= st.selectbox('Select the Batting Team ',('India', 'South Africa', 'Australia','New Zealand','Pakistan','Afghanistan','Sri Lanka','England','Bangladesh','West Indies'))
prediction_array = []
if batting_team == 'India':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif batting_team == 'South Africa':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif batting_team == 'Australia':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif batting_team == 'New Zealand':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif batting_team == 'Pakistan':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif batting_team == 'Afghanistan':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif batting_team == 'Sri Lanka':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif batting_team == 'England':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif batting_team == 'Bangladesh':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif batting_team == 'West Indies':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]
bowling_team= st.selectbox('Select the Bowling Team ',('India', 'South Africa', 'Australia','New Zealand','Pakistan','Afghanistan','Sri Lanka','England','Bangladesh','West Indies'))
if bowling_team==batting_team:
    st.error('How can be bowling team same as batting team, use some brain bro')
if bowling_team == 'India':
    prediction_array = prediction_array + [1,0,0,0,0,0,0,0,0,0]
elif bowling_team == 'South Africa':
    prediction_array = prediction_array + [0,1,0,0,0,0,0,0,0,0]
elif bowling_team == 'Australia':
    prediction_array = prediction_array + [0,0,1,0,0,0,0,0,0,0]
elif bowling_team == 'New Zealand':
    prediction_array = prediction_array + [0,0,0,1,0,0,0,0,0,0]
elif bowling_team == 'Pakistan':
    prediction_array = prediction_array + [0,0,0,0,1,0,0,0,0,0]
elif bowling_team == 'Afghanistan':
    prediction_array = prediction_array + [0,0,0,0,0,1,0,0,0,0]
elif bowling_team == 'Sri Lanka':
    prediction_array = prediction_array + [0,0,0,0,0,0,1,0,0,0]
elif bowling_team == 'England':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,1,0,0]
elif bowling_team == 'Bangladesh':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,1,0]
elif bowling_team == 'West Indies':
    prediction_array = prediction_array + [0,0,0,0,0,0,0,0,0,1]
col1, col2 = st.columns(2)
with col1:
    overs = st.number_input('Enter the Current Over',min_value=5.1,max_value=19.5,value=5.1,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('You should go back to the prehistoric days where over was more than 6 balls, T20I is clearly not for you, and I respect that')
with col2:
    runs = st.number_input('Enter Current runs',min_value=0,max_value=354,step=1,format='%i')
wickets =st.slider('Enter Wickets fallen till now',0,9)
wickets=int(wickets)
col3, col4 = st.columns(2)
with col3:
    runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs',min_value=0,max_value=runs,step=1,format='%i')
with col4:
    wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs',min_value=0,max_value=wickets,step=1,format='%i')
prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5,wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)
if st.button('Predict Score'):
    my_prediction = int(round(predict[0]))
    x=f'PREDICTED MATCH SCORE : {my_prediction-5} to {my_prediction+5}' 
    st.success(x)
