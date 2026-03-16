def run_prompt_optimization(prompt: str, scenario: str, test_cases: list = None):
    """完整流程：分析→优化→测试→报告"""
    # 1. 诊断
    analysis = analyze_prompt(prompt)
    # 2. 优化
    optimized_prompts = optimize_prompt(prompt, analysis, scenario)
    # 3. A/B 测试
    test_results = ab_test(optimized_prompts, test_cases)
    # 4. 生成报告
    report = generate_report(analysis, optimized_prompts, test_results)
    return report