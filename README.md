# fabcrNFC

# obiettivi:
l'applicazione permette di creare e rimuovere Account per ogni utente del FabLab e gestire i FabCR (FabLab CRedit) attraverso la chiave unica di tag NFC, MifareUltralight Card e alcuni smartphone dotati di NFC.
I crediti vengono aggiornati in locale nel db MySql
 
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
		
		dove “<version>” va sostituito con la reale versione contenuta nel nome del file.
	
	installare wrapper "nxppy" di Scott Vitale, per l'interfacciamento tra Python e le lib. per EXPLORE-NFC 
		https://github.com/svvitale/nxppy
	
	
	installare MySql
		sudo apt-get install mysql-server
		
	creazione del database:
		###
	
ora possiamo avviare l'applicazione da terminale:

	sudo python fabCR.py