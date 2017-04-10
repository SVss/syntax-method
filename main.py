from input import *
from grammar import *
from syntax_method import analyze

def main():
    # print(analyze(INPUT_ROOF, ROOF_GRAMMAR))
    # print(analyze(INPUT_RECT, ROOF_GRAMMAR))
    # print(analyze(INPUT_RECT, RECT_GRAMMAR))
    print(analyze(INPUT_HOUSE, HOUSE_GRAMMAR))
    # print(analyze(INPUT_HOUSE, ROOF_GRAMMAR))

if __name__ == '__main__':
    main()
