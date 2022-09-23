from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "bachelor") == 990
    assert count_ocurrences("src/jobs.csv", "responsibilities") == 1645
    assert count_ocurrences("src/jobs.csv", "training") == 1347
