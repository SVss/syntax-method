from input import *
from grammar import *
from syntax_method import analyze
from drawer import draw_sample

def test_analyze():
    print("Is roof a roof ?")
    print(analyze(INPUT_ROOF, ROOF_GRAMMAR))
    draw_sample(INPUT_ROOF)

    print("Is rectangle a roof ?")
    print(analyze(INPUT_RECT, ROOF_GRAMMAR))

    print("Is rectangle a rectangle ?")
    print(analyze(INPUT_RECT, RECT_GRAMMAR))
    draw_sample(INPUT_RECT)

    print("Is house a house ?")
    print(analyze(INPUT_HOUSE, HOUSE_GRAMMAR))
    draw_sample(INPUT_HOUSE)

    print("Is house a roof ?")
    print(analyze(INPUT_HOUSE, ROOF_GRAMMAR))


def generate_house(rect):
    house = HouseRule().generate(rect)
    if analyze(house, HOUSE_GRAMMAR):
        draw_sample(house)
    else:
        print("Missed!")


def main():
    generate_house(
        Rect(
            [0, 100],
            [40, 0]
        )
    )


if __name__ == '__main__':
    main()
