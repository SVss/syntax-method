import matplotlib.pyplot as plt


def draw_sample(items_list):
    for i in items_list:
        plt.plot([i.start[0], i.stop[0]], [i.start[1], i.stop[1]], c='black', linewidth=1)
    plt.show()
