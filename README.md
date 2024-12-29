# Главная страница

## Введение
This project was originally conceived as a useful code. In e-books, the names of books and folders are often written in transliteration, so it is inconvenient to work with the original folder names, and you have to translate them. The code is pretty simple, but I decided to post it anyway as an example of how to use GitHub, hooks, pre-commits, and GitHub jobs.

From now on, all comments and descriptions of methods and functions will be in Russian. This is necessary so that the English-speaking audience can better understand the purpose of the project, as they do not encounter such problems because the file names are already written in English.

Этот проект изначально задумывался как полезный код. В электронных книгах часто названия книг и папок записываются в транслитерации, поэтому работать с исходными названиями папок неудобно, и приходится их переводить. Код достаточно простой, однако я всё равно решил опубликовать этот проект как мой иллюстрация моего умения работать с гитхабом, хуками, прекоммитами и гитхабными джобами.


Алгоритм следующий:
1. У нас есть папка, в которой остальные папки и архивы, мы для каждой папки (или архива) создаём папку с аналогичным название.
2. Переводим внешние папки (не нарушая свойств внутренних элементов).
3. Сортируем и работаем со внешними папками.
4. Удаляем внешние папки после требуемых сортировок. 

Например у нас есть архив "Kamnem_po_golove.zip", то программа создаст папку с содержимым \#\_Kamnem_po_golove/Kamnem_po_golove.zip, затем переведёт и получит \#\_Камнем_по_голове/Kamnem_po_golove.zip, что позволит работать с обёртками, понимая их содержимое, а затем безболезненно после требуемой сортировки удалить папку и сохранить содержимое. \#\_ здесь написан для того, чтобы определять какие именно папки являются обрёртками, а какие полноценными папки, которые трогать не стоит.

Также проект используется для демонтрации работы Doxygen. 

## Основные возможности проекта
- Возможность работать с программой при помощи Makefile, а именно сгенерировать тестовую директорию, создать надпапки, а также удалять подпапки.
- Генерация HTML и PDF документации.
- Перевод названий папок.
- Создание обёрток для файлов, которые позволяют работать с обёртками, не а с изначальными папками. 
- Удаление обёрток.
- Демонстрация работы с pytest.


## Как использовать Doxygen
1. Установите Doxygen.
2. Настройте конфигурацию в `Doxyfile`.
3. Выполните команду `doxygen`, чтобы сгенерировать документацию.

## Как использовать Makefile
- make test_all: Проводит все тесты
- make test_translite: Генерирует папки в ./test_folders_and_archives и демонстрирует как работает перевод транслита, изменяя названия файлов в этой же папке.
- make test_archive: Генерирует папки в ./test_folders_and_archives и в папку ./test_archives сохраняет папки с обёртками
- make test_unarchive: Генерирует папки в ./test_folders_and_archives и в папку ./test_archives сохраняет папки с обёртками, а затем удаляет обёртки и результат сохраняет в ./test_unarchived
- make clean: удаляет папки, которые могли быть созданы выше.

## Documentation

You can find the documentation [here](https://romansamoilovmsumm.github.io/translite_english_to_russian/).


