import streamlit as st

st.title("🎈 Aqualoop")
st.write(
    "Ayo kita mulai mendeteksi tangki! [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
import streamlit as st

st.balloons()
