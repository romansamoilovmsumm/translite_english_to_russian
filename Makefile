test_all: test_translite test_archive test_unarchive

test_translite:
	python3 generate_folder_with_translit.py ./test_folders_and_archives; python3 translite.py ./test_folders_and_archives

test_archive:
	python3 generate_folder_with_translit.py ./test_folders_and_archives; python3 archive.py ./test_folders_and_archives ./test_archives

test_unarchive: 
	python3 generate_folder_with_translit.py ./test_folders_and_archives; python3 archive.py ./test_folders_and_archives ./test_archives; python3 unarchive.py ./test_archives ./test_unarchived

clean:
	rm -rf ./test_folders_and_archives ./test_archives ./test_unarchived

