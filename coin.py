import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from PIL import Image

import os
import matplotlib.font_manager as fm

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
plt.rc('font', family='NanumSquareRound')
mpl.rcParams['axes.unicode_minus'] = False

st.title("	:punch: 동전 던지기")

if "n" not in st.session_state:
    st.session_state["n"] = 0
if "head" not in st.session_state:
    st.session_state["head"] = 0
if "tail" not in st.session_state:
    st.session_state["tail"] = 0
if "x" not in st.session_state:
    st.session_state["x"] = np.array([])
if "y" not in st.session_state:
    st.session_state["y"] = np.array([])              

troll = Image.open('troll.jpg')
st.image(troll, width = 200)
input_n = st.number_input("동전을 몇 번 던질까?", min_value=1, max_value=50000)


if st.button("던지기"):
    if input_n == 1557 :
        st.write("왜 이렇게 빨리 끝내나요 IG!!")
    for i in range(input_n):
        coin = random.randrange(2)
        st.session_state["n"] += 1
        if coin == 0:
            st.session_state["head"] += 1
        else:
            st.session_state["tail"] += 1
        if st.session_state["n"] < 100 :
            st.session_state["x"] = np.append(st.session_state["x"], st.session_state["n"])
            st.session_state["y"] = np.append(st.session_state["y"], st.session_state["head"]/st.session_state["n"])
        elif st.session_state["n"] < 1000 :
            if st.session_state["n"]%10 == 0 :
                st.session_state["x"] = np.append(st.session_state["x"], st.session_state["n"])
                st.session_state["y"] = np.append(st.session_state["y"], st.session_state["head"]/st.session_state["n"])
        elif st.session_state["n"] < 10000 :
            if st.session_state["n"]%100 == 0 :
                st.session_state["x"] = np.append(st.session_state["x"], st.session_state["n"])
                st.session_state["y"] = np.append(st.session_state["y"], st.session_state["head"]/st.session_state["n"])
        else :
            if st.session_state["n"]%1000 == 0 :
                st.session_state["x"] = np.append(st.session_state["x"], st.session_state["n"])
                st.session_state["y"] = np.append(st.session_state["y"], st.session_state["head"]/st.session_state["n"])

    st.write("동전을 {}회 던졌습니다.".format(input_n))
    st.write("지금까지 던진 횟수는 총 {}회입니다.".format(st.session_state["n"]))
    st.write("앞면이 나온 횟수는 총 {}, 뒷면이 나온 횟수는 총 {} 입니다.".format(st.session_state["head"], st.session_state["tail"]))
    st.write("앞면이 나온 횟수의 상대도수는 {:.4f}, 뒷면이 나온 횟수의 상대도수는 {:.4f} 입니다.".format(st.session_state["head"]/st.session_state["n"], st.session_state["tail"]/st.session_state["n"]))

if st.button("Reset"):
    st.session_state["n"] = 0
    st.session_state["head"] = 0
    st.session_state["tail"] = 0   
    st.session_state["x"] = np.array([])
    st.session_state["y"] = np.array([])

st.write("")    
st.divider()
st.write("")

st.write("동전을 던진 횟수에 따른 앞면에 나온 횟수의 상대도수의 변화를 그래프로 관찰해봅시다. :eyes:")

if st.button("그래프 그리기") : 
    fig = plt.figure()
    plt.plot(st.session_state["x"], st.session_state["y"])
    plt.title('상대도수 그래프', fontsize=18)
    plt.xlabel('던진 횟수', fontsize=15)
    plt.ylabel('앞면 상대도수', fontsize=15)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.axhline(y=0.5, color='r', linewidth=1)
    st.pyplot(fig)