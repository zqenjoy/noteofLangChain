import time

import streamlit as st
from agent.react_agent import ReactAgent
from agent_pro.chat_page import message

# 标题
st.title='智能扫地机器人客服'
st.divider()
# 防止频繁创建实例
if 'agent' not in st.session_state:
    st.session_state['agent']=ReactAgent()

# 保存历史聊天记录
if 'message' not in st.session_state:
    st.session_state['message']=[]

for message in st.session_state['message']:
    st.chat_message(message['role']).write(message['content'])



#  用户输入提示词
prompt = st.chat_input()

if prompt:
    st.chat_message('user').write(prompt)
    st.session_state['message'].append({'role':"user","content":prompt})

    response_msg = []
    with st.spinner('思考中……'):
        res_stream= st.session_state['agent'].excute_stream(prompt)


        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.01)
                    yield char
        st.chat_message('assistant').write_stream(capture(res_stream,response_msg))
        st.session_state['message'].append({'role':"assistant","content":response_msg[-1]})
        st.rerun()

