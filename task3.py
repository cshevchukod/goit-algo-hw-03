def move_disk(src, dest, towers):
    disk = towers[src].pop()          # знімаємо верхній диск зі стрижня src
    towers[dest].append(disk)         # кладемо на стрижень dest
    print(f"Перемістити диск {disk} з {src} на {dest}")
    print(f"Проміжний стан: {towers}")


def hanoi(n, src, dest, aux, towers):
    """Перемістити n дисків зі стрижня src на dest, використовуючи aux."""
    if n == 1:
        move_disk(src, dest, towers)
    else:
        # 1) перенести n-1 дисків на допоміжний стрижень
        hanoi(n - 1, src, aux, dest, towers)
        # 2) перенести найбільший диск n
        move_disk(src, dest, towers)
        # 3) перенести n-1 дисків з допоміжного на цільовий
        hanoi(n - 1, aux, dest, src, towers)


def task3():
    user_input = input("Введіть кількість дисків n: ")
    try:
        n = int(user_input)
        if n <= 0:
            print("n має бути додатнім цілим числом")
            return
    except ValueError:
        print("Потрібно ввести ціле число")
        return

    # Стани стрижнів: A, B, C
    towers = {
        'A': list(range(n, 0, -1)),   # [n, n-1, ..., 1]
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {towers}")
    hanoi(n, 'A', 'C', 'B', towers)
    print(f"Кінцевий стан: {towers}")


if __name__ == "__main__":
    task3()
