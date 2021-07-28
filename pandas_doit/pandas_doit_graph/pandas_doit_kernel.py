import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

ax = plt.subplots()  # sub를 만들겠단 뜻
ax = sns.kdeplot(data=tips['total_bill'],
                 data2=tips['tip'], shade=True)   # shade가 False이면 일반 등고선

ax.set_title('Kernel Density Plot')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

plt.show()
