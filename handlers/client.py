from telethon import TelegramClient 
from telethon.sessions import StringSession
import os

string = "BQCj3P8Al5uRgLVsDJb9QVmvcgR1-_CtrF_EGHxwnNP6-pdGY4xK4FiHw2R_tgTSBAEJ1fHcscrpIzMi62CxRWXMK4NCMuUJ71sm230sk1cOZjN_Krie1mzaKzy6Mwp4lQTE_6HP7M6T6y1yNjHAJXswo9_c4IapgZfRhnREteFAD5LNg7YvafcPicjpFNE8smygj2lGx_CkcpVYexHK4dlXYPH-cV4IY9ZJzqE3KZq2OIhwbBIkJxAIH24WqbzLGpAMrIIZPvYJ36qp07zuSWKJ4hqiHF8AkCFB9RImX9bTLJ8Y3pHWZxgledaIMZnKJOaRB-3utZ9LC86OhifVl2NDPn-o_QAAAAF-NhYaAQ"
api_id = "10738943"
api_hash = "da61e3a08b5ac78ce28b4a4cd854aeec"
news_api = "6ee5a3c2aa074546bc12b1e05a1da1e2"

# with TelegramClient(StringSession(), api_id, api_hash) as client:
#     session_str

client = TelegramClient(StringSession(string), api_id , api_hash)
