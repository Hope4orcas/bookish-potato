import streamlit as st 
import requests
import json

if st.button("Generate meme"):
  url="https://meme-api.com/gimme/wholesomememes"
  response = requests.get(url)
  data = json.loads(response.text)
  meme = ["url"]
  st.title(data["title"])
  
st.markdown ("![Un meme hermoso]("meme")")