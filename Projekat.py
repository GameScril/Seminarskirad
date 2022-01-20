def prijava(ime_fajla):
	korisnicko_ime = input("Korisnicko ime: ")
	lozinka = input("Lozinka: ")
	fajl = open(ime_fajla,"r")
	for red in fajl.readlines():
		c = red.strip().split("|")
		korisnik = c[0]
		lozinkaa = c[1]
		ime = c[2]
		prezime = c[3]
		uloga = c[4].rstrip()
		if korisnicko_ime == korisnik and lozinka == lozinkaa:
			print("***********************")
			print("Uspesno ste prijavljeni")
			print("***********************")
			print(ime + " " + prezime + " " + uloga)
			print("Dobro dosli")
			print("-----------------------")
			if uloga == "kupac":
				import Kupac
			elif uloga == "prodavac":
				import Prodavac
			elif uloga == "menadzer":
				import Menadzer
	if korisnicko_ime != korisnik or lozinka != lozinkaa:
		print("-----------------------------------")
		print("Pogresno korisnicko ime ili lozinka")
		print("-----------------------------------")
		return glavna_funkcija()
	fajl.close
##########Funkcija za korisnicko ime za registraciju
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
			print(glavna_funkcija())
	fajl.close
	fajl = open("korisnici.txt","a")
	fajl.write(korisnicko_ime)
	fajl.write("|")
	fajl.close
	return "--------------------------------------------------------------------------------------"
############Funkcija za lozinku
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
		return glavna_funkcija()			
	fajl = open("korisnici.txt","a")
	fajl.write(lozinka)
	fajl.write("|")
	fajl.close
	return "----------------------------------------------------------------------------------------------------------"
###########GLAVNA FUNKCIJA
def glavna_funkcija():
	print("Nakon registracije novog korisnika aplikacija se gasi zbog ucitavanja novog korisnika")
	print("=====================================")
	print("1-Registrovanje")
	print("2-Uloguj se")
	x = input("Uneti opciju po zelji: ")
	print("=====================================")
	if x == "1":
##########REGISTRACIJA
		print("Registracija")
##########KORISNICKO IME
		print(Korisnicko_ime("korisnici.txt"))		
##########LOZINKA
		print(Lozinka())
###########IME I PREEZIME
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
		fajl.write("kupac")
		fajl.write("\n")
		fajl.close
		print("USPESNO STE REGISTROVANI")
		print("DOBRO DOSLI!")
 ###########Prijava
	if x == "2":
		print(prijava("korisnici.txt"))
	elif x != "1" and x != "2":
		print("Nepoznata komanda")
		print(glavna_funkcija())
glavna_funkcija()	
