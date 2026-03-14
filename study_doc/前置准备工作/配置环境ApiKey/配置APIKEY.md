# 为什么api要配置在系统内？

    apikey明文显示在代码中，有很大的隐患
    通过环境变量隐藏apikey

# 配置环境变量

## windows系统

- 快捷键：windows+S 打开搜索框“高级系统设置”
- 点击“高级”->“环境变量”->“用户变量”->“新建”
- 变量名：OPENAI_API_KEY
- 变量值：你的apikey

- 变量名：DASHSCOPE_API_KEY
- 变量值：你的apikey
- 点击“确定”

## mac系统

- 打开mac自带的终端软件，输入：open .zshrc 打开配置文件
- export OPENAI_API_KEY=你的apikey
- export DASHSCOPE_API_KEY=你的apikey
- 配置完成后重启pycharm
