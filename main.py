# Import libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of time zones
Time_Zones = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]



# Flag image URLs mapping (using a free flag CDN)
flags = {
    "UTC": "https://flagcdn.com/w20/un.png",              # UN flag for UTC
    "Asia/Karachi": "https://flagcdn.com/w20/pk.png",     # Pakistan
    "America/New_York": "https://flagcdn.com/w20/us.png", # USA
    "Europe/London": "https://flagcdn.com/w20/gb.png",    # UK
    "Asia/Tokyo": "https://flagcdn.com/w20/jp.png",       # Japan
    "Australia/Sydney": "https://flagcdn.com/w20/au.png", # Australia
    "America/Los_Angeles": "https://flagcdn.com/w20/us.png", # USA
    "Europe/Berlin": "https://flagcdn.com/w20/de.png",    # Germany
    "Asia/Dubai": "https://flagcdn.com/w20/ae.png",       # UAE
    "Asia/Kolkata": "https://flagcdn.com/w20/in.png",     # India
}

st.title("Time Zone App")

# Multiselect for timezones
selected_timezone = st.multiselect("Select Timezones", Time_Zones, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone: 
    # Get and format current time
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    # Display flag and timezone in columns for better layout
    col1, col2 = st.columns([1, 5])  
    with col1:
        st.image(flags[tz], width=30)  # Display flag image
    with col2:
        st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between TimeZones")

current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From TimeZone", Time_Zones, index=0)
to_tz = st.selectbox("To TimeZone", Time_Zones, index=1)

# Convert time when button clicked
if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    # Display converted time with flag
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(flags[to_tz], width=30)
    with col2:
        st.success(f"Converted Time in {to_tz}: {converted_time}")