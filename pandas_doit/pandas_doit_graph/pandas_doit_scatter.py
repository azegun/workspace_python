import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)


def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(
    x=tips['total_bill'],
    y=tips['tip'],
    s=tips['size'] * 10,
    c=tips['sex_color'],
    alpha=0.5
)

axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
axes1.set_xlabel('Total Bill')
axes1.set_ylabel('Tip')
plt.show()

