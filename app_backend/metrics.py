from matplotlib import pyplot as plt


def generate_line_bar(fail, success, timing):
    """Requests line bar"""
    print('hey')
    legend = ['Success', 'Failed']
    w = 0.6

    plt.bar(timing, success, w, color='g')
    plt.bar(timing, fail, w, bottom=success, color='r')

    plt.ylabel('Total requests', fontsize=14)
    plt.xlabel('Hour', fontsize=14)
    plt.legend(legend, loc=2)

    plt.savefig('app_backend/static/success-failed.png')
    plt.close()


def hey():
    print('hey')
