# 会话history临时记忆功能
langchain提供了history，帮助模型再有历史记忆的情况下回答
- 基于RunnableWithMessageHistory 在原有链的基础上创建带有历史记忆功能的新链（新的runnable实例）提供功能
- 基于InMemoryChatMessageHistory 为历史记录提供内存存储   （实现存储）

两者搭配起来一起实现封装历史记录
```commandline
new_chain=    RunnableWithMessageHistory(
        some_chain,     #被附加了历史消息的runnable，通常是chain
        None,           # 获取指定会话ID的历史会话函数
        input_message="input",  #明湖输入消息在模板中的占位符
        history_message="chat_history"  # 声明历史消息在模板中的占位符
)
```

