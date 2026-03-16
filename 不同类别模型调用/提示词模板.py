from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# prompt_template =  PromptTemplate.from_template("我有一个男朋友叫{hisName}，他是一位{job}，帮忙给他取个网名，请简单回答。")
# prompt_text = prompt_template.format(hisName='吴汉斌',job="老师") #注入变量
# # print(prompt_text)
# model = Tongyi(model="qwen-max")
#
# res=model.invoke(input=prompt_text)
#
# print(res)



print('---------fewshot模版--------------')

example_template = PromptTemplate.from_template('单词：{word},反义词：{antonym}')
example_data = [
    {"word":'上',"antonym":'下'},
    {"word":"大","antonym":"小"}
]

few_shot_prompt = FewShotPromptTemplate( #写代码时注意这里不要额外加一些缩进，会导致缩进格式错误
example_prompt=example_template,
examples=example_data,
prefix='给出给定词的反义词，有如下示例',
suffix="基于以上的示例，{input_word}的反义词是？",
input_variables=['input_word']
 )
prompt_text=few_shot_prompt.invoke(input={"input_word":'左'}).to_string()

print('prompt_text',prompt_text)


model = Tongyi(model="qwen-max")
print(model.invoke(input=prompt_text))

