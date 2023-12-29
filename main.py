import sys


def main(fst, sec):
    print(eval(f"{fst} + {sec}"))


if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2])
