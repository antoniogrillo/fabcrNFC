# fabcrNFC

# obiettivi:
l'applicazione permette di creare e rimuovere Account per ogni utente del FabLab e gestire i FabCR (FabLab CRedit) attraverso la chiave unica (UID) di tag NFC, MifareUltralight Card e alcuni smartphone dotati di NFC.
I crediti vengono aggiornati in locale nel db MySql. Alla creazione di ogni Account vengono caricati 25 FabCR.

Coming soon:

1) il db locale verrà condiviso con il db remoto del sito per permettere agli utenti di prenotare le macchine e visualizzare la propria situazione crediti.
2) le macchine dotate di client (in progettazione) permetteranno l'aggiornamento automatico dei crediti e l'abilitazione all'uso nel caso in cui: a) il numero di crediti sia sufficiente all'utilizzo della prima ora della macchina; b) abilitare solo gli utenti che oltre al numero di crediti necessario alla prima ora di funzionamento, siano taggati come abilitati per quella tecnologia.

# hardware:
raspberry pi 2
		
shield EXPLORE-NFC per Raspberry Pi 2 / B+

	https://www.element14.com/community/community/designcenter/explorenfc
	
# software:
installare raspbian

	https://www.raspberrypi.org/downloads/raspbian/
		
attivare SPI

	sudo raspi-config
	// Advanced Options > SPI > <Yes>.
	sudo reboot
		
installare le librerie NFC
scaricare il software necessario dal sito element14
decomprimerlo in una cartella e spostarsi nella cartella creata da terminale
installare i files come segue:

	sudo dpkg -i libneardal0_<version>_armhf.deb libwiringpi2-<version>_armhf.deb neard-explorenfc_<version>_armhf.deb

dove “<version>” va sostituito con la reale versione contenuta nel nome del file
	
installare wrapper "nxppy" di Scott Vitale, per l'interfacciamento tra Python e le lib. per EXPLORE-NFC 

	https://github.com/svvitale/nxppy
	
installare MySql

	sudo apt-get install mysql-server
		
creare utente e password per MySql

importare la struttura del db, file allegato:
	
	fabcr_utenti.sql
	
installare la libreria MySQLdb:

	apt-get install MySQLdb
	
ora possiamo avviare l'applicazione da terminale:

	sudo python fabCR.py