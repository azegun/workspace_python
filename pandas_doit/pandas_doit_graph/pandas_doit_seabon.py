import matplotlib.pyplot as plt
import seaborn as sns

anscombe = sns.load_dataset('anscombe')
print(anscombe, type(anscombe))

dataset1 = anscombe[anscombe['dataset'] == 'I']
dataset2 = anscombe[anscombe['dataset'] == 'II']
dataset3 = anscombe[anscombe['dataset'] == 'III']
dataset4 = anscombe[anscombe['dataset'] == 'IV']
# plt.plot(dataset1['x'], dataset1['y'], 'o')  # 'o' 가 있으면 point로 그래프 표시
# plt.show()
fig = plt.figure()

axes1 = fig.add_subplot(2, 2, 1)   # 2,2 라는 4개의 그래프가 생성되는데 그중에 n번쨰
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.plot(dataset1['x'], dataset1['y'], 'o')
axes2.plot(dataset2['x'], dataset2['y'], 'o')
axes3.plot(dataset3['x'], dataset3['y'], 'o')
axes4.plot(dataset4['x'], dataset4['y'], 'o')

fig.suptitle('Anscombe Data')  #  큰 프레임의 이름을 지정하는 메서드
fig.tight_layout()    # layout이 겹치지 않게 하는것

axes1.set_title('I')
axes2.set_title('II')
axes3.set_title('III')
axes4.set_title('IV')

plt.show()
