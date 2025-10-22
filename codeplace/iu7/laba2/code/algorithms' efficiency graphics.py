import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def graphics(data):
    df = pd.DataFrame(data)

    df_melted = df.melt(id_vars='sequence_length', 
                        var_name='Алгоритм', 
                        value_name='Время (мс)')

    sns.set_style("whitegrid")
    sns.set_palette("husl", 2)

    plt.figure(figsize=(12, 8))

    lineplot = sns.lineplot(data=df_melted, 
                        x='sequence_length', 
                        y='Время (мс)', 
                        hue='Алгоритм',
                        style='Алгоритм',
                        markers={'Рекурсивный алгоритм': 'o', 'Итеративный алгоритм': 's'},
                        dashes=False,
                        markersize=8,
                        linewidth=2.5)

    plt.title('Сравнение эффективности алгоритмов обработки числовой последовательности', 
            fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Последовательность длины n', fontsize=12, fontweight='bold')
    plt.ylabel('Время выполнения (мс)', fontsize=12, fontweight='bold')

    plt.legend(title='Алгоритмы', title_fontsize=12, fontsize=11)

    plt.grid(True, alpha=0.3)

    last_size = df['sequence_length'].iloc[-1]
    for algo in ['Рекурсивный алгоритм', 'Итеративный алгоритм']:
        last_point = df[algo].iloc[-1]
        plt.annotate(f'{last_point:.1f} мс', 
                    xy=(last_size, last_point),
                    xytext=(10, 0), 
                    textcoords='offset points',
                    fontsize=10,
                    fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", 
                            facecolor="white", 
                            alpha=0.8,
                            edgecolor='gray'))

    sns.despine()
    plt.tight_layout()

    plt.show()

data_1 = {
    'sequence_length': [],
    'Рекурсивный алгоритм': [],
    'Итеративный алгоритм': []
}

with open('data.txt', 'r') as f:
    plus = 200
    i = 100
    while i <= 10**3:
        a = f.readline().split()

        data_1['sequence_length'].append(i)
        data_1['Рекурсивный алгоритм'].append(float(a[0]))
        data_1['Итеративный алгоритм'].append(float(a[1]))
        i += plus
    plus = 2000
    i = 1000
    while i <= 10**4:
        a = f.readline().split()

        data_1['sequence_length'].append(i)
        data_1['Рекурсивный алгоритм'].append(float(a[0]))
        data_1['Итеративный алгоритм'].append(float(a[1]))
        i += plus

graphics(data_1)