import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


def plot_embedding_dim():
    dims = [128, 192, 256, 384, 512, 768, 1024]
    
    # Balanced Accuracy and nDCG
    balanced_accuracy = {
        'GTE-Large': [77.95, 78.20, 78.34, 78.43, 78.46, (78.49 + 78.46)/2, 78.49],
        'GTE-Base':  [77.69, 77.96, 77.96, 78.06, 78.07, 78.07, None],
        'SPECTER2':  [78.02, 78.14, 78.20, 78.26, 78.29, 78.25, None],
        'TF-IDF':    [73.93, 74.27, 74.67, 74.93, 74.95, 75.11, 75.08],
    }
    ndcg = {
        'GTE-Large': [84.32, 85.02, 85.45, 85.75, 85.85, (85.91 + 85.85)/2, 85.91],
        'GTE-Base':  [83.73, 84.56, 84.99, 85.28, 85.34, 85.35, None],
        'SPECTER2':  [83.19, 83.65, 83.79, 83.88, 83.93, 83.93, None],
        'TF-IDF':    [80.27, 81.88, 82.86, 84.00, 84.93, 85.77, 86.35],
    }
    colors = {
        'GTE-Large': 'tab:blue',
        'GTE-Base': 'skyblue',
        'SPECTER2': 'coral',
        'TF-IDF': 'crimson',
    }

    fig, axs = plt.subplots(2, 1, figsize=(6, 8), sharex=True)

    for method, values in balanced_accuracy.items():
        axs[0].plot(dims, values, marker='o', label=method, color=colors[method])
    axs[0].set_title('Balanced Accuracy vs Embedding Dimensionality', fontsize=12, fontweight='bold')
    axs[0].set_ylabel('Balanced Accuracy (%)', fontsize=10)
    axs[0].grid(True)
    axs[0].legend(fontsize=9)
    axs[0].set_ylim(73, 79)

    for method, values in ndcg.items():
        axs[1].plot(dims, values, marker='o', label=method, color=colors[method])
    axs[1].set_title('nDCG vs Embedding Dimensionality', fontsize=12, fontweight='bold')
    axs[1].set_xlabel('Embedding Dimensionality', fontsize=10)
    axs[1].set_ylabel('nDCG', fontsize=10)
    axs[1].grid(True)
    axs[1].legend(fontsize=9)
    axs[1].set_ylim(80, 87)

    axs[1].set_xticks(dims)
    axs[1].set_xticklabels([str(d) for d in dims])

    plt.tight_layout()
    plt.savefig('pca_plots.png', dpi=300, bbox_inches='tight')


def plot_retention():
    # 模拟数据
    days = list(range(31))
    users = [
    537, 2399, 3451, 4240, 4473, 4567, 4684, 5183, 5625, 5997,
    6286, 6505, 6560, 6594, 6771, 6925, 7101, 7272, 7423, 7464,
    7495, 7622, 7735, 7872, 8001, 8107, 8136, 8162, 8252, 8364, 8460
]


    total_users = 21000  # Hypothetical total user base

    # total_users = sum(users)  # 假设总用户数

    # 绘图
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(days, users, marker='o', color='#4ea1d3', linewidth=2, label='User Number')
    # plt.bar(days, users, color='#4ea1d3', alpha=0.7)

    # 标题和标签
    ax.set_title('User Retention Over the Last 30 Days', fontsize=13, fontweight='bold')
    ax.set_xlabel('Days Ago', fontsize=12)
    ax.set_ylabel('Active Users(% of Total Users)', fontsize=12)

    # 设置 Y 轴为双格式（用户数和百分比，换行显示）
    y_ticks = np.linspace(0, max(users), 5).astype(int)
    y_labels = [f"{y}\n({y / total_users * 100:.1f}%)" for y in y_ticks]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)

    # 网格
    ax.grid(True, linestyle='-', alpha=0.6)
    plt.legend(loc='lower right', fontsize=14)
    plt.tight_layout()
    plt.savefig('user_retention.png', dpi=300, bbox_inches='tight')
    # plt.show()


