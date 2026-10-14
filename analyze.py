"""销售数据分析：汇总、可视化、生成报告。"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 中文字体处理（直接注册字体文件，避免名称匹配失败）
import matplotlib.font_manager as fm
for _f in ["/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
           "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"]:
    fm.fontManager.addfont(_f)
plt.rcParams["font.family"] = "Noto Sans CJK JP"  # ttc 首个 face，含完整中文字形
plt.rcParams["axes.unicode_minus"] = False

os.makedirs("output", exist_ok=True)
df = pd.read_csv("data/sales.csv")

# 1. 各产品线销售额汇总
by_product = df.groupby("产品线")["销售额"].sum().sort_values(ascending=False)

# 2. 月度趋势
df["月份"] = df["日期"].str[:7]
by_month = df.groupby("月份")["销售额"].sum()

# 3. 各地区汇总
by_region = df.groupby("地区")["销售额"].sum().sort_values(ascending=False)

# ---- 图表 ----
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(by_product.index, by_product.values, color=["#d9534f", "#f0ad4e", "#5bc0de"])
axes[0].set_title("各产品线销售额")
axes[0].set_ylabel("销售额（元）")

axes[1].plot(by_month.index, by_month.values, marker="o", color="#d9534f")
axes[1].set_title("月度销售额趋势")
axes[1].set_ylabel("销售额（元）")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("output/sales_chart.png", dpi=120)
plt.close()

# ---- 文字报告 ----
total = df["销售额"].sum()
top_product = by_product.index[0]
top_region = by_region.index[0]
peak_month = by_month.idxmax()
growth = (by_month.iloc[-1] - by_month.iloc[0]) / by_month.iloc[0] * 100

report = f"""# 销售数据分析报告

## 总体概览
- 统计周期：{df['日期'].min()} ~ {df['日期'].max()}
- 总销售额：**¥{total:,.0f}**
- 总订单量：{df['销量'].sum():,} 件

## 关键发现
1. **最畅销产品线**：{top_product}（¥{by_product.iloc[0]:,.0f}）
2. **表现最佳地区**：{top_region}（¥{by_region.iloc[0]:,.0f}）
3. **销售高峰月份**：{peak_month}（¥{by_month.max():,.0f}）
4. **首末月增长率**：{growth:.1f}%

## 各产品线明细
{by_product.to_string()}

## 各地区明细
{by_region.to_string()}
"""

with open("output/report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("分析完成，已生成：")
print("  - output/sales_chart.png（可视化图表）")
print("  - output/report.md（分析报告）")
