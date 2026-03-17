# 解析器
像 JsonOutputParser 这类固定功能的解析器，
我们也可以自定义一些解析器，加入到链式调用当中

## RunnableLambda类
是langchain内置的，将普通的函数转换为runnable接口实例

```commandline

RunnableLambda(lambda ai_msg:{"name":ai_msg})

# ai_msg是作为参数传入自定义方法中

```





