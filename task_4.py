def snowball(n):
    offset = 0.5
    ray = n / 2

    for x in range(n):
        for y in range(n):
            if (x + offset - ray) ** 2 + (y + offset - ray) ** 2 <= ray ** 2:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def snowman(n):
    pass
