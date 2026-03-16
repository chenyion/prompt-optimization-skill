def analyze_prompt(prompt: str) -> dict:
    """分析 Prompt 的冗余度、歧义点、指令清晰度"""
    # 实现逻辑：
    # 1. 冗余度：统计重复词汇、无效修饰（如“非常非常重要”）
    # 2. 歧义点：检测模糊表述（如“尽快”“大概”）
    # 3. 指令清晰度：检查是否包含“角色、任务、要求、输出格式”四要素
    return {
        "redundancy_score": 0.8,  # 0-1，越高越冗余
        "ambiguity_points": ["表述‘尽快’未明确时间"],
        "clarity_score": 0.6,     # 0-1，越高越清晰
        "suggestions": ["补充输出格式要求", "明确时间限制"]
    }