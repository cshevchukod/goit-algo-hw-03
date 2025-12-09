import sys
from pathlib import Path


def sort_dir(src: Path, dest: Path):
    #Рекурсивно обходимо src і копіюємо файли в dest за розширеннями.
    try:
        for item in src.iterdir():
            if item.is_dir():
                # рекурсія для підпапки
                sort_dir(item, dest)
            elif item.is_file():
                # визначаємо розширення
                ext = item.suffix[1:] if item.suffix else "no_extension"
                target_dir = dest / ext
                target_dir.mkdir(parents=True, exist_ok=True)

                target_file = target_dir / item.name
                try:
                    # просте «копіювання» через читання/запис байтів
                    data = item.read_bytes()
                    target_file.write_bytes(data)
                except OSError as e:
                    print(f"Помилка під час копіювання файлу {item}: {e}")
    except PermissionError as e:
        print(f"Немає доступу до директорії {src}: {e}")


def task1():
    if len(sys.argv) < 2:
        print("Використання: python task1.py <source_dir> [dest_dir]")
        return

    src = Path(sys.argv[1])
    dest = Path(sys.argv[2]) if len(sys.argv) >= 3 else Path("dist")

    if not src.exists() or not src.is_dir():
        print(f"Вихідна директорія {src} не існує.")
        return

    dest.mkdir(parents=True, exist_ok=True)

    sort_dir(src, dest)

    print("Готово.")


if __name__ == "__main__":
    task1()