def plot_paper_number():
    # 类别和对应的论文数（大致估算自图像）
    categories = [
            "Physics", "Mathematics", "Computer Science", "Biology",
        "Vision and Graphics", "Machine Learning", "Robotics and Control",
        "Language", "Statistics", "Medicine", "Audio and Speech",
        "Economics", "Chemistry", "Other"
    ]
    paper_counts = [
        1495974, 549731, 399018, 391051,
        233168, 224669, 145469,
        106133, 93277, 70792, 56566,
        35675, 32807, 6
    ]

    fig, ax = plt.subplots(figsize=(6, 6))
    bars = ax.bar(categories, paper_counts, color='#79a8a9', alpha=1.0, zorder=2)

    ax.set_title('Papers Received by Category', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Papers', fontsize=12)
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=45, ha='right')

    # 设置稀疏的 y 轴网格线
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6))
    ax.grid(which='major', axis='y', linestyle='-', alpha=0.6, zorder=0)

    # 设置稀疏的 x 轴网格线（每隔3个）
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(which='major', axis='x', linestyle='-', alpha=0.6, zorder=1)

    plt.tight_layout()

    # 保存或显示
    plt.savefig('papers_by_category.png', dpi=300)
    # plt.show()



def plot_user_distribution():
    # 原始数据
    labels = [
        'Computer \nVision\n and Graphics', 'Machine \nLearning', 'Robotics \nand Control',
        'Language', 'Statistics', 'Physics', 'Biology', 'Mathematics', 'Other'
    ]
    sizes = [29, 29, 11, 10, 5, 4, 4, 3, 5]
    colors = [
        '#4ea1d3', '#c8c8a9', '#79a8a9', '#fd999a', '#f9cdad',
        '#a79c8e', '#d68189', '#c7c7c7', '#ffec8b'
    ]

    # 按照大小排序（从大到小）
    # sorted_data = sorted(zip(sizes, labels, colors), key=lambda x: -x[0])
    # sizes, labels, colors = zip(*sorted_data)

    # 绘图
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.0f%%',
        startangle=100,
        counterclock=False,  # 顺时针
        pctdistance=0.85,
        textprops={'fontsize': 12}
    )

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    ax.set_title('Users by Field of Interest', fontsize=15, fontweight='bold', y=0.96)
    ax.axis('equal')

    plt.tight_layout()
    plt.savefig('user_interest_donut_chart.png', dpi=300)
    # plt.show()


def plot_user_satisfaction():
    # 准备数据
    satisfaction_levels = ['very good', 'good', 'medium', 'bad', 'very bad']
    ml =       [300, 200, 80, 20, 5]
    cv =       [350, 150, 50, 10, 3]
    robotics = [100, 50, 30, 5, 2]

    # Stack data
    x = np.arange(len(satisfaction_levels))
    width = 0.6

    # 右图数据
    tools = ['Google\nScholar', 'Preprint\nservers', 'Social\nMedia', 'Other']
    tool_usage = [800, 500, 480, 40]

    # 绘图
    fig, axs = plt.subplots(1, 2, figsize=(6, 3))
    # colors = {
    #     'GTE-Large': 'tab:blue',
    #     'GTE-Base': 'skyblue',
    #     'SPECTER2': 'coral',
    #     'TF-IDF': 'crimson',
    # }
    # 左图：满意度分布
    axs[0].bar(x, ml, label='Machine Learning', color='#fc9d9a')
    axs[0].bar(x, cv, bottom=ml, label='Computer Vision', color='#f9cdad')
    axs[0].bar(x, robotics, bottom=np.array(ml)+np.array(cv), label='Robotics and Control', color='#4ea1d3')
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(satisfaction_levels, rotation=45)
    axs[0].set_ylabel('number of users')
    axs[0].set_title('Satisfaction')
    axs[0].legend(fontsize=8, loc='upper right', frameon=True)
    axs[0].set_axisbelow(True)
    axs[0].grid(True, linestyle='-', alpha=0.6)
    axs[0].set_ylim(0, 840)

    # 右图：其他工具使用情况
    axs[1].bar(tools, tool_usage, color='skyblue', label='All Domains')
    axs[1].set_title('Other tools')
    axs[1].set_axisbelow(True)
    axs[1].grid(True, linestyle='-', alpha=0.6)
    axs[1].set_ylim(0, 840)
    axs[1].legend(fontsize=8, loc='upper right', frameon=True)
    plt.tight_layout()
    plt.savefig('user_study_results.png', dpi=300)

if __name__ == "__main__":
    plot_retention()
    plot_paper_number()
    plot_user_distribution()
    plot_embedding_dim()
    plot_user_satisfaction()