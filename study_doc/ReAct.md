# 什么是ReAct
是大模型智能体的核心思考与行动框架，全程reasoning + Acting（推理和行动），是让agent像人类一样思考问题-》制定策略-》执行行动-》验证结果的关键逻辑

# react范式
- 思考reasoning：分析问题，判断现有信息是否足够，明确下一步
- 行动action ：执行思考阶段指定的策略，调用工具获取信息
- 观察：获取行动的结果，判断返回值为下一轮思考提供信息

# middleware中间件
中间件通过hooks钩子实现拦截，自定义中间件可以简单的使用装饰器来定义

 ## 节点式钩子
- before_agent: agent执行前拦截
- after_agent:
- before_model: 模型执行前拦截
- after_model:
## 针对工具和模型的包装式钩子
- wrap_model_call：每个模型调用时拦截
- wrap_tool_call:每个工具调用时拦截
