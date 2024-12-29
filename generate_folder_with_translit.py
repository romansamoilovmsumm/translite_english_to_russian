import os
import random
import zipfile
import sys

# Транслитерированные названия папок
folders = [
    "Kamnem_po_golove", "Korol_i_Shut", "Akusticheskiy_albom", "Geroi_i_Zlodei",
    "Kak_v_staroy_skazke", "Zhal_net_ruzhiya", "Bunt_na_korable", "Prodavets_koshmarov",
    "Poganaya_molodezh", "Optimism", "Myshelovka", "Khorosho", "Totalitarizm", 
    "Nekrofiliya", "Krasniy_albom", "Vse_idet_po_planu", "Boevoy_stimul", 
    "Tak_zakalyalas_stal", "Russkoe_pole_eksperimentov", "Zdorovo_i_vechno", 
    "Instruktsiya_po_vyzhivaniyu", "Strategiya", "Solntsevorot", 
    "Sto_let_odinochestva", "Nevynosimaya_legkost_bytiya", "Snosnaya_tyazhest_nebytiya", 
    "Zvezdopad", "Normativnaya_teoriya_schastya", "Solntse_iyun", "Reanimatsiya", 
    "Dolgaya_schastlivaya_zhizn", "Zachem_snyatsya_sny"
]

# Список возможных расширений для архивов
extensions = ['.zip', '.rar']

# Функция для генерации папок и архивов
def generate_named_folders_and_archives(directory: str) -> None:
    """
    Генерирует папки и архивы в указанной директории.
    
    :directory: str: Путь к директории, в которую будут созданы папки и архивы.

    :return: None
    """

    # Создаем директорию, если она не существует
    os.makedirs(directory, exist_ok=True)
    
    for i, folder_name in enumerate(folders, 1):
        # Случайно выбираем, создать ли папку или архив
        if random.choice([True, False]):
            # Создаем папку
            folder_path = os.path.join(directory, f"test_{folder_name}")
            os.makedirs(folder_path, exist_ok=True)
            
            # В каждой папке создаём один файл
            with open(os.path.join(folder_path, f"file_{i}.txt"), 'w') as f:
                f.write(f"This is test file for folder {folder_name}")
        else:
            # Создаем архив
            archive_name = f"test_{folder_name}{random.choice(extensions)}"
            archive_path = os.path.join(directory, archive_name)
            
            # Создаем пустой архив (для простоты)
            with zipfile.ZipFile(archive_path, 'w') as archive:
                # Добавляем пустой файл в архив для демонстрации
                archive.writestr(f"file_{i}.txt", f"This is test file for archive {folder_name}")
    
    print(f"Generated {len(folders)} folders and archives in {directory}")

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        print("Использование: python3 generate_folder_with_translit.py <путь_к_директории>")
        sys.exit(1)

    # Получаем путь к директории из аргументов командной строки
    test_directory = sys.argv[1]

    # Генерируем папки и архивы
    generate_named_folders_and_archives(test_directory)
