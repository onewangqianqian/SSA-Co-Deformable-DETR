import matplotlib.pyplot as plt

# 准备数据
x = [0,1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y = [0,0.529, 0.641, 0.598,0.586, 0.592,0.608,0.648,0.667,0.703,0.711,0.723,0.729,0.826,0.829,0.828,0.830,0.821,0.824,0.822,0.821,0.821,0.821,0.820,0.815]
y2 = [0, 0, 0, 0, 0,0,0,0,0,0,0,12,13,14,15,16,17,18,19,20,21,22,23,24]
y3=[0, 0, 0, 0, 0,0,0,0,0,0,0,12,13,14,15,16,17,18,19,20,21,22,23,24]

x_hidden = x[12:]
y_hidden = y[12:]
# plt.figure(facecolor='lightblue')
# 绘制折线图
plt.plot(x, y,marker='o',label='Line 1')
# plt.plot(x, y2,marker='o',label='Line 2')
# plt.plot(x, y3,marker='o',label='Line 2')
# plt.fill_between(x, y, color='lightblue', alpha=0.3)
# plt.fill_between(x, y2, color='lightgreen', alpha=0.3)
plt.xticks(x, x)
# 添加标题和标签
plt.title('Line Chart Example')
plt.xlabel('epoch')
plt.ylabel('bbox_mAP')
plt.legend()
# 显示网格线
# plt.grid(True)

# 显示图形
plt.show()
