def sprawdz_dostep():
	kod_wprowadzony = None
	kod_dostepu = input("Podaj kod dostępu: ")

	print("Kod dostępu zapisany.")

	while kod_wprowadzony != 'quit':
		kod_wprowadzony = input("Podaj kod dostępu: ")

		if kod_dostepu == kod_wprowadzony:
			print("Uzyskano dostęp!")
			break
		else:
			print("Kod nieprawidłowy!")

if __name__ == '__main__':
	sprawdz_dostep()