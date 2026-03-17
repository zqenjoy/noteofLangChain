from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import  ChatTongyi
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser() #不需要传参，即可拿到实例对象
model = ChatTongyi(model="qwen3-max")
prompt_template = PromptTemplate.from_template("我叫{name},刚出生了一个{gender}宝，请帮忙起一个名字")

chain = prompt_template |model|parser |model|parser
res =chain.invoke({"name":"周青","gender":'男'})
print(res,)
print(type(res))