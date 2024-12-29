import os
import sys

# Словарь для транслитерации
translit_dict = {
    "a": "а",
    "b": "б",
    "v": "в",
    "g": "г",
    "d": "д",
    "e": "е",
    "yo": "ё",
    "zh": "ж",
    "z": "з",
    "i": "и",
    "j": "й",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "f": "ф",
    "h": "х",
    "c": "ц",
    "ch": "ч",
    "sh": "ш",
    "shch": "щ",
    "yu": "ю",
    "ya": "я",
    "ey": "э",
    "yi": "ы",
    "kh": "х",
    "ts": "ц",
    "ye": "е",
    "y": "ы",
}


# Функция для транслитерации
def transliterate(text: str) -> str:
    """
    Применяет транслитерацию к тексту.

    :text (str): Текст для транслитерации.

    :return: str: Текст с транслитерацией.
    """

    for k in sorted(translit_dict.keys(), key=lambda x: -len(x)):
        text = text.replace(k, translit_dict[k])
    return text


# Преобразование имени с учётом расширения
def convert_file_name(file_name: str) -> str:
    """
    Преобразование имени с учётом расширения.
    Функция применяет транслитерацию к основному имени и сохраняет расширение.

    file_name (str): Имя файла с расширением.

    :return: str: Преобразованное имя файла.
    """

    # Разбиваем имя на основное имя и расширение
    if "." in file_name:
        base_name, ext = os.path.splitext(file_name)
    else:
        base_name, ext = file_name, ""

    # Применяем транслитерацию только к основному имени
    words = base_name.split("_")
    converted_words = [transliterate(word.lower()) for word in words]
    return "_".join(converted_words) + ext


# Основная функция для переименования папок и файлов с учетом архивов
def rename_files_in_directory(directory: str) -> None:
    """
    Изменяет название файлов и директорий в указанной директории.

    :directory: str: Путь к директории, в которую будут переименованы папки и файлы.

    :return: None
    """

    for root, dirs, files in os.walk(directory):
        # Переименовываем директории
        for name in dirs:
            new_name = convert_file_name(name)
            old_path = os.path.join(root, name)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

        # Переименовываем файлы (с учётом расширений)
        for name in files:
            new_name = convert_file_name(name)
            old_path = os.path.join(root, name)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)


# Пример использования
if __name__ == "__main__":
    test_directory = "./test_folders_and_archives"
    rename_files_in_directory(test_directory)


if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        print("Использование: python3 translite.py <путь_к_директории>")
        sys.exit(1)

    # Получаем путь к директории из аргументов командной строки
    test_directory = sys.argv[1]

    # Генерируем папки и архивы
    rename_files_in_directory(test_directory)
