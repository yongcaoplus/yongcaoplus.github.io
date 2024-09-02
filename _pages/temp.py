import matplotlib.pyplot as plt
import numpy as np


# Data from the provided image
models = ["MT-zs", "MT-ft", "mT5", "BLOOM", "ChatGLM2", "GPT-4", "Retrieval"]
chrF_zh_to_en = [29.1, 42.5, 31.6, 48.3, 41.8, 50.3, 37.8]
chrF_en_to_zh = [6.9, 28.3, 28.1, 11.5, 11.0, 21.9, 33.6]
cul_zh_to_en = [2.7, 4.3, 3.7, 2.8, 4.0, 6.0, 3.8]
cul_en_to_zh = [2.3, 3.2, 3.5, 3.0, 4.1, 4.4, 3.5]

# Removing mBART50 from the first chart
models_chrF = ["MT-zs", "MT-ft", "mT5", "BLOOM", "ChatGLM2", "GPT-4", "Retrieval"]
chrF_zh_to_en = [29.1, 42.5, 31.6, 48.3, 41.8, 50.3, 37.8]
chrF_en_to_zh = [6.9, 28.3, 28.1, 11.5, 11.0, 21.9, 33.6]

# Removing Human from the second chart
models_cul = ["MT-zs", "MT-ft", "mT5", "BLOOM", "ChatGLM2", "GPT-4", "Retrieval"]
cul_zh_to_en = [2.7, 4.3, 3.7, 2.8, 4.0, 6.0, 3.8]
cul_en_to_zh = [2.3, 3.2, 3.5, 3.0, 4.1, 4.4, 3.5]

x_chrF = np.arange(len(models_chrF))
x_cul = np.arange(len(models_cul))
width = 0.35

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(22, 10), dpi=300)

# set global text size 
font_size = 22
plt.rcParams.update({'font.size': font_size})
color_zh2en = '#87cdeb'
color_en2zh = '#f08080'
# ChrF Scores plot
rects1 = ax1.bar(x_chrF - width/2, chrF_zh_to_en, width, label='Chinese -> English', color=color_zh2en)
rects2 = ax1.bar(x_chrF + width/2, chrF_en_to_zh, width, label='English -> Chinese', color=color_en2zh)

# annotate scores
for i, v in enumerate(chrF_zh_to_en):
    ax1.text(i - width/2, v + 0.5, str(v), color='black', ha='center', va='bottom')

for i, v in enumerate(chrF_en_to_zh):
    ax1.text(i + width/2, v + 0.5, str(v), color='black', ha='center', va='bottom')

ax1.axis([-0.5, 6.5, 0, 70])
ax1.set_ylabel('ChrF Score', fontsize=font_size)
ax1.set_title('ChrF Scores for Our Models (Both direction)', fontsize=font_size)
ax1.set_xticks(x_chrF, fontsize=font_size)
ax1.set_xticklabels(models_chrF, fontsize=font_size)
ax1.tick_params(axis='y', labelsize=font_size)
# set legend position
ax1.legend(loc='upper left')

# CUL Scores plot
rects3 = ax2.bar(x_cul - width/2, cul_zh_to_en, width, label='Chinese -> English', color=color_zh2en)
rects4 = ax2.bar(x_cul + width/2, cul_en_to_zh, width, label='English -> Chinese', color=color_en2zh)

# annotate scores
for i, v in enumerate(cul_zh_to_en):
    ax2.text(i - width/2, v + 0.05, str(v), color='black', ha='center', va='bottom')

for i, v in enumerate(cul_en_to_zh):
    ax2.text(i + width/2, v + 0.05, str(v), color='black', ha='center', va='bottom')

ax2.axis([-0.5, 6.5, 0, 7])
ax2.set_ylabel('CUL Score', fontsize=font_size)
ax2.set_title('Culture Scores for Our Models (Both direction)', fontsize=font_size)
ax2.set_xticks(x_cul, fontsize=font_size)
ax2.tick_params(axis='y', labelsize=font_size)
ax2.set_xticklabels(models_cul, fontsize=font_size)
ax2.legend(loc='upper left')
fig.tight_layout()
plt.savefig('chrF_cul_scores.png')
# plt.show()
