import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'img/{name}.png')

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('img/pie.png')


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,200,300]
    generate_pie_chart(labels,values)




