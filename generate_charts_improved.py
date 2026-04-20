import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 时间点标签
time_points = ['初始', '72h干热', '72h紫外', '144h干热', '144h紫外', '216h干热', '216h紫外', '288h干热', '288h紫外']
x_indices = np.arange(len(time_points))

# 无媒染剂组数据
group_A = {
    'pH': [4.50, 5.03, 5.36, 5.26, 5.50, 5.46, 6.12, 5.84, 6.62],
    'L': [49.78, 48.23, 52.53, 45.79, 55.48, 47.93, 58.30, 45.93, 61.15],
    'a': [7.97, 8.39, 7.77, 7.68, 6.85, 8.70, 6.41, 8.56, 5.85],
    'b': [17.36, 17.35, 17.44, 16.21, 16.85, 17.58, 16.71, 17.01, 16.45],
    'dE': [None, 1.57, 2.76, 4.19, 5.81, 2.01, 8.69, 3.91, 11.60]
}

# 明矾组数据
group_B = {
    'pH': [4.02, 4.59, 5.18, 4.78, 5.41, 4.74, 6.26, 5.12, 6.96],
    'L': [48.27, 46.91, 52.30, 46.03, 54.17, 46.45, 57.48, 45.33, 60.43],
    'a': [7.84, 8.03, 7.54, 8.04, 6.81, 8.15, 6.37, 8.25, 5.85],
    'b': [16.52, 16.22, 16.81, 16.30, 16.31, 16.21, 16.34, 16.10, 16.23],
    'dE': [None, 1.40, 4.05, 2.28, 6.00, 1.89, 9.33, 3.00, 12.33]
}

# 蓝矾组数据
group_C = {
    'pH': [4.82, 5.05, 5.71, 5.07, 5.90, 5.50, 6.56, 5.63, 7.10],
    'L': [46.24, 45.47, 47.93, 45.44, 49.14, 45.10, 50.67, 44.70, 52.12],
    'a': [6.78, 7.08, 7.06, 7.25, 6.91, 7.31, 7.05, 7.55, 7.11],
    'b': [14.09, 14.03, 15.96, 14.25, 16.58, 14.68, 18.03, 14.76, 19.28],
    'dE': [None, 0.83, 2.58, 0.94, 3.82, 1.39, 5.94, 1.85, 7.85]
}

# 绿矾组数据
group_D = {
    'pH': [4.57, 4.98, 6.24, 5.20, 5.48, 5.34, 6.34, 5.66, 6.79],
    'L': [40.66, 40.61, 43.30, 40.64, 43.32, 41.31, 45.09, 41.30, 46.42],
    'a': [4.67, 5.59, 5.36, 6.02, 5.31, 6.08, 5.75, 6.75, 6.07],
    'b': [10.17, 11.76, 12.50, 12.80, 13.20, 13.00, 14.99, 14.32, 16.50],
    'dE': [None, 1.84, 3.62, 2.96, 4.12, 3.23, 6.64, 4.69, 8.67]
}

def create_group_chart(group_data, group_name, filename):
    """为单个媒染剂组创建图表"""
    plt.close('all')  # 关闭所有图形
    fig, ax = plt.subplots(figsize=(14, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    # 左轴：pH和Lab值
    ax.set_xlabel('老化时间', fontsize=12)
    ax.set_ylabel('pH/L/a/b值', fontsize=12, color=colors[0])
    
    line1, = ax.plot(x_indices, group_data['pH'], marker='o', linewidth=2.5, label='pH', 
                     color=colors[0], markersize=8)
    line2, = ax.plot(x_indices, group_data['L'], marker='s', linewidth=2.5, label='L', 
                     color=colors[1], markersize=8)
    line3, = ax.plot(x_indices, group_data['a'], marker='^', linewidth=2.5, label='a', 
                     color=colors[2], markersize=8)
    line4, = ax.plot(x_indices, group_data['b'], marker='d', linewidth=2.5, label='b', 
                     color=colors[3], markersize=8)
    
    # 右轴：ΔE
    ax_r = ax.twinx()
    ax_r.set_ylabel('ΔE值', fontsize=12, color=colors[4])
    non_none_dE = [(i, val) for i, val in enumerate(group_data['dE']) if val is not None]
    if non_none_dE:
        dE_x = [i for i, val in non_none_dE]
        dE_y = [val for i, val in non_none_dE]
        line5, = ax_r.plot(dE_x, dE_y, marker='*', linewidth=2.5, label='ΔE', 
                          color=colors[4], markersize=10, linestyle='--')
    
    ax.set_xticks(x_indices)
    ax.set_xticklabels(time_points, rotation=45, ha='right', fontsize=10)
    ax.set_title(f'{group_name}老化周期变化', fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # 合并图例
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax_r.get_legend_handles_labels()
    legend = ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', 
                       fontsize=11, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"已生成: {filename}")

# 生成每个媒染剂组的图表
print("开始生成各媒染剂组图表...")
create_group_chart(group_A, '无媒染剂组', '图3-2_无媒染剂组老化周期变化.png')
create_group_chart(group_B, '明矾组', '图3-3_明矾组老化周期变化.png')
create_group_chart(group_C, '蓝矾组', '图3-4_蓝矾组老化周期变化.png')
create_group_chart(group_D, '绿矾组', '图3-5_绿矾组老化周期变化.png')

# 图5: 288h干热老化ΔE值对比
plt.close('all')
fig5, ax5 = plt.subplots(figsize=(12, 7))
mordants = ['无媒染', '明矾', '蓝矾', '绿矾']
dE_dry = [3.91, 3.00, 1.85, 4.69]
colors_bar = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

bars = ax5.bar(mordants, dE_dry, color=colors_bar, alpha=0.85, edgecolor='black', 
                linewidth=1.5, width=0.6)

# 在柱子上显示数值
for bar, val in zip(bars, dE_dry):
    height = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2., height,
            f'{val}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax5.set_xlabel('媒染剂类型', fontsize=13)
ax5.set_ylabel('ΔE值', fontsize=13)
ax5.set_title('四种媒染剂在288h干热老化后的ΔE值对比', fontsize=15, fontweight='bold', pad=20)
ax5.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.savefig('图3-6_干热老化ΔE值对比.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("已生成: 图3-6_干热老化ΔE值对比.png")

# 图6: 288h紫外老化ΔE值对比
plt.close('all')
fig6, ax6 = plt.subplots(figsize=(12, 7))
dE_uv = [11.60, 12.33, 7.85, 8.67]

bars = ax6.bar(mordants, dE_uv, color=colors_bar, alpha=0.85, edgecolor='black', 
                linewidth=1.5, width=0.6)

for bar, val in zip(bars, dE_uv):
    height = bar.get_height()
    ax6.text(bar.get_x() + bar.get_width()/2., height,
            f'{val}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax6.set_xlabel('媒染剂类型', fontsize=13)
ax6.set_ylabel('ΔE值', fontsize=13)
ax6.set_title('四种媒染剂在288h紫外老化后的ΔE值对比', fontsize=15, fontweight='bold', pad=20)
ax6.grid(True, alpha=0.3, axis='y', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.savefig('图3-7_紫外老化ΔE值对比.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("已生成: 图3-7_紫外老化ΔE值对比.png")

def create_phtrend_chart(pH_data_dict, title, filename):
    """创建pH值变化趋势图"""
    plt.close('all')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    time_points_simple = ['初始', '72h', '144h', '216h', '288h']
    x_simple = np.arange(len(time_points_simple))
    
    colors_line = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    markers = ['o', 's', '^', 'd']
    labels = ['无媒染', '明矾', '蓝矾', '绿矾']
    
    for i, (label, data) in enumerate(pH_data_dict.items()):
        ax.plot(x_simple, data, marker=markers[i], linewidth=2.5, label=label, 
                color=colors_line[i], markersize=8)
    
    ax.set_xlabel('老化时间', fontsize=13)
    ax.set_ylabel('pH值', fontsize=13)
    ax.set_title(title, fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x_simple)
    ax.set_xticklabels(time_points_simple)
    ax.legend(loc='best', fontsize=12, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"已生成: {filename}")

# pH值趋势数据
pH_dry = {'无媒染': [4.50, 5.03, 5.26, 5.46, 5.84],
          '明矾': [4.02, 4.59, 4.78, 4.74, 5.12],
          '蓝矾': [4.82, 5.05, 5.07, 5.50, 5.63],
          '绿矾': [4.57, 4.98, 5.20, 5.34, 5.66]}

pH_uv = {'无媒染': [4.50, 5.36, 5.50, 6.12, 6.62],
         '明矾': [4.02, 5.18, 5.41, 6.26, 6.96],
         '蓝矾': [4.82, 5.71, 5.90, 6.56, 7.10],
         '绿矾': [4.57, 6.24, 5.48, 6.34, 6.79]}

create_phtrend_chart(pH_dry, '四种媒染剂干热老化pH值变化趋势对比', 
                     '图3-8_干热老化pH值变化趋势.png')
create_phtrend_chart(pH_uv, '四种媒染剂紫外老化pH值变化趋势对比', 
                     '图3-9_紫外老化pH值变化趋势.png')

print("\n所有图表已生成完成！")