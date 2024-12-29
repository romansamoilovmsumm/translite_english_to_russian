import os
import shutil
import sys


def unwrap_wrappers(wrapper_path: str, output_path: str) -> None:
    """
    Копирует содержимое обёрток (папок с одним элементом внутри), если их название начинается с '#_',
    и копирует все остальные файлы и папки в указанную выходную директорию.

    :wrapper_path: str: Путь к директории, содержащей обёртки.
    :output_path: str: Путь к выходной директории для сохранения содержимого.

    :return: None
    """

    # Создаем выходную директорию, если она не существует
    os.makedirs(output_path, exist_ok=True)

    # Получаем список всех папок и файлов в указанной директории
    items = os.listdir(wrapper_path)

    for item in items:
        full_item_path = os.path.join(wrapper_path, item)

        # Проверяем, является ли элемент папкой и начинается ли имя с '#_'
        if os.path.isdir(full_item_path):
            # Список содержимого текущей обёртки
            inner_items = os.listdir(full_item_path)

            if item.startswith("#_") and len(inner_items) == 1:
                # Если в папке только один элемент и она начинается с '#_', копируем его в выходную директорию
                inner_item_path = os.path.join(full_item_path, inner_items[0])
                dest_path = os.path.join(output_path, inner_items[0])

                # Копируем файл или папку
                if os.path.isdir(inner_item_path):
                    shutil.copytree(inner_item_path, dest_path)
                else:
                    shutil.copy(inner_item_path, dest_path)

                print(
                    f"Содержимое обёртки '{full_item_path}' скопировано в '{dest_path}'."
                )
            else:
                # Копируем папку, если она не обёртка или содержит больше одного элемента
                dest_path = os.path.join(output_path, item)
                shutil.copytree(full_item_path, dest_path)
                print(f"Папка '{full_item_path}' скопирована в '{dest_path}'.")
        else:
            # Копируем файл, если он не является папкой
            dest_path = os.path.join(output_path, item)
            shutil.copy(full_item_path, dest_path)
            print(f"Файл '{full_item_path}' скопирован в '{dest_path}'.")


if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 3:
        print(
            "Использование: python3 unwrap.py <путь_к_папке> <путь_к_выходной_директории>"
        )
        sys.exit(1)

    # Получаем пути из аргументов командной строки
    wrapper_path = sys.argv[1]
    output_path = sys.argv[2]

    # Проверяем, существует ли входная директория
    if not os.path.exists(wrapper_path):
        print(f"Ошибка: директория {wrapper_path} не существует.")
        sys.exit(1)

    # Вызываем функцию unwrap_wrappers
    unwrap_wrappers(wrapper_path, output_path)
    print(f"Содержимое из '{wrapper_path}' обработано и сохранено в '{output_path}'.")
