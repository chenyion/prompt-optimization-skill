def optimize_prompt(prompt: str, analysis: dict, scenario: str = "general") -> list:
    """基于诊断结果生成多组优化版本"""
    optimized_prompts = []
    # 实现逻辑：
    # 1. 结构优化：补充“角色-任务-要求-格式”框架
    # 2. 少样本示例：根据场景自动注入 1-2 个示例
    # 3. 思维链引导：添加“先思考...再执行...”指令
    optimized_prompts.append(optimized_v1)  # 结构优化版
    optimized_prompts.append(optimized_v2)  # +少样本
    optimized_prompts.append(optimized_v3)  # +思维链
    return optimized_prompts