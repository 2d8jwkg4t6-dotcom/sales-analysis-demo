"""生成模拟销售数据（可复现，随机种子固定）。"""
import csv
import random

random.seed(42)

PRODUCTS = ["产品A", "产品B", "产品C"]
REGIONS = ["华东", "华南", "华北", "西南"]

rows = []
for month in range(1, 10):  # 2026年1-9月
    for day in range(1, 29):  # 每月28天
        for product in PRODUCTS:
            for region in REGIONS:
                base = {"产品A": 5000, "产品B": 3200, "产品C": 6800}[product]
                seasonal = 1 + 0.15 * (month - 5) ** 2 / 16  # 年中略有旺季
                noise = random.uniform(0.75, 1.25)
                sales = round(base * seasonal * noise, 2)
                quantity = random.randint(10, 80)
                rows.append([f"2026-{month:02d}-{day:02d}", product, region, sales, quantity])

with open("data/sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "产品线", "地区", "销售额", "销量"])
    writer.writerows(rows)

print(f"已生成 {len(rows)} 行模拟销售数据 -> data/sales.csv")
