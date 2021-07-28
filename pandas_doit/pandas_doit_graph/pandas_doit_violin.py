import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)
ax = plt.subplots()
colors = ['red', 'blue']
sns.set_palette(sns.color_palette(colors))

# hue는 그룹별로 색을 지정
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
ax.set_title('Violineplot Plot')

plt.show()


