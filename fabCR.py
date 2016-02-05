import nxppy
import time
import pycurl
import MySQLdb

vuoto = 'null'
puntiLetti = 0
nome = ""
mifare = nxppy.Mifare()
# Definisco i parametri di connessione al db
dbHost   = "localhost"
dbUser   = "root"
dbPwd    = "toor"
dbDbName = "fabcr"
# Mi collego al db
db = MySQLdb.connect(dbHost, dbUser, dbPwd, dbDbName)
# Pulisco la finestra del terminale con due sequenze di escape
print chr(27) + "[2J" + chr(27) + "[1;1H"
# Mi presento, sono FabCR Manager e questo e' il mio MENU
print "FabCR Manager MENU: \n"

def leggi_carta ():
    while True:
        try:
            uid = mifare.select()
            if uid:
                return uid
                break
        except nxppy.SelectError:
            pass
    time.sleep(1)

def dbConnect ():
    print '-Connessioe al DB-'
    print '-DB Connesso-'
    
def creaUtente():
    print '-Crea Utente-'
    nome = raw_input("Digita il Nome per il nuovo Account: ")
    print "=== Passa la Carta o lo Smartphone sul Lettore ==="
    uid = leggi_carta()
    cur = db.cursor()
    cur.execute("INSERT INTO utenti (uid, nome_utente, punti) VALUES (%s,%s,%s)",(uid, nome, 25))
    db.commit()
    cur.close()
    print '-Utente Creato-'
    time.sleep(1)
    menu()
    
def eliminaUtente():
    print '-Elimina Utente-'
    print "=== Passa la Carta o lo Smartphone sul Lettore ==="
    uid = leggi_carta()
    cur = db.cursor()
    cur.execute("DELETE FROM utenti WHERE uid=%s", (uid))
    db.commit()
    cur.close()
    print '-Utente Eliminato-'
    time.sleep(1)
    menu()

def gestisciPunti():
    print '-Aggiorna Punti Utente-'
    print "=== Passa la Carta o lo Smartphone sul Lettore ==="
    uid = leggi_carta()
    cur = db.cursor()
    cur.execute("SELECT punti FROM utenti WHERE uid=%s",(uid))
    puntiLetti = cur.fetchone()
    print puntiLetti[0]
    punti = input("Inserisci i punti: ")
    puntiTot = (puntiLetti[0]+punti)
    cur.execute("UPDATE utenti SET punti=%s WHERE uid=%s",(puntiTot, uid))
    db.commit()
    cur.close()
    time.sleep(1)
    print str(puntiTot)+(" FabCR associati al Profilo")
    time.sleep(2)
    menu()

def menu():
    print chr(27) + "[2J" + chr(27) + "[1;1H"
    print "FabCR Manager MENU: \n"
    print '[1] Crea Utente'
    print '[2] Elimina Utente'
    print '[3] Gestisci Punti'
    options[input('\n Inserisci Scelta menu: ')]()
    
     
options = {1: creaUtente,
           2: eliminaUtente,
           3: gestisciPunti,
}
print '[1] Crea Utente'
print '[2] Elimina Utente'
print '[3] Gestisci Punti'

options[input('\n Inserisci Scelta menu: ')]()



 

    
