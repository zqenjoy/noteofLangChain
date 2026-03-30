from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史回应用户问题。对话历史：{chat_history},用户提问：{input}，请回答"
)

str_parser = StrOutputParser()
base_chain = prompt | model | str_parser

store={}  # 字典的key为session，value是InMemoryChatMessageHistory类对象
# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 创建新的链，对原有的链增加历史对话功能:自动附加历史消息
conversation_chain=RunnableWithMessageHistory(
    base_chain,   #被增强的原有链
    get_history,   # 通过回话id获取InMemoryChatMessageHistory类对象
    input_message_key='input',# 用户输入在模版中的占位符
    history_message_key='chat_history'    # 历史消息在模版中的占位符
)

if __name__ == '__main__':
    # 为当前程序添加sessionid
    session_config= {
        'configurable':{
            'session_id':'user_001'
        }
    }

    res=conversation_chain.invoke({'input':'小明有两只猫'},session_config)
    print('第一次运行',res)