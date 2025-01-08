import streamlit as st


st.title('나의 첫번째 앱')
st.text('\n\n')
st.write('안녕하세요. 저는 🍊🌵입니다')
st.write('이메일주소: t002@daejin.sen.hs.kr')

st.button("Reset", type="secondary")
if st.button('Say hello'):
  st.write('안녕, 오늘도 좋은 하루')
else:
  st.wirte('잘가')

