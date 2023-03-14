import streamlit as st 
import requests
import json

if st.button("Generate meme"):
  url="https://meme-api.com/gimme/cats"
  response = requests.get(url)
  data = json.loads(response.text)
  meme = data["url"]
  st.title(data["title"])
  
  st.markdown ("![Un meme hermoso]("+meme+")")
