from translite import transliterate
import os
import shutil

folders = [
    "Kamnem_po_golove",
    "Korol_i_Shut",
    "Akusticheskiy_albom",
    "Geroi_i_Zlodei",
    "Kak_v_staroy_skazke",
    "Zhal_net_ruzhiya",
    "Bunt_na_korable",
    "Prodavets_koshmarov",
    "Poganaya_molodezh",
    "Optimism",
    "Myshelovka",
    "Khorosho",
    "Totalitarizm",
    "Nekrofiliya",
    "Krasniy_albom",
    "Vse_idet_po_planu",
    "Boevoy_stimul",
    "Tak_zakalyalas_stal",
    "Russkoe_pole_eksperimentov",
    "Zdorovo_i_vechno",
    "Instruktsiya_po_vyzhivaniyu",
    "Strategiya",
    "Solntsevorot",
    "Sto_let_odinochestva",
    "Nevynosimaya_legkost_bytiya",
    "Snosnaya_tyazhest_nebytiya",
    "Zvezdopad",
    "Normativnaya_teoriya_schastya",
    "Solntse_iyun",
    "Reanimatsiya",
    "Dolgaya_schastlivaya_zhizn",
    "Zachem_snyatsya_sny",
]

folder_translit_true = [
    "камнем_по_голове",
    "корол_и_шут",
    "акустическиы_албом",
    "герои_и_злодеи",
    "как_в_староы_сказке",
    "жал_нет_ружия",
    "бунт_на_корабле",
    "продавец_кошмаров",
    "поганая_молодеж",
    "оптимисм",
    "мышеловка",
    "хорошо",
    "тоталитаризм",
    "некрофилия",
    "красниы_албом",
    "все_идет_по_плану",
    "боевоы_стимул",
    "так_закалялас_стал",
    "русское_поле_експериментов",
    "здорово_и_вечно",
    "инструкция_по_выживанию",
    "стратегия",
    "солнцеворот",
    "сто_лет_одиночества",
    "невыносимая_легкост_бытия",
    "сносная_тяжест_небытия",
    "звездопад",
    "нормативная_теория_счастя",
    "солнце_июн",
    "реанимация",
    "долгая_счастливая_жизн",
    "зачем_сняця_сны",
]


def rename_files_in_directory(directory: str) -> None:
    """
    Пример функции для переименования файлов в директории.
    Переименовывает папки на основе транслитерации.
    """
    for folder_name in os.listdir(directory):
        old_path = os.path.join(directory, folder_name)
        if os.path.isdir(old_path):
            new_name = transliterate(folder_name.lower())
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)


def test_of_correct_translite():
    """
    Проверка корректности транслитерации.
    Создаёт директории, переименовывает их и проверяет результат.
    """
    test_directory = "./test_folders_and_archives"
    os.makedirs(test_directory, exist_ok=True)

    try:
        # Создание папок и файлов
        for i, folder_name in enumerate(folders):
            folder_path = os.path.join(test_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            with open(os.path.join(folder_path, f"file_{i}.txt"), "w") as f:
                f.write(f"This is a test file for folder {folder_name}")

        # Переименование
        rename_files_in_directory(test_directory)

        # Проверка корректности переименования
        generated_folders = sorted(os.listdir(test_directory))
        assert generated_folders == sorted(
            folder_translit_true
        ), f"Ошибка: Ожидалось {folder_translit_true}, но получено {generated_folders}"

        print("Тест пройден успешно!")

    finally:
        # Удаление тестовой директории и её содержимого
        shutil.rmtree(test_directory, ignore_errors=True)


def test_of_one_folder_0():
    """
    Тест на одной папке.
    """

    test_directory = "./test_folder"
    os.makedirs(test_directory, exist_ok=True)

    try:
        # Создание папок и файлов
        folder_path = os.path.join(test_directory, folders[0])
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, f"file.txt"), "w") as f:
            f.write(f"This is a test file for folder {folders[0]}")

        # Переименование
        rename_files_in_directory(test_directory)

        # Проверка корректности переименования
        generated_folders = os.listdir(test_directory)
        assert generated_folders == [
            folder_translit_true[0]
        ], f"Ошибка: Ожидалось {folder_translit_true[0]}, но получено {generated_folders}"

        print("Тест пройден успешно!")

    finally:
        # Удаление тестовой директории и её содержимого
        shutil.rmtree(test_directory, ignore_errors=True)


def test_of_one_folder_1():
    """
    Тест на одной папке.
    """

    test_directory = "./test_folder"
    os.makedirs(test_directory, exist_ok=True)

    try:
        # Создание папок и файлов
        folder_path = os.path.join(test_directory, folders[1])
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, f"file.txt"), "w") as f:
            f.write(f"This is a test file for folder {folders[1]}")

        # Переименование
        rename_files_in_directory(test_directory)

        # Проверка корректности переименования
        generated_folders = os.listdir(test_directory)
        assert generated_folders == [
            folder_translit_true[1]
        ], f"Ошибка: Ожидалось {folder_translit_true[1]}, но получено {generated_folders}"

        print("Тест пройден успешно!")

    finally:
        # Удаление тестовой директории и её содержимого
        shutil.rmtree(test_directory, ignore_errors=True)


def test_of_one_folder_2():
    """
    Тест на одной папке.
    """

    test_directory = "./test_folder"
    os.makedirs(test_directory, exist_ok=True)

    try:
        # Создание папок и файлов
        folder_path = os.path.join(test_directory, folders[2])
        os.makedirs(folder_path, exist_ok=True)
        with open(os.path.join(folder_path, f"file.txt"), "w") as f:
            f.write(f"This is a test file for folder {folders[2]}")

        # Переименование
        rename_files_in_directory(test_directory)

        # Проверка корректности переименования
        generated_folders = os.listdir(test_directory)
        assert generated_folders == [
            folder_translit_true[2]
        ], f"Ошибка: Ожидалось {folder_translit_true[2]}, но получено {generated_folders}"

        print("Тест пройден успешно!")

    finally:
        # Удаление тестовой директории и её содержимого
        shutil.rmtree(test_directory, ignore_errors=True)
