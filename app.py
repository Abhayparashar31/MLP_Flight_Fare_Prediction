import streamlit as st
import pickle
import numpy as np
import datetime
import pandas as pd

### Loading Model
model = pickle.load(open('predict_flight_fare_V3_86.pkl','rb'))

## Web App Design Text
st.title('Flight Fare Prediction 🛫')

## Departure Details
st.subheader('Departure Details')

## Date_of_Journey (Departure Date)
# Current Day/Month/Year	
day = datetime.date.today().day
month = datetime.date.today().month
year = datetime.date.today().year

d_o_j = st.date_input("Departure Date" , datetime.date(year,month,day))
if d_o_j is not None:
    Date_of_Journey_Day = d_o_j.day     
    Date_of_Journey_Month = d_o_j.month 


## Departure Time
dep_time = st.time_input('Your Departure Time From The Source', datetime.time(12, 30))
Dep_Time_Hour = dep_time.hour         
Dep_Time_Minute = dep_time.minute      

## Airline
Available_Airlines = ['Air Asia','IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet']
Airline = st.selectbox("Choose Your Airline For The Trip",Available_Airlines)
encoded_airline = [1 if Airline==airline else 0 for airline in Available_Airlines[1:]]

## Source
Available_Sources = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
Source = st.selectbox('Source For The Journey',Available_Sources)
encoded_source = [1 if Source==source else 0 for source in Available_Sources[1:]]

## Destination
Available_Destinations = ['Banglore','New Delhi','Cochin', 'Kolkata', 'Delhi', 'Hyderabad']
Destination = st.selectbox('Destination of The Journey',Available_Destinations)
encoded_destination = [1 if Destination==destination else 0 for destination in Available_Destinations[1:]]

## Total Stops
total_stops = st.selectbox('Number of Stops Between Source and Destination',[0,1,2,3,4])

## Duration of The Flight
duration = st.time_input('Duration of The Flight', datetime.time(2, 30))
Duration_Hour = duration.hour
Duration_Minute = duration.minute

## Arrival Time
ar_time = st.time_input('Expected Time of Arrival At The Destination', datetime.time(12, 30))
Arrival_Time_Hour = ar_time.hour             
Arrival_Time_Minute  = ar_time.minute        


## Print Departure Details
# st.write('### Trip Details')
# st.write('Date of Journey:', datetime.date(d_o_j.year,d_o_j.month,d_o_j.day).strftime('%d/%m/%Y'))
# st.write(f'Departure Time From The {Source} is', datetime.time(Dep_Time_Hour,Dep_Time_Minute).strftime('%I:%M %p'))

# st.write('Airline For The Trip: ',Airline)
# st.write('Encoded Airline: ',encoded_airline)

# st.write('Source For The Trip: ',Source)
# st.write('Encoded Source: ',encoded_source)

# st.write('Destination of The Trip: ',Destination)
# st.write('Encoded Source: ',encoded_destination)

# st.write(f'Total Stops Between Source and {Destination}: ',total_stops)
# st.write(f'Expected Arrival Time To Reach At P{Destination}',datetime.time(Arrival_Time_Hour,Arrival_Time_Minute).strftime('%I:%M %p'))

new_entry = [total_stops,Date_of_Journey_Day,Date_of_Journey_Month,Arrival_Time_Hour,Arrival_Time_Minute,Dep_Time_Hour,Dep_Time_Minute,Duration_Hour,Duration_Minute]
new_entry.extend(encoded_airline)
new_entry.extend(encoded_source)
new_entry.extend(encoded_destination)

st.write('Encoded Data')
st.write(pd.DataFrame([new_entry]))
st.write(pd.DataFrame([new_entry]).shape)

data = pd.DataFrame([new_entry])

Generate_pred = st.button("Predict Flight Fare")
if Generate_pred:
    prediction = model.predict(data)
    st.write('The Fare For Your Upcoming Will Be Close To: ',int(prediction[0]),'INR')

if st.checkbox("Know About The Creator"):
    st.write(''' ***Streamlit App Developed By Abhay Parashar***  ''') 
    st.write(''' **Find Him On**''')
    st.write(''' [**Medium**](https://abhayparashar31.medium.com/) | [**LinkedIN**](https://www.linkedin.com/in/abhayparashar31/) | [**GitHub**](https://github.com/abhayparashar31/)''')
    st.write('Sayonara !!!')
    