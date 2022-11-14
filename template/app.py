import streamlit as st
from st_event_selectioninterface import EventSelectionInterface
import json
f =open('text.json')
event=json.load(f)
st.markdown("--")
EventSelectionInterface(event =event)