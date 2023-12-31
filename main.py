import sys


def main(fst, sec):
    return fst + sec


def run_tests():
    assert main(0, 0) == 0
    assert main(1, 2) == 3
    assert main(2, -1) != -4


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        print("starting assertion tests")
        run_tests()
    else:
        print("tests are skipped")
    main(1, 0)
