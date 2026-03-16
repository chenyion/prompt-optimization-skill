\# Prompt 工程自动化调优 \& 效果验证 Skill



\## 功能简介

针对大模型应用场景，自动分析现有 Prompt 的有效性、冗余度、歧义点，基于目标优化结构、少样本示例、思维链引导，生成多组备选并执行 A/B 测试，输出最优版本与调优报告。



\## 安装与配置

1\. 将本 Skill 放入 OpenClaw 工作目录的 `workspace/skills` 文件夹

2\. 安装依赖：在 Skill 根目录执行 `pip install -r requirements.txt`

3\. 配置大模型 API：在环境变量中设置 `OPENAI\_API\_KEY` 或 `ANTHROPIC\_API\_KEY`



\## 使用方法

\### 基础调用

在 OpenClaw 中输入：

