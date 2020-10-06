import os
os.chdir('/')
path = input('Podaj ścieżkę eksplorowanej struktury: ')

for root, _ , files in os.walk(path):
	print('Ścieżka: {path}'.format(path=root))
	if files:
		for file in files:
			print('Plik: {file}'.format(file=file))
	else:
		print("Brak plików w danej ścieżce.")
		


