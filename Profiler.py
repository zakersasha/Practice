from line_profiler import LineProfiler

profile = LineProfiler()


@profile
def test_memory():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    test_memory()
