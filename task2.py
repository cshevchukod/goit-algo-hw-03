import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)  # трохи вище
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def task2():
    user_input = input("Введіть рівень рекурсії (0, 1, 2, ...): ")
    try:
        order = int(user_input)
        if order < 0:
            order = 0
    except ValueError:
        order = 0

    draw_koch_snowflake(order)


if __name__ == "__main__":
    task2()
