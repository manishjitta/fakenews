import streamlit as st

from bardapi import Bard
import os

os.environ["_BARD_API_KEY"] = "Xwjlv90Q_Olh03XdBQcTmXfWENmbBPTlVuGz-rIUtDQ1GlCXhqVMrLd5CDXsmR3TEgh61g."

st.title("FAKE NEWS DETECTION")

news = st.text_input("Enter the news: ")
news+="YES or NO. write very shortly."

result = Bard().get_answer(str(news))['content']

st.write(result)

if len(result)>0:
    if "No" and 'no' not in result:
        st.write("The News is True")
    else:
        st.write("The News is Fake")
