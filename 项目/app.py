import time

import streamlit as st
from agent.react_agent import ReactAgent

# 标题
# st.title('🤖智能扫地机器人客服')

import streamlit as st

# 设置页面配置（浏览器标签页显示的文字和图标）
st.set_page_config(page_title="扫地机助手", page_icon="🤖")

# 主界面标题
st.title('🤖 智能扫地机器人客服')

# 提示语
st.caption("我是扫地机器人专业智能客服，需要我为您做些什么？")

# 侧边栏
with st.sidebar:
    st.header("配置选项")
    st.info("当前模式：ReAct Agent")

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
        res_stream= st.session_state['agent'].execute_stream(prompt)


        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.01)
                    yield char
        st.chat_message('assistant').write_stream(capture(res_stream,response_msg))
        st.session_state['message'].append({'role':"assistant","content":response_msg[-1]})
        st.rerun()

