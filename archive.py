import os
import shutil
import sys

"""
Модуль содержит в себе функционал для создания обёрток
в виде папок для всех папок или архивов из указанной
директории. Обёртки создаются в указанной выходной
директории.

Функция archive создает папки и архивы в указанной
директории. Она использует shutil для копирования, чтобы
создать обёртки."""


def archive(folder_path: str, archive_path: str) -> None:
    """
    Создание обёртки в виде папок для всех папок или архивов
    из указанной директории. Обёртки создаются в указанной
    выходной директории.

    :folder_path: str: Путь к папке, откуда берутся папки и архивы.
    :archive_path: str: Путь к архиву, в который будут сохранены обёртки для папок и архивов.
    """

    # Создаем директорию, если она не существует
    os.makedirs(archive_path, exist_ok=True)

    # Получаем список всех элементов в указанной директории
    items = os.listdir(folder_path)

    for item in items:
        full_item_path = os.path.join(folder_path, item)
        dest_wrapper_path = os.path.join(archive_path, "#_" + item)

        # Создаем папку-обёртку с тем же названием
        os.makedirs(dest_wrapper_path, exist_ok=True)

        if os.path.isdir(full_item_path):
            # Если это папка, копируем её внутрь обёртки
            shutil.copytree(full_item_path, os.path.join(dest_wrapper_path, item))
        elif os.path.isfile(full_item_path):
            # Если это файл (например, архив), перемещаем его внутрь обёртки
            shutil.copy(full_item_path, os.path.join(dest_wrapper_path, item))
        else:
            print(f"Пропущен: {full_item_path} не является файлом или папкой.")

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 3:
        print("Использование: python3 archive.py <путь_к_папке> <путь_к_архиву>")
        sys.exit(1)

    # Получаем пути из аргументов командной строки
    folder_path = sys.argv[1]
    archive_path = sys.argv[2]

    # Проверяем, существует ли входная директория
    if not os.path.exists(folder_path):
        print(f"Ошибка: директория {folder_path} не существует.")
        sys.exit(1)

    # Вызываем функцию archive
    archive(folder_path, archive_path)
    print(f"Обёртки успешно созданы в {archive_path}.")
