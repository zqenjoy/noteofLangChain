import time
from rag import RagService
import streamlit as st
import config_data as config


# 标题
st.title('智能客服agent')
st.divider()

# 引入rag服务
if "rag" not in st.session_state:
 st.session_state["rag"] = RagService()

# stream自身的刷新机制：当页面有元素变化时，页面会重新跑一遍
# 所以需要缓存历史对话记录
if "message" not in st.session_state:
    st.session_state["message"] = [{"role":"assistant","content":"你好，我是智能客服，有什么剋一帮助你的？"}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])


# 在页面最下方提供用户的输入框
prompt = st.chat_input()


if prompt:
    # 在页面输出用户的提问
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role":"user","content":prompt})

    with st.spinner('AI思考中……'):
        st.session_state["rag"].chain.invoke({"input":prompt},config.session_config)
        st.chat_message('assistant').write('你也好呀')
        st.session_state["message"].append({"role": "assistant", "content": "你也好呀"})


