# 概念
「将组件串联，上一个组件的输出作为下一个组件的辑原理，这也是链式调用的核心价值:实现数据的自动化
入」是LangChain链(尤其是| 管道链)的核心工作

## 核心前提
Runnable子类对象才能入链(以及callable、Mapping接口子类对象也可加入(后续了解用的不多)我们目前所学习到的组件，均是Runnable接口的子类，如下类的继承关系:

# 工作机制
流转与组件的协同工作，如下。
```commandline
chain = propmt_template | model

```
- 通过|链接提示词模版对象和模型对象
- 返回值chain对象是runnableSerializable：是runnable的直接字类，也是绝大多数组件的父类
- 通过链调用invoke或者stream进行阻塞执行或者流式执行

组成的链在执行上：必须是  上一个组件的输出作为下一个组件的输入的关系