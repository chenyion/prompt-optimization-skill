from jinja2 import Template
import json
from datetime import datetime

def generate_report(analysis: dict, optimized_prompts: list, test_results: dict, 
                    original_prompt: str, scenario: str) -> dict:
    """
    生成调优报告，包含：
    - 原始 Prompt 诊断
    - 优化版本对比
    - A/B 测试结果
    - 最优版本推荐
    """
    # 1. 筛选最优 Prompt（基于准确率+相关性+稳定性加权）
    best_prompt = None
    best_score = 0
    for prompt, metrics in test_results.items():
        score = metrics["accuracy"] * 0.5 + metrics["relevance"] * 0.3 + metrics["stability"] * 0.2
        if score > best_score:
            best_score = score
            best_prompt = prompt

    # 2. 生成结构化报告数据
    report_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scenario": scenario,
        "original_prompt": original_prompt,
        "analysis": analysis,
        "optimized_prompts": [
            {"version": f"v{i+1}", "prompt": p, "metrics": test_results[p]} 
            for i, p in enumerate(optimized_prompts)
        ],
        "best_prompt": best_prompt,
        "best_score": round(best_score, 2)
    }

    # 3. 生成 Markdown 格式报告（可选保存为文件）
    markdown_report = _render_markdown(report_data)
    
    return {
        "data": report_data,
        "markdown": markdown_report
    }

def _render_markdown(data: dict) -> str:
    """使用 Jinja2 渲染 Markdown 报告"""
    template = Template("""
# Prompt 调优报告
- **生成时间**: {{ data.timestamp }}
- **应用场景**: {{ data.scenario }}

## 1. 原始 Prompt 诊断
- 冗余度评分: {{ data.analysis.redundancy_score }}
- 清晰度评分: {{ data.analysis.clarity_score }}
- 歧义点: {% for point in data.analysis.ambiguity_points %}{{ point }}{% if not loop.last %}, {% endif %}{% endfor %}
- 优化建议: {% for suggestion in data.analysis.suggestions %}{{ suggestion }}{% if not loop.last %}, {% endif %}{% endfor %}

## 2. 优化版本对比
| 版本 | 准确率 | 相关性 | 稳定性 |
|------|--------|--------|--------|
{% for prompt in data.optimized_prompts %}| {{ prompt.version }} | {{ prompt.metrics.accuracy }} | {{ prompt.metrics.relevance }} | {{ prompt.metrics.stability }} |
{% endfor %}

## 3. 最优 Prompt
**综合评分**: {{ data.best_score }}