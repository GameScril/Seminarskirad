def unos():
	print("===============")
	print("Unos projekcije ili filma: ")
	print("===============")
	print("1) Unos nove projekcije: ")
	print("2) Unos novog filma: ")
	print("Za povratak uneti x")
	komanda = input(">>")
	while komanda not in ("1","2","x"):
		print("Pogresna opcija pokusaj ponovo: ")
		komanda = input(">>")
	if komanda == '1':
		print("Unos nove projekcije:")

		oznaka = input("Uneti oznaku projekcije(xxxx): ")
		if len(oznaka) != 6:
			oznaka = oznaka[:6]
			if len(oznaka) < 6:
				oznaka = oznaka + " " * (6 - len(oznaka))

		sala = input("Uneti salu(a1,a2,a3,a4): ")
		if len(sala) != 4:
			sala = sala[:4]
			if len(sala) < 4:
				sala = sala + " " * (4 - len(sala))

		vre_po = input("Uneti vreme pocetka(hh:mm): ")
		if len(vre_po) != 5:
			vre_po = vre_po[:5]
			if len(vre_po) < 5:
				vre_po = vre_po + " " * (5 - len(vre_po))

		vre_kra = input("Uneti vreme kraja(hh:mm): ")
		if len(vre_kra) != 5:
			vre_kra = vre_kra[:5]
			if len(vre_kra) < 5:
				vre_kra = vre_kra + " " * (5 - len(vre_kra))

		dani = input("Uneti dane odrzavanja projekcije(dan1,dan2): ")
		if len(dani) != 30:
			dani = dani[:30]
			if len(dani) < 30:
				dani = dani + " " * (30 - len(dani))

		film = input("Uneti naziv filma: ")
		if len(film) != 15:
			film = film[:15]
			if len(film) < 15:
				film = film + " " * (15 - len(film))

		datum = input("Uneti datum projekcije(dd.mm.gggg): ")
		if len(datum) != 10:
			datum = datum[:10]
		if len(datum) < 10:
			datum = datum + " " * (10 - len(datum))

		cena = input("Uneti cenu: ")

		with open ("projekcija.txt","a") as b:
			b.write( '\n'+ oznaka + "|" + sala.lower() + "|" + vre_po + "|" + vre_kra + "|" + datum + "|" + dani.lower() + "|" + film.lower() + "|"+cena)
		print(povratak())
	elif komanda == '2':
		print("Unos novog filma:")
		ime = input("Uneti naziv filma: ")
		if len(ime) != 15:
			ime = ime[:15]
			if len(ime) < 15:
				ime = ime + " " * (15 - len(ime))

		zanr = input("Uneti zanr filma: ")
		if len(zanr) != 17:
			zanr = zanr[:17]
			if len(zanr) < 17:
				zanr = zanr + " " * (17 - len(zanr))

		trajanje = input("Uneti trajanje filma (hh:mm): ")
		if len(trajanje) != 8:
			trajanje = trajanje[:8]
			if len(trajanje) < 8:
				trajanje = trajanje + " " * (8 - len(trajanje))

		reziser = input("Uneti ime rezisera: ")
		if len(reziser) != 15:
			reziser = reziser[:15]
			if len(reziser) < 15:
				reziser = reziser + " " * (15 - len(reziser))

		glavna = input("Uneti glavnu ulogu: ")
		if len(glavna) != 15:
			glavna = glavna[:15]
			if len(glavna) < 15:
				glavna = glavna + " " * (15 - len(glavna))

		godina = input("Uneti godinu filma: ")
		if len(godina) != 6:
			godina = godina[:6]
			if len(godina) < 6:
				godina = godina + " " * (6 - len(godina))

		kratak = input("Uneti kratak opis: ")
		if len(reziser) != 32:
			kratak = kratak[:32]
			if len(kratak) < 32:
				kratak = kratak + " " * (32 - len(kratak))

		drzava = input("Uneti ime drzava: ")

		with open ("film.txt","a") as b:
			b.write("\n" + ime + "|" + zanr + "|" + trajanje + "|" + reziser + "|" + glavna + "|" + godina + "|" + kratak + "|" + drzava)
		with open ("filmovi_pretraga.txt","a") as r:
			r.write("\n" + ime.lower() + "|" + zanr.lower() + "|" + trajanje + "|" + reziser.lower() + "|" + glavna.lower() + "|" + godina + "|" + kratak.lower() + "|" + drzava.lower()+ "\n")
		print(povratak())

