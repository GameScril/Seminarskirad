import re

def pretraga_karata():
	print("================")
	print("Pretraga karata")
	print("================")
	print("Izabrati opciju za pretragu?")
	print("1) Pretraga po imenu")
	print("2) Pretraga po sifri projekcije")
	print("3) Pretraga po redu i mestu: ")
	komanda = input(">> ")
	while komanda not in ("1","2","3"):
		print("Uneli ste pogresnu komandu!")
		komanda = input(">> ")
	if komanda == "1":
		brojac = 0
		print("=================")
		print("Pretraga po imenu")
		print("=================")
		k_ime = input("Uneti korisnicko ime za pretragu: ")
		with open("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				provera = red.strip().split("|")
				kor_ime = provera[0]
				if kor_ime == k_ime:
					print(red)
					brojac += 1
			if brojac == 0:
				print("Nema rezervisanih karata pod tim imenom")
			print(povratak())
	if komanda == "2":
		brojac1 = 0
		print("============================")
		print("Pretraga po sifri projekcije")
		print("============================")
		s_pro = input("Uneti sifru projekcije za pretragu u vidu (xxxx): ")
		with open("ponistene_karte.txt","r") as r:
			for i in r.readlines():
				c = i.strip().split("|")
				s_proj = c[1]
				if s_pro == s_proj:
					print(i)
					brojac1 += 1
			if brojac1 == 0:
				print("Nema rezervisanih karata pod tim imenom")
			print(povratak())
	if komanda == "3":
		brojac1 = 0
		print("================")
		print("Pretraga po redu")
		print("================")
		red = input("Uneti zeljeni red za pretragu u vidu (1,2,3,4): ")
		mesto = input("Uneti zeljeno mesto u vidu(a,b,c,d): ")
		with open("ponistene_karte.txt","r") as r:
			for i in r.readlines():
				c = i.strip().split("|")
				redd = c[2]
				mestoo = c[3]
				if red == redd and mesto == mestoo:
					print(i)
					brojac1 += 1
			if brojac1 == 0:
				print("Nema rezervisanih karata pod tim redom")
			print(povratak())
def direktna_prodaja():
	brojac = 0
	print("")
	print("==================")
	print("Direktna prodaja")
	print("==================")
	with open ("projekcija.txt","r") as r:
		print(tabela_projekcije())
		print(r.read())
		print("Za povratak uneti x: ")
		zeljeni_termin = input("Uneti oznaku projekcije za koju zelite prodati: ")
		if zeljeni_termin.lower() == 'x':
			print(prodavac())
	with open ("projekcija.txt","r") as t:	
		for i in t.readlines():
			linija = i.strip().split("|")
			oznaka = linija[0].rstrip()
			film = linija[6].rstrip()
			if zeljeni_termin == oznaka:
				print("---------------------------------------------------------------------------------------------------")
				print(i)
				print("Uneti [da] ili [ne]")
				x = input("Da li ste sigurni da zelite prodati ovu kartu: ")
				while x.lower() not in("da","ne"):
					print("")
					print("Pogresna opcija: ")
					print("Uneti [da] ili [ne]")
					x = input("Da li ste sigurni da za ovu projekciju zelite rezervisati kartu: ")
				if "da" == x.lower():
					red = input("Izaberite red(1,2,3,4): ")
					while red not in ["1","2","3","4"]:
						print("Pogresan unos")
						red = input("Izaberite red(1,2,3,4): ")
					kolona = input("Izaberite kolonu(a,b,c,d): ")
				while kolona not in ["a", "b", "c", "d"]:
					print("Pogresan unos")
					kolona = input("Izaberite kolonu(a,b,c,d): ")
				with open("Rezervacije.txt", "r") as k:
					for f in k.readlines():
						redd = f.strip().split("|")
						if zeljeni_termin in redd:
							if red in redd and kolona in redd:
								print("Mesto je zauzeto pokusaj ponovo")
					else:
						with open("Rezervacije.txt", "a") as m:
							with open("projekcija.txt", "r") as t:
								for i in t.readlines():
									linija = i.strip().split("|")
									cena = linija[7].rstrip()

								k_ime = input("Uneti vase korisnicko ime: ")
								datum = input("Uneti danasnji datum u vidu (dd.mm.gggg): ")
								ime_pro = input("Unesite ime prodavca: ")
								t = k_ime.lower()
								m.write(f"{t}|{zeljeni_termin}|{red}|{kolona}|prodato|{film}|{datum}|{cena}|{ime_pro}|\n")
							with open("ponistene_karte.txt", "a") as b:
								with open("projekcija.txt", "r") as t:
									for i in t.readlines():
										linija = i.strip().split("|")
										cena = linija[7].rstrip()
								t = k_ime.lower()
								b.write(
									f"{t}|{zeljeni_termin}|{red}|{kolona}|prodato|{film}|{datum}|{cena}|{ime_pro}|\n")
							print(povratak())

def ponistavanje_rezervacije():
	print("Ponistavanje rezervacije\n")
	print("Unesi ime korisnika za koga hocete da ponistite rezervaciju: ")
	ime = input(">> ")
	with open("Rezervacije.txt","r") as r:
		with open("ponistene_karte.txt","w") as w:
			for red in r.readlines():
				provera = red.strip().split("|")
				korIme = provera[0]
				if korIme != ime:
					w.write(red)
	print(povratak())		
def pregled_karata():
	print("Uneti korisnicko ime za pregled karata: ")
	k_ime = input('=>')
	x = k_ime.lower()
	with open ("Rezervacije.txt","r") as f:
		for i in f.readlines():
			linije = i.strip().split("|")
			ime = linije[0]
			if ime == x:
				print(i)
	print(povratak())		
def povratak():
	po = input("Za povratak uneti x: ")
	print("")
	if po == "x":
		print(prodavac())
	else:
		print("Pogresna opcija pokusaj ponovo")
		print(povratak())
def tabela_projekcije():
	print("Oznaka|Sala|Od   |Do   |Datum     |Dani prikazivanja             |Naziv filma    |Cena")
	return "------+----+-----+-----+----------+------------------------------+---------------+-----"
def tabela_filmovi():
	print("Naziv filma    |Znar             |Trajanje|Reziser        |Glavne uloge   |Godina|Kratak opis                     |Drzava")
	return "---------------+-----------------+--------+---------------+---------------+------+--------------------------------+-------"
def rezervacija():
	brojac = 0
	print("")
	print("==================")
	print("Rezervacija karata")
	print("==================")
	with open ("projekcija.txt","r") as r:
		print(tabela_projekcije())
		print(r.read())
		print("Za povratak uneti x: ")
		zeljeni_termin = input("Uneti oznaku projekcije za koju zelite da rezervisete vasu kartu: ")
		if zeljeni_termin.lower() == 'x':
			print(prodavac())
	with open ("projekcija.txt","r") as t:	
		for i in t.readlines():
			linija = i.strip().split("|")
			oznaka = linija[0].rstrip()
			cena = linija[7].rstrip
			if zeljeni_termin == oznaka:
				brojac += 1
				print("---------------------------------------------------------------------------------------------------")
				print(i)
				print("Uneti [da] ili [ne]")
				x = input("Da li ste sigurni da za ovu projekciju zelite rezervisati kartu: ")
				while x.lower() not in("da","ne"):
					print("")
					print("Pogresna opcija: ")
					print("Uneti [da] ili [ne]")
					x = input("Da li ste sigurni da za ovu projekciju zelite rezervisati kartu: ")
				if "da" == x.lower():
					red = input("Izaberite red(1,2,3,4): ")
					while red not in ["1", "2", "3", "4"]:
						print("Pogresan unos")
						red = input("Izaberite red(1,2,3,4): ")
					kolona = input("Izaberite kolonu(a,b,c,d): ")
					while kolona not in ["a", "b", "c", "d"]:
						print("Pogresan unos")
						kolona = input("Izaberite kolonu(a,b,c,d): ")
					with open("Rezervacije.txt", "r") as k:
						for f in k.readlines():
							redd = f.strip().split("|")
							oznakaa = redd[1].rstrip()
							reds = redd[2].rstrip()
							kolonas = redd[3].rstrip()
							if zeljeni_termin == oznakaa:
								if red == reds and kolona == kolonas:
									print("Mesto je zauzeto pokusaj ponovo")
						else:
							with open("Rezervacije.txt", "a") as m:
								with open("projekcija.txt", "r") as t:
									for i in t.readlines():
										linija = i.strip().split("|")
										cena = linija[7].rstrip()
										film = linija[6].rstrip()
									k_ime = input("Uneti vase korisnicko ime: ")
									datum = input("Uneti danasnji datum u vidu (dd.mm.gggg): ")
									t = k_ime.lower()
									m.write(f"{t}|{zeljeni_termin}|{red}|{kolona}|rezervisana|{film}|{datum}|{cena}|\n")
								with open("ponistene_karte.txt", "a") as b:
									with open("projekcija.txt", "r") as t:
										for i in t.readlines():
											linija = i.strip().split("|")
											cena = linija[7].rstrip()
											film = linija[6].rstrip()
									t = k_ime.lower()
									b.write(f"{t}|{zeljeni_termin}|{red}|{kolona}|rezervisana|{film}|{datum}|{cena}|\n")
								print(povratak())

def pretraga_projekcija():
	brojac = 0
	brojac1 = 0
	brojac2 = 0
	brojac3 = 0
	print("")
	print("=====================")
	print("Pretraga projekcija")
	print("=====================")
	print("1) Naziv filma")
	print("2) Oznaka sale")
	print("3) Datum i vreme pocetka projekcije")
	print("4) Datum i vreme kraja projekcije")
	print("Za povratak uneti x!")
	komanda = input("Uneti opciju pretrage: ")
	while komanda not in ("1","2","3","4","x"):
		print("--------------------------------------------")
		print("Uneli ste pogresnu opciju! Pokusajte ponovo!")
		print("--------------------------------------------")
		komanda = input("Uneti opciju pretrage: ")
	if komanda =="x":	
		print("")
		print("")	
		print(prodavac())
	elif komanda == "1":
		unos = input("Unesite naziv filma: ")
		print (tabela_projekcije())
		x = unos.lower()
	elif komanda == "2":
		unos = input("Unesite oznaku sale: ")
		print (tabela_projekcije())
		x = unos.lower()
	elif komanda == "3":
		unos1 = input("Unesite datum(u formatu dd.mm.gggg):  ")
		unos2 = input("Unesi vreme pocetka projekcije(u formatu hh:mm): ")
		print (tabela_projekcije())
	elif komanda == "4":
		unos1 = input("Unesite datum projekcije(u formatu dd.mm.gggg): ")
		unos2 = input("Unesi vreme kraja projekcije(u formatu hh:mm): ")
		print (tabela_projekcije())
	with open ("projekcija.txt","r") as r:
		for red in r.readlines():
			proveraKolone = red.strip(" ").split("|")
			nazivFilma = proveraKolone[6].rstrip()
			oznakaSale = proveraKolone[1].rstrip()
			datum = proveraKolone[4].rstrip()
			pocetakProjekcije = proveraKolone[2].rstrip()
			krajProjekcije = proveraKolone[3].rstrip()

			if komanda == "1":
				nazivFilma = re.sub(' +', ' ', nazivFilma)
				if x == nazivFilma.lower():
					brojac = 1
					print(red)

			elif komanda == "2":
				oznakaSale = re.sub(' +', ' ', oznakaSale)
				if x == oznakaSale:
					brojac = 1
					print(red)

			elif komanda == "3":
				pocetakProjekcije = re.sub(' +', ' ', pocetakProjekcije)
				datum = re.sub(' +', ' ', datum)
				if unos2 == pocetakProjekcije and unos1 == datum:
					brojac = 1
					print(red)

			elif komanda == "4":
				krajProjekcije = re.sub(' +', ' ', krajProjekcije)
				datum = re.sub(' +', ' ', datum)
				if unos2 == krajProjekcije and unos1 == datum:
					brojac = 1
					print(red)

		if not brojac:
			brojac = 1
			print("Unos ne postoji, pokusajte ponovo!")
			print('')

		return (povratak())


def pregled_filmova():
	print("")
	print("==========================")
	print("Pregled dostupnih filmova")
	print("==========================")
	file = open("film.txt","r")
	print(file.read())
	v = input("Za povratak uneti x: ")
	if v == "x":
		print(prodavac())
def pretraga_filmova():
	brojac = 0
	brojac1 = 0
	brojac2 = 0
	brojac3 = 0
	brojac4 = 0
	brojac5 = 0	
	print("")
	print("==================")
	print("Pretraga filmova")
	print("==================")
	print("1) Pretraga po nazivu filma")
	print("2) Pretraga po zanru")
	print("3) Pretraga po reziseru")
	print("4) Pretraga po ulogama")
	print("5) Pretraga po zemlji porekla")
	print("6) Pretraga po godini proizvodnje")
	print("Za povratak uneti x")
	print("Uneti jednu of opcija: ")
	komanda = input(">> ")
	if 'x' == komanda.lower():
		print(prodavac())
	while komanda not in ("1","2","3","4","5","6","x"):
		print("Uneli ste pogresnu opciju! Pokusajte ponovo!")
		komanda = input(">> ")
	unos = input("Unesite rec za pretragu: ")
	print(tabela_filmovi())
	x = unos.lower()
	with open ("filmovi_pretraga.txt","r") as r:
		for red in r.readlines():
			proveraKolone = red.strip(" ").split("|")
			nazivFilma = proveraKolone[0].rstrip()
			zanr = proveraKolone[1].rstrip()
			reziser = proveraKolone[3].rstrip()
			uloge = proveraKolone[4].rstrip()
			zemljaPorekla = proveraKolone[7].rstrip()
			godinaProizvodnje = proveraKolone[5].rstrip()
			if komanda == "1":
				if x == nazivFilma:
					print(red)
					brojac += 1
			elif komanda == "2":
				if x == zanr:
					print(red)
					brojac1 += 1
			elif komanda == "3":
				if x == reziser:
					print(red)
					brojac2 += 1
			elif komanda == "4":
				if x == uloge:
					print(red)
					brojac3 += 1
			elif komanda == "5":
				if x == zemljaPorekla:
					print(red)
					brojac4 += 1
			elif komanda == "6":
				if x == godinaProizvodnje:
					print(red)
					brojac5 += 1
		if komanda == "1":
			if brojac == 0:
				print("Nemamo u ponudi projekciju sa unetim filmom, pokusajte ponovo!")
				print('')
				print(povratak())
		elif komanda == "2":
			if brojac == 1:
				print("Nemamo u ponudi projekciju sa unetim zanrom, pokusajte ponovo!")
				print('')
				print(povratak())
		elif komanda == "3":
			if brojac == 2:
				print("Nemamo u ponudi projekciju sa unetim reziserom, pokusajte ponovo!")
				print('')
				print(povratak())
		elif komanda == "4":
			if brojac == 3:
				print("Nemamo u ponudi projekciju sa unetom ulogom, pokusajte ponovo!")
				print('')
				print(povratak())
		elif komanda == "5":
			if brojac == 4:
				print("Nemamo u ponudi projekciju sa unetom zemljom porekla, pokusajte ponovo!")
				print('')
				print(povratak())
		elif komanda == "6":
			if brojac == 5:
				print("Nemamo u ponudi projekciju sa unetom godinom proizvodnje!")
				print('')
				print(povratak())	
	return povratak()
#######################################################################################
def izlaz():
	print("")
	print("!!!!!!!!!!!!!!!!!")
	print("Da li ste sigurni")
	izlazak = int(input("[1]Da [2]Ne: "))
	print("")
	if izlazak == 1:
		exit()
	elif izlazak == 2:
		return prodavac()
	else:
		print("Pogresna komanda")	
#########################################################################################
def odjava():
	print("")
	print("!!!!!!!!!!!!!!!!!")
	print("Da li ste sigurni")
	odj = int(input("[1]Da [2]Ne: "))
	print("")
	if odj == 1:
		import Projekat
	elif odj == 2:
		return prodavac()
	else:
		print("Pogresna komanda")
		return odjava()
##########################################################################################
def prodavac():
	print("")
	print("")
	print("1) Pregled dostupnih filmova")
	print("2) Pretraga filmova")
	print("3) Pretraga projekcija")
	print("4) Rezervacija karata")
	print("5) Pregled rezervisanih karata")
	print("6) Ponistavanje rezervisanih karata")
	print("7) Pretraga karata")
	print("8) Direktna prodaja")
	print("9) Pregled rezervisanih karata")
	print("10) Odjava ")
	print("11) izlaz")
	try:
		x = int(input("Uneti zeljenu opciju: "))
	except ValueError as err:
		print(prodavac())
	if x > 11 or x < 1:
		print("*******************************")
		print("Pogresna opcija pokusaj ponovo")
		print("*******************************")
		print(prodavac())
	elif x == 1:
		print(pregled_filmova())
	elif x == 2:
		print(pretraga_filmova())
	elif x == 3:
		print(pretraga_projekcija())
	elif x == 4:
		print(rezervacija())
	elif x == 5:
		print(pregled_karata())
	elif x == 6:
		print(ponistavanje_rezervacije())
	elif x == 7:
		print(pretraga_karata())
	elif x == 8:
		print(direktna_prodaja())
	elif x == 9:
		print("===========================")
		print("Pregled rezervisanih karata")
		print("===========================")
		file = open("ponistene_karte.txt","r")
		print(file.read())
		print(povratak())
	elif x == 10:
		print(odjava())
	elif x == 11:
		print(izlaz())
prodavac()
