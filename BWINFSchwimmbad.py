

def familienkarte1(daten):
	anzahlJugendliche=int(daten[0])-2
	anzahlErwachsene=int(daten[1])-2
	preis=int(daten[2])+8
	anzahlFamilienkarten=int(daten[3])+1
	return [anzahlJugendliche,anzahlErwachsene,preis,anzahlFamilienkarten,daten[4]]
"""
def preisFamilienkarte1(daten):
	anzahlJugendliche=int(daten[0])-2
	anzahlErwachsene=int(daten[1])-2
	preis=int(daten[2])+8
	anzahlFamilienkarten=int(daten[3])+1
	return daten[2]

def preisFamilienkarte2(daten):
	anzahlJugendliche=int(daten[0])-3
	anzahlErwachsene=int(daten[1])-1
	preis=int(daten[2])+8
	anzahlFamilienkarten=int(daten[3])+1
	return daten[2]
"""
def familienkarte2(daten):
	anzahlJugendliche=int(daten[0])-3
	anzahlErwachsene=int(daten[1])-1
	preis=int(daten[2])+8
	anzahlFamilienkarten=int(daten[3])+1
	return [anzahlJugendliche,anzahlErwachsene,preis,anzahlFamilienkarten,daten[4]]


def gutscheinberechnen(daten,ferien,kinderKarten,erwachsenenKarten,anzahlGutscheine):
	if not ferien:
		while daten[4] > 0 and anzahlGutscheine > 0:
			daten[4]-=1
			anzahlGutscheine-=1
			daten[2]-=0.8
		while daten[3] > 0 and anzahlGutscheine > 0:
			daten[3]-=1
			anzahlGutscheine-=1
			daten[2]-=1.1
		while erwachsenenKarten > 0 and anzahlGutscheine > 0:
			erwachsenenKarten-=1
			anzahlGutscheine-=1
			daten[2]-=0.35
		while kinderKarten > 0 and anzahlGutscheine > 0:
			kinderKarten-=1
			anzahlGutscheine-=1
			daten[2]-=0.25
	return daten[2]


def gruppenkarte(daten):
#möglichst Familienkarte übrig lassen
"""
	if daten[1] > 7 and daten[0] > 2:
		daten[1]-=6
		daten[4]+=1
		daten[2]+=11
	elif daten[1] > 8 and daten[0] >= 1:
		daten[1]-=6
		daten[4]+=1
		daten[2]+=11
	elif daten[1]<=2 and daten[0] > 7:
		daten[0]-=6
		daten[2]+=11
		daten[4]+=1
	elif daten[0]+daten[1]==6:
		daten[1]=0
		daten[0]=0
		daten[2]+=11
		daten[4]+=1
	elif daten[1]>=6:
		daten[1]-=6
		daten[2]+=11
		daten[4]+=1
	elif daten[0] + daten[1] >= 7 and ((daten[1] >= 1 and daten[0] >= 3) or (daten[1] >= 1 and daten[0] >= 3)):
"""
	while daten[0] + datn[1] >= 12:
		for i in range(6):
			if daten[1] >= daten[0]:
				daten[1]-=1
			else:
				daten[0]-=1
		daten[4]+=1
		daten[2]+=11
"""        print("Gruppenkartenfehler")
	preistemporaer=daten[0]*2.5+daten[1]*3.5
	testdaten1=daten
	if daten[1] >= 2 and daten[0] >= 2:
		testdaten1=familienkarte1(daten)
"""    
	return daten

while True:
	personen=[]
	anzahlPersonen=int(input("Wie viele Personen? "))
#Wochentag/Ferien?
	wochenende=True
	if input("Wochenende? j/n ")!= "j":
		wochenende=False
	ferien=True
	if input("Ferien? j/n ")!= "j":
		ferien=False
#Gutschein?
	anzahlGutscheine=int(input("wie viele Gutscheine? "))
#Personen abfragen
	for i in range(anzahlPersonen):
		print("Alter der",str(i+1)+". Person: ",end="")
		personen+=[int(input())]
