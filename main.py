from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def main():
    introduce_yourself()
    robot.research_scientists(SCIENTISTS)
    robot.say_goodbye()


if __name__ == "__main__":
    main()