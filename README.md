# 销售数据分析 Demo

一个最小的数据分析项目，用于演示 **WorkBuddy + GitHub** 的完整工作流。

## 项目结构
```
sales-analysis-demo/
├── data/             # 原始数据（sales.csv）
├── output/           # 分析产物（图表、报告）
├── generate_data.py  # 生成模拟数据
├── analyze.py        # 数据分析脚本
└── README.md
```

## 使用方法
```bash
# 1. 生成数据
python3.11 generate_data.py

# 2. 运行分析
python3.11 analyze.py
```

## 产出
- `output/sales_chart.png`：各产品线销售额 + 月度趋势图
- `output/report.md`：文字分析报告

## 依赖
- pandas
- matplotlib
