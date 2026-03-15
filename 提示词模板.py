from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

prompt_template =  PromptTemplate.from_template("我有一个男朋友叫{hisName}，他是一位{job}，帮忙给他取个网名，请简单回答。")
prompt_text = prompt_template.format(hisName='吴汉斌',job="老师") #注入变量
# print(prompt_text)
model = Tongyi(model="qwen-max")

res=model.invoke(input=prompt_text)

print(res)
