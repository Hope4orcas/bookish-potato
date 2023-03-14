import streamlit as st 
import requests
import json

sub=st.text_input("subreddit")

if st.button("Generate meme"):
  url="https://meme-api.com/gimme/"+sub
  response = requests.get(url)
  data = json.loads(response.text)
  meme = data["url"]
  st.title(data["title"])
  
  st.markdown ("![Un meme hermoso]("+meme+")")