def izvestavanje():
	print("============")
	print("Izvestavanje")
	print("============")
	print("1) Lista prodatih karata za odabran datum")
	print("2) Ukupan broj i ukupna cena prodatih karata za izabran datum")
	print("3) Ukupna cena prodatih karata za zadati film u svim projekcijama")
	print("4) Ukupna cena prodatih karata za datog prodavca")
	print("5) Ukupna zarada")
	print("Za povratak uneti x")
	komanda = input("Uneti zeljenu opciju: ")
	while komanda not in ("1","2","3","4","5","x"):
		print("Uneli ste pogresnu opciju! Pokusajte ponovo!")
		komanda = input(">> ")
	if komanda == "x":
		print(povratak())
	elif komanda == "1":
		brojac = 0
		print("Lista prodatih karata za odabran datum: ")
		datum = input("Uneti datum u vidu dd.mm.gggg: ")
		with open ("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				proveraKolone = red.strip(" ").split("|")
				datumm = proveraKolone[7]
				if datumm == datum:
					print(red)
					brojac += 1
			if brojac == 0:
				print("Nema ni jedna prodana karta za uneti datum")
				print(povratak())
			print(povratak())
	elif komanda == "2":
		brojac = 0
		ukupna_cena = 0
		print("Ukupan broj i ukupna cena prodatih karata za izabran datum: ")
		datum = input("Uneti datum u vidu dd.mm.gggg: ")
		with open ("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				proveraKolone = red.strip(" ").split("|")
				datumm = proveraKolone[7]
				cena = int(proveraKolone[6])
				if datumm == datum:
					brojac += 1
					ukupna_cena += cena
			if brojac == 0:
				print("Nema ni jedna prodana karta za uneti datum")
				print(povratak())
			print("========================================================================")
			print("Ukupan broj prodatih karti za izabran datum je: ",brojac)
			print("------------------------------------------------------------------------")
			print("Ukupna zarada prodatih karti za izabran datum je: ",ukupna_cena,"dinara")
			print("=========================================================================")
			print(povratak())
	elif komanda == "3":
		brojac = 0
		ukupna_cena = 0
		print("Ukupan zarada prodatih karata za zadati filmm: ")
		film = input("Uneti naziv filma: ")
		with open ("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				proveraKolone = red.strip(" ").split("|")
				filmm = proveraKolone[5]
				cena = int(proveraKolone[6])
				if film == filmm:
					brojac += 1
					ukupna_cena += cena
			if brojac == 0:
				print("Nema ni jedna prodana karta za uneti datum")
				print(povratak())
			print("========================================================================")
			print("Ukupan broj prodatih karti za izabran film je: ",brojac)
			print("------------------------------------------------------------------------")
			print("Ukupna zarada prodatih karti za izabran film je: ",ukupna_cena,"dinara")
			print("=========================================================================")
			print(povratak())
	elif komanda == "4":
		brojac = 0
		ukupna_cena = 0
		print("Ukupan broj i zarada prodatih karata za datog prodavca: ")
		prodavac = input("Uneti ime prodavca: ")
		x = prodavac.lower()
		with open ("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				proveraKolone = red.strip(" ").split("|")
				prodavacc = proveraKolone[8].rstrip()
				cena = int(proveraKolone[6])
				if x == prodavacc:
					brojac += 1
					ukupna_cena += cena
			if brojac == 0:
				print("Nema ni jedna prodana karta za unetog prodavca")
				print(povratak())
			print("========================================================================")
			print("Ukupan broj prodatih karti za izabranog prodavca: ",brojac)
			print("------------------------------------------------------------------------")
			print("Ukupna zarada prodatih karti za izabranog prodavca: ",ukupna_cena,"dinara")
			print("=========================================================================")
			print(povratak())
	elif komanda == "5":
		brojac = 0
		ukupna_cena = 0
		print("Ukupna zarada: ")
		with open ("ponistene_karte.txt","r") as r:
			for red in r.readlines():
				proveraKolone = red.strip(" ").split("|")
				cena = int(proveraKolone[6])
				brojac += 1
				ukupna_cena += cena
			if brojac == 0:
				print("Nema zarade :( ")
				print(povratak())
			print("========================================================================")
			print("Ukupan broj prodatih karti: ",brojac)
			print("------------------------------------------------------------------------")
			print("Ukupna zarada prodatih karti: ",ukupna_cena,"dinara")
			print("=========================================================================")
			print(povratak())
			
def Korisnicko_ime(ime_fajla):
	korisnicko_ime = input("Uneti korisnicko ime:")
	fajl = open(ime_fajla,"r")
	for red in fajl.readlines():
		c = red.strip().split("|")
		korisnik = c[0]
		if len(korisnicko_ime) == 0:
			print("===========================================")
			print("Korisnicko ime nije ispravno pokusaj ponovo")
			print("===========================================")
			print(glavna_funkcija())
		if korisnicko_ime == korisnik:
			print("*************************")
			print("Korisnicko ime je zauzeto")
			print("*************************")
			print("Pokusaj ponovo")
			print(menadzer())
	fajl.close
	fajl = open("korisnici.txt","a")
	fajl.write(korisnicko_ime)
	fajl.write("|")
	fajl.close
def Lozinka():
	lozinka = input("Uneti lozinku: ")
	broj = 0
	brojevi = "0123456789"
	for i in lozinka:
		for u in brojevi.strip():
			if i == u:
				broj = broj + 1
	if broj == 0 or len(lozinka) < 6:
		print("Lozinka mora da ima najmanje 6 znakova i 1 broj")
		return menadzer()			
	fajl = open("korisnici.txt","a")
	fajl.write(lozinka)
	fajl.write("|")
	fajl.close
def registrovanje_prodavaca():
	print("============================")
	print("Registracija novih prodavaca")
	print("============================")
	print(Korisnicko_ime("korisnici.txt"))	
	print(Lozinka())
	error = ""
	ime = input("Uneti ime: ")
	while ime == error:
		print("******")
		print("Greska")
		print("******")
		ime = input("Uneti ime: ")
	prezime = input("Uneti prezime: ")
	while prezime == error:
		print("******")
		print("Greska")
		print("******")
		prezime == input("Uneti Prezime: ")
	fajl = open("korisnici.txt","a")
	fajl.write(ime)
	fajl.write("|")
	fajl.write(prezime)
	fajl.write("|")
	fajl.write("prodavac")
	fajl.write("\n")
	fajl.close
	print("USPESNO JE REGISTROVAN NOVI PRODAVAC")
	print("Nakon registracije restartovati program zbog ucitavanja korisnika")
	print(povratak())
def pregled_karata():
	print("Uneti korisnicko ime za pregled karata: ")
	k_ime = input('=>')
	x = k_ime.lower()
	with open ("ponistene_karte.txt","r") as f:
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
		print(menadzer())
	else:
		print("Pogresna opcija pokusaj ponovo")
		print(povratak())
def tabela_projekcije():
	print("Oznaka|Sala|Od   |Do   |Datum     |Dani prikazivanja             |Naziv filma    |Cena")
	return "------+----+-----+-----+----------+------------------------------+---------------+-----"
def tabela_filmovi():
	print("Naziv filma    |Zanr             |Trajanje|Reziser        |Glavne uloge   |Godina|Kratak opis                     |Drzava")
	return "---------------+-----------------+--------+---------------+---------------+------+--------------------------------+-------"
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
	while komanda not in ["1","2","3","4","x"]:
		print("--------------------------------------------")
		print("Uneli ste pogresnu opciju! Pokusajte ponovo!")
		print("--------------------------------------------")
		komanda = input("Uneti opciju pretrage: ")
	if komanda =="x":
		print("")
		print("")
		print(kupac())
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
		brojac = 0
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

		return(povratak())
def pregled_filmova():
	print("")
	print("==========================")
	print("Pregled dostupnih filmova") 
	print("==========================")
	file = open("film.txt","r")
	print(file.read())
	print(povratak())
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
	if 'x'== komanda.lower():
		print(menadzer())
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
	try:
		izlazak = int(input("[1]Da [2]Ne: "))
	except ValueError as err:
		print(menadzer())
	print("")
	if izlazak == 1:
		exit()
	elif izlazak == 2:
		return menadzer()
	else:
		print("Pogresna komanda")	
#########################################################################################
def odjava():
	print("")
	print("!!!!!!!!!!!!!!!!!")
	print("Da li ste sigurni")
	try:
		odj = int(input("[1]Da [2]Ne: "))
	except ValueError as err:
			print(menadzer())
	print("")
	if odj == 1:
		import Projekat
	elif odj == 2:
		return menadzer()
	else:
		print("Pogresna komanda")
		return odjava()
##########################################################################################
def menadzer():
	print("1) Pregled dostupnih filmova")
	print("2) Pretraga filmova")
	print("3) Pretraga projekcija")
	print("4) Unos projekcije i filma")
	print("5) Registracija novih prodavaca")
	print("6) Izvestavanje")
	print("7) Odjava")
	print("8) Izlaz")
	try:
		x = int(input("Uneti zeljenu opciju: "))
	except ValueError as err:
			print(menadzer())
	if x > 8 or x < 1:
		print("*******************************")
		print("Pogresna opcija pokusaj ponovo")
		print("*******************************")
		print(menadzer())
	elif x == 1:
		print(pregled_filmova())
	elif x == 2:
		print(pretraga_filmova())
	elif x == 3:
		print(pretraga_projekcija())
	elif x == 4:
		print(unos())
	elif x == 5:
		print(registrovanje_prodavaca())
	elif x == 6:
		print(izvestavanje())
	elif x == 7:
		print(odjava())
	elif x == 8:
		print(izlaz())
menadzer()
