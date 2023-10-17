import streamlit as st

st.set_page_config(
    page_title="LARA",
    page_icon="👋",
)

st.sidebar.success("Access different types of assistance above.")


# Set the title of the app
st.title('LARA: Life Aid Recovery Assistant')

# Introduction text
st.write('''
LARA is designed to assist individuals with dementia with daily tasks and emergencies. 
This is a proof-of-concept application to demonstrate its potential features and functionalities.
''')


# Placeholder items to demonstrate other features of LARA
st.subheader('Future Features of LARA')
st.write('''
- **Real-time Geolocation**: Track the user's current location and provide directions to get back home.
- **Emergency Contact**: Automatically notify emergency contacts if the user seems lost for an extended period.
- **Safety Zones**: Define areas where the user frequently visits and get alerted if they wander off too far.
- **Memory Aids**: Provide photos or familiar landmarks to help the user recognize their surroundings.
''')

# Interactive button to demonstrate potential interactions
if st.button('Find my current location'):
    st.write("Fetching current location... (Placeholder)")

# Placeholder map showing a predefined location (can be replaced with real-time geolocation in the future)
st.subheader('Map of Your Current Location')
map_data = {
    'lat': [37.573890],  # Placeholder latitude
    'lon': [-122.378562]  # Placeholder longitude 
}
st.map(map_data)

# Footer with more information or contacts
st.write('''
---
For more information or support, please [contact us](#).
''')
