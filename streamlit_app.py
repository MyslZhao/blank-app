import streamlit as st
QUES = ["早餐","中餐","晚餐"]

#html样式设计
st.markdown("""<style>
            div[role = "radiogroup"] ~ div p{
            font-size: 20px !important;
            font-weight:bold;
            }
            </style>""",
            unsafe_allow_html=True)


st.title("父母性别预测")
st.markdown(
    "_通过科学算法预测父母性别_"
    )

frame = st.empty()

with frame.container():
    

st.markdown("""
你的父亲是：  
## 男性
你的母亲是：  
## 女性
""")

