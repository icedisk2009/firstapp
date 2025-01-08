import streamlit as st
import random

st.title('나의 첫번째 앱')
st.text('\n\n')
st.write('안녕하세요. 저는 🍊🌵입니다')
st.write('이메일주소: t002@daejin.sen.hs.kr')

st.button("Reset", type="secondary")
if st.button('랜덤 숫자 생성'):
  st.write(random.randint(1,100))
else:
  st.write('잘가')


text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)

st.link_button("Go to gallery", "https://streamlit.io/gallery")