#Personen nach Alter einstufen
	anzahlKleinkinder=0
	anzahlJugendliche=0
	anzahlErwachsene=0
	for element in personen:
		print(element)
		if element >= 0 and element < 4:
			anzahlKleinkinder += 1
		elif element >= 4 and element < 16:
			anzahlJugendliche += 1
		elif element >= 16:
			anzahlErwachsene += 1
		else:
			print("Schwachsinn!")
	print("Erwachsene: ", anzahlErwachsene, "  Jugendliche: ", anzahlJugendliche, "  Kleinkinder: ", anzahlKleinkinder)
	if anzahlErwachsene<anzahlKleinkinder:
		print("Nicht genügend Begleitpersonen!")
		break
	daten=[anzahlJugendliche,anzahlErwachsene,0,0,0]
#daten[0]=anzahlJugendliche
#daten[1]=anzahlErwachsene
#daten[2]=preis
#daten[3]=anzahlFamilienkarten
#daten[4]=anzahlTageskarten
	kinderKarten=0
	erwachsenenKarten=0
	if not wochenende:
#kein Wochenende
#Gruppenkarte IMMER günstiger als Familienkarte
		daten=gruppenkarte(daten)
		if daten[0]>=2 and daten[1]>=2:
			datentemp1=familienkarte1(daten)
			if datentemp1[0]*2+daten[1]*2.8>11:
				datentemp1[1]=0
				datentemp1[0]=0
				datentemp1[4]+=1
			else:
		if daten[0]>=3 and daten[1]>=1:
			datentemp2=familienkarte2(daten)
			if datentemp2[0]*2+daten[1]*2.8>11:
				datentemp2[1]=0
				datentemp2[0]=0
				datentemp2[4]+=1
		if daten[0]>=4 and daten[1]>=4:
			datentemp3=familienkarte1(familienkarte1(daten))
		if daten[0]>=5 and daten[1]>=3:
			datentemp4=familienkarte1(familienkarte2(daten))
		if daten[0]>=6 and daten[1]>=2:
			datentemp5=familienkarte2(familienkarte2(daten))
		datentemp6=daten
		datentemp6[4]+=1
		for i in range(6):
			if datentemp6[1]>0:
				datentemp6[1]-=1
			else:
				datentemp6[0]-=1
		datentemp6[4]+=1
		datentemp6[2]+=11
		datentemp7=datentemp6
		datentemp7[4]+=1
		for i in range(6):
			if datentemp7[1]>0:
				datentemp7[1]-=1
			elif daten[0]>1:
				datentemp7[0]-=1
		datentemp7[4]+=1
		datentemp7[2]+=11
		datentemp=[datentemp1, datentemp2, datentemp3, datentemp4, datentemp5, datentemp6, datentemp7] 
		for element in datentemp:
			if element[2]+element[0]*2+element[1]*2.8 < daten[2]+daten[0]*2+daten[1]*2.8:
				daten=element
		daten[2]+=daten[0]*2+daten[1]*2.8
		kinderKarten=daten[0]
		erwachsenenKarten=daten[1]
"""
		while daten[0]+daten[1] >= 6:
			daten=gruppenkarte(daten)
		if daten[0]>=2 and daten[1]>=2:
			daten=familienkarte1(daten)
		elif daten[0] >=3 and daten[1] >=1:
			daten=familienkarte2(daten)
		if 11<=daten[0]*2.5+(daten[1]*3.5):
			daten[2]+=11
		else:
			if daten[0]*2.5+(daten[1]*3.5) < 11:
				daten[2]+=daten[0]*2.5+(daten[1]*3.5)*4/5
			else:
				daten[2]+=11
			kinderKarten=daten[0]
			erwachsenenKarten=daten[1]
"""
#Wochenende
	else:
		if daten[1]>=daten[0]:
			while daten[0]>1:
				daten=familienkarte1(daten)
		elif daten[0]>=3*daten[1]:
			while daten[1]>0:
				daten=familienkarte2(daten)
		else:
			while daten[0]>daten[1]+1:
				daten=familienkarte2(daten)
			while daten[0] >= 2 and daten[1] >= 2:
				daten = familienkarte1(daten)
		daten[2]+=daten[0]*2.5+(daten[1]*3.5)
		kinderKarten=daten[0]
		erwachsenenKarten=daten[1]
#Gutschein        
	preis=gutscheinberechnen(daten,ferien,kinderKarten,erwachsenenKarten,anzahlGutscheine)
	print("Preis: ",round(preis,2),"€ Karten:", daten[3],"Familienkarten, ",daten[4]," Tageskarten, ",kinderKarten," Kinderkarten und ",erwachsenenKarten," Erwachsenenkarten. ",end="")
	print("")
	if input("Wiederholen? j/n") != "j":
		break
