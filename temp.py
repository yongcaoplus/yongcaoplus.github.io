import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 手动从图中估计或假设的 RMSLE 值（可以替换为准确数据）
pruning_levels = ['10%', '20%', '40%', '100%']
x = np.arange(len(pruning_levels))

# 假设的 RMSLE 值（估算或从图中读取）
rmsle_citation = [0.84, 0.90, 0.95, 1.01]
rmsle_venue = [0.78, 0.83, 0.85, 0.89]
rmsle_institution = [0.83, 0.85, 0.84, 0.89]

width = 0.25  # 每组bar的宽度

# set font to Times New Roman and size 12
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制三组柱状图
bars1 = ax.bar(x - width, rmsle_citation, width, label='Citation > 20', color="#5CAB7D")
bars2 = ax.bar(x, rmsle_venue, width, label='Venue not None', color="#DE6449")
bars3 = ax.bar(x + width, rmsle_institution, width, label='Institution > 1000', color="#ABD0CE")


# 设置标签和标题
ax.set_ylabel('RMSLE', fontsize=16)
ax.set_xlabel('Pruning Level', fontsize=16)
ax.set_title('RMSLE vs. Pruning Level (Grouped by Subset)', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(pruning_levels, fontsize=16)
ax.set_ylim(0.5, 1.1)
ax.legend(fontsize=16)

plt.tight_layout()
plt.savefig('rmsle.png', dpi=300)
