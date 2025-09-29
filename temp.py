# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd


# # 手动从图中估计或假设的 RMSLE 值（可以替换为准确数据）
# pruning_levels = ['10%', '20%', '40%', '100%']
# x = np.arange(len(pruning_levels))

# # 假设的 RMSLE 值（估算或从图中读取）
# rmsle_citation = [0.84, 0.90, 0.95, 1.01]
# rmsle_venue = [0.78, 0.83, 0.85, 0.89]
# rmsle_institution = [0.83, 0.85, 0.84, 0.89]

# width = 0.25  # 每组bar的宽度

# # set font to Times New Roman and size 12
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 16

# fig, ax = plt.subplots(figsize=(10, 6))

# # 绘制三组柱状图
# bars1 = ax.bar(x - width, rmsle_citation, width, label='Citation > 20', color="#5CAB7D")
# bars2 = ax.bar(x, rmsle_venue, width, label='Venue not None', color="#DE6449")
# bars3 = ax.bar(x + width, rmsle_institution, width, label='Institution > 1000', color="#ABD0CE")


# # 设置标签和标题
# ax.set_ylabel('RMSLE', fontsize=16)
# ax.set_xlabel('Pruning Level', fontsize=16)
# ax.set_title('RMSLE vs. Pruning Level (Grouped by Subset)', fontsize=16)
# ax.set_xticks(x)
# ax.set_xticklabels(pruning_levels, fontsize=16)
# ax.set_ylim(0.5, 1.1)
# ax.legend(fontsize=16)

# plt.tight_layout()
# plt.savefig('rmsle.png', dpi=300)


import pandas as pd
import matplotlib.pyplot as plt

# CSV 文件路径
month_csv_path = "../../../Downloads/year.csv"  # 改成你的文件路径
year_csv_path = "../../../Downloads/month.csv"  # 改成你的文件路径
# 读取 CSV
df = pd.read_csv(month_csv_path)
df_year = pd.read_csv(year_csv_path)


# 检查数据
print(df.head())

# 绘制 loss 曲线
plt.figure(figsize=(8, 6))
# set font to Times New Roman and size 16
# plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20
print("Length of df:", len(df))
print("Length of df_year:", len(df_year))
plt.plot(df_year['Step'][0:29], df_year['lora-Qwen3-4B-Instruct-2507 - train_avg_loss'][0:29], marker='o', color='#e45756', label="Year")
plt.plot(df['Step'][0:29], df['lora-Qwen3-4B-Instruct-2507 - train_avg_loss'][0:29], marker='o', color='#72b7b2', label="Month")

# plt.title("Loss Curve", fontsize=16)
plt.xlabel("Step", fontsize=20)
plt.ylabel("Loss", fontsize=20)
plt.grid(axis='y', linestyle="--", alpha=0.6)
# set y grid false
# plt.yaxis.set_major_locator(ticker.MultipleLocator(0.01))
plt.legend()
plt.tight_layout()
# 保存图像
plt.savefig("loss_curve.png", dpi=300)

# 显示图像
# plt.show()


samples = [20, 200, 1000, 5000, 10000, "Avg"]
data_qwen_4b = [0.8099, 1.0834, 1.1008, 1.2212, 1.1297, 1.06900]
data_llama_3b = [1.1851, 1.0996, 1.1012, 1.11, 1.13, 1.12518]

plt.figure(figsize=(8, 6))
plt.plot(data_qwen_4b, marker='o', color='#72b7b2', label="Qwen-4B")
plt.plot(data_llama_3b, marker='o', color='#e45756', label="Llama-3B")
plt.xlabel("Step", fontsize=20)
plt.ylabel("Loss", fontsize=20)
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.xticks(range(len(samples)), samples, fontsize=20)
plt.ylim(0.0, 1.5)
plt.legend()
plt.tight_layout()
plt.savefig("loss_curve_qwen_4b_llama_3b.png", dpi=300)