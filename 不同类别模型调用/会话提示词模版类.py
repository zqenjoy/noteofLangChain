from langchain_core.prompts import PromptTemplate ,ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.base import RunnableSerializable


# 普通的PromptTemplate 通过from_template只能传入一条模板消息
# ChatPromptTemplate 通过from_message方法,从列表list中获取多轮次会话作为聊天的基础模板

# MessagesPlaceholder作为占位符 不是静态固定消息，它能随着对话的进行不停地积攒，动态的

chat_propmt_template=ChatPromptTemplate.from_messages(
    [
        ("system","你是一位风景诗人，会作诗"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗"),
    ]
)


history_messages = [
    ("human","你来写一首唐诗"),
    ("ai","国破山河在，城春草木深"),
    ("human","好诗，再来一首"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

# prompt_text=chat_propmt_template.invoke({"history":history_messages}).to_string()
# print(prompt_text)
#
chat = ChatTongyi(model="qwen3-max")
# res = chat.invoke(prompt_text)
#
#
# print(res.content)
# print(type(res))



# 链式写法

chain:RunnableSerializable = chat_propmt_template | chat
# 这里chat_propmt_templated.invoke的输出是 chat的输入，所以可以形成链式机制

# res = chain.invoke({"history":history_messages})
# print(res.content)

res = chain.stream({"history":history_messages})

for chunk in res:
    print(chunk.content,end="",flush=True)
