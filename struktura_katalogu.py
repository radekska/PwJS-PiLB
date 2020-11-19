"""
Napisz rekurencyjne przejście drzewa katalogów i wypisanie plików, które znajdują się w eksplorowanej strukturze
"""

import os

def sprawdz_strukture_sciezki(path):
	os.chdir('/')
	for root, _ , files in os.walk(path):
		print('\nŚcieżka: {path}'.format(path=root))
		if files:
			for file in files:
				print('Plik: {file}'.format(file=file))
		else:
			print("Brak plików w danej ścieżce.")
		
if __name__ == '__main__':
	path = input('Podaj ścieżkę eksplorowanej struktury: ')
	sprawdz_strukture_sciezki(path)

