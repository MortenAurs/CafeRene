from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import font
from datetime import datetime
from tkinter import messagebox

try:
    # Kobler opp mot databasen
    mindatabase = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='Cafesjef',
                                  passwd='Caferene',
                                  db='Caferene2018')

    # Lager en funksjon med tidspunkt nå
    def hente_dato():
        dato = str(datetime.now())
        return dato

    # Lager en funksjon for å oppdatere totalsum (penger i kassen)
    def oppdater_totalsum():
        markor = mindatabase.cursor()
        markor.execute("SELECT Beløp FROM Solgt")
        totalsum = 500
        for r in markor:
            totalsum += r[0]

        markor.close()
        return totalsum

    # Lager en funksjon for å oppdatere menyen
    def oppdater_liste(tre_meny):
        tre_meny.delete(*tre_meny.get_children())
        # Kobler opp mot databasen og henter hele listen med en teller
        # på hvor mange ganger et produkt er solgt
        markor = mindatabase.cursor()
        markor.execute("SELECT Produkt.Produktnr, Produktnavn, Pris, COUNT(Solgt.Produktnr) AS Antall \
                        FROM Produkt LEFT JOIN Solgt \
                            ON Produkt.Produktnr = Solgt.Produktnr \
                            WHERE Tilgjengelighet IS NULL \
                            GROUP BY Produkt.Produktnr, Produktnavn, Pris")

        # Legger data inn i menylisten
        for r in markor:
            tre_meny.insert("", 0, values=(r[1],r[2],r[3]))
        # Returnerer variabelen så den kan hentes fra andre funksjoner
        markor.close()
        return tre_meny

    # Lager hovedfunksjonen
    def main():
        # Lager en funksjon det som skjer når man dobbelklikker i listen
        def dobbelklikk(event):
            # Denne skal gjøre nøyaktig det samme som selge funksjonen
            selge()

        # Lager en funksjon for oversikt over inntektene til de forskjellige kategoriene
        def kategori_oversikt():
            # Oppretter vindu og tittel
            katvindu = Toplevel()
            katvindu.title("Cafè Renè: Oversikt kategori")

            # Oppretter labels for overskrift og infotekst
            lbl_overskrift = Label(katvindu, text='Oversikt kategorier', font=arial_deloverskrift).grid(row=0, column=0, columnspan=5, padx=10, pady=(0,5))
            lbl_tekstinfo = Label(katvindu, wraplength=200, font=arial, text='Her er en oversikt over inntektene de forskjellige kategoriene har').grid(row=1, column=0, columnspan=2, padx=10, pady=(0,5))

            # Oppretter tekst og utdatafelt for kategoriene 
            kald_drikke = StringVar()
            ent_kald_drikke = Entry(katvindu, width=10, state='readonly', justify='center', textvariable=kald_drikke, font=arial).grid(row=2, column=1, sticky=W)
            lbl_kald_drikke = Label(katvindu, text='Kald drikke:', font=arial).grid(row=2, column=0, sticky=E)
            varm_drikke = StringVar()
            ent_varm_drikke = Entry(katvindu, width=10, state='readonly', justify='center', textvariable=varm_drikke, font=arial).grid(row=3, column=1, sticky=W)
            lbl_varm_drikke = Label(katvindu, text='Varm drikke:', font=arial).grid(row=3, column=0, sticky=E)
            middag = StringVar()
            ent_middag = Entry(katvindu, width=10, state='readonly', justify='center', textvariable=middag, font=arial).grid(row=4, column=1, sticky=W)
            lbl_middag = Label(katvindu, text='Middag:', font=arial).grid(row=4, column=0, sticky=E)
            boller = StringVar()
            ent_boller = Entry(katvindu, width=10, state='readonly', justify='center', textvariable=boller, font=arial).grid(row=5, column=1, sticky=W)
            lbl_boller = Label(katvindu, text='Boller/rundstykker:', font=arial).grid(row=5, column=0, sticky=E)
            dessert = StringVar()
            ent_dessert = Entry(katvindu, width=10, state='readonly', justify='center', textvariable=dessert, font=arial).grid(row=6, column=1, sticky=W)
            lbl_dessert = Label(katvindu, text='Dessert:', font=arial).grid(row=6, column=0, sticky=E)

            # Kobler opp mot databasen og henter KategoriID og Beløp fra solgte produkter
            markor = mindatabase.cursor()
            markor.execute("SELECT KategoriID, Beløp FROM Solgt, Produkt WHERE Solgt.Produktnr = Produkt.Produktnr")

            # Oppretter telle-variabler som settes til 0
            sum_kald_drikke = 0
            sum_varm_drikke = 0
            sum_middag = 0
            sum_boller = 0
            sum_dessert = 0
            for r in markor:
                if r[0] == '01':   #01 representerer Kategori 'Kald drikke'
                    # Øker kald_drikke telle-variabel med aktuelt beløp for hver gang KategoriID er 01
                    sum_kald_drikke += r[1]
                if r[0] == '02':    #02 representerer Kategori 'Varm drikke'
                    # Øker kald_drikke telle-variabel med aktuelt beløp for hver gang KategoriID er 02
                    sum_varm_drikke += r[1]
                if r[0] == '03':    #03 representerer Kategori 'Middag'
                    # Øker kald_drikke telle-variabel med aktuelt beløp for hver gang KategoriID er 03
                    sum_middag += r[1]
                if r[0] == '04':    #04 representerer Kategori 'Boller og rundstykker'
                    # Øker kald_drikke telle-variabel med aktuelt beløp for hver gang KategoriID er 04
                    sum_boller += r[1]
                if r[0] == '05':    #05 representerer Kategori 'Dessert'
                    # Øker kald_drikke telle-variabel med aktuelt beløp for hver gang KategoriID er 05
                    sum_dessert += r[1]

            # Legger variablene inn i utdatafeltene
            kald_drikke.set(str(sum_kald_drikke)+',-')
            varm_drikke.set(str(sum_varm_drikke)+',-')
            middag.set(str(sum_middag)+',-')
            boller.set(str(sum_boller)+',-')
            dessert.set(str(sum_dessert)+',-')
            
            markor.close()

            # Lager tilbakeknapp
            btn_avslutt = ttk.Button(katvindu, text='Tilbake', command=katvindu.destroy).grid(row=7, column=0, columnspan=2, padx=10, pady=(10,5), sticky=EW)

        # Lager en funksjon for å hente produktnr, produktnavn og pris når man klikker i listen
        def velge_vare(event):
            try:
                # Setter produkt til den raden man klikker i menyen
                produkt = tre_meny.selection()[0]
                produktnavn = tre_meny.item(produkt)['values'][0]

                # Oppretter markør og henter informasjon om alle produkter som er tilgjengelige
                markor = mindatabase.cursor()
                markor.execute("SELECT Produkt.Produktnr, Produktnavn, Pris, COUNT(Solgt.Produktnr) AS Antall \
                                FROM Produkt LEFT JOIN Solgt \
                                    ON Produkt.Produktnr = Solgt.Produktnr \
                                WHERE Tilgjengelighet IS NULL \
                                GROUP BY Produkt.Produktnr, Produktnavn, Pris")

                # Henter produktnummer og pris fra produkt-tabellen
                for r in markor:
                    if produktnavn == r[1]:
                        produktnr = r[0]
                        belop = r[2]
                # Legger produktnr, pris og produktnavn i set() her for å kunne hente den med get() i andre funksjoner        
                prodnr.set(produktnr)
                pris.set(belop)
                prodnavn.set(produktnavn)
                
                markor.close()
            # Legger inn en dummy exception da jeg får en feilmelding når jeg dobbelklikker
            # i lista om ikke denne er her
            except:
                pass

        # Lager funksjon for henting av produktnavn
        def hent_produktnavn():
            markor = mindatabase.cursor()
            markor.execute("SELECT Produktnr, Produktnavn FROM Produkt WHERE Tilgjengelighet IS NULL")

            produktnr = prodnr.get()
            produktnavn = ''
            for r in markor:
                if produktnr == r[0]:
                    produktnavn = r[1]

            markor.close()
            return produktnavn
                
        # Lager en funksjon for der som skjer når bruker trykker på selg-knappen    
        def selge():
            # Henter produknr og pris med en get()
            produktnr = prodnr.get()
            belop = pris.get()
            # Henter produktnavn fra hent_produktnavn funksjonen
            produktnavn = hent_produktnavn()
            if produktnavn != '':
                # Lager en pop-up box om bruker er sikker på de ønsker å selge det aktuelle produktet
                sikker = messagebox.askquestion("Spørsmål", "Er du sikker på at du vil selge '" + produktnavn + "'?")
                if sikker == 'yes':
                    # Henter dagens dato
                    dato = hente_dato()

                    # Genererer salgsnummer ved å hente siste registrerte 
                    # nummer i Solgt-tabellen og plusse på 1
                    markor = mindatabase.cursor()
                    markor.execute("SELECT Salgsnr FROM Solgt ORDER BY Salgsnr-0")

                    # Legger verdi 1 i salgsnr dersom solgt-tabellen er tom
                    salgsnr = 1
                    # Dersom det er varer i solgt-tabellen hentes
                    # det siste registrerte nummeret og legger til 1
                    for r in markor:
                        salgsnr = int(r[0]) + 1

                    # Legger data inn i Solgt-tabellen basert på tidligere oppgitte variabler
                    insert_solgt = ("INSERT INTO Solgt"
                                    "(Salgsnr, Produktnr, Tidspunkt, Beløp)"
                                    "VALUES(%s, %s, %s, %s)")
                    insert_var = (salgsnr, produktnr, dato, belop)
                    markor.execute(insert_solgt, insert_var)
                    mindatabase.commit()
                    markor.close()

                    # Oppdaterer meny med ny verdi i 'antall solgt' kolonne ved å kjøre oppdater_liste funsksjonen
                    oppdater_liste(tre_meny)

                    # Henter totalsummen fra oppdater_totalsum funksjonen
                    totalsum = str(oppdater_totalsum())
                    # Legger oppdatert totalsum-verdien inn i inndatafelt for penger i kassen
                    totalbelop.set(totalsum +',-')

                    # Lukker markør
                    markor.close()
                    messagebox.showinfo("Vellykket", "'" + produktnavn + "' er solgt!")
            else:
                # Dersom ingen valg er gjort i listen gis en feilmelding
                messagebox.showerror("Error","Vennligst velg produkt fra menyen")       

        # Oppretter funksjon hva som skjer når 'Fjern produkt' knappen blir trykt
        def fjern_produkt_vindu():
            # Leter i databasen etter siste oppdatert tabell slik at det kommer en feilmelding dersom
            # bruker har fjernet et produkt og klikker på 'Fjern produkt' uten å ha valgt nytt produkt fra lista
            markor = mindatabase.cursor()
            markor.execute("SELECT Produktnr, Produktnavn FROM Produkt WHERE Tilgjengelighet is NULL")
            soke_liste = []
            for r in markor:
                soke_liste += r
            produktnavn = prodnavn.get()
            markor.close()
            
            if produktnavn in soke_liste:
                # Ber bruker bekrefte at han ønsker å fjerne det aktuelle produktet
                sikker = messagebox.askquestion("Spørsmål", "Er du sikker på at du vil fjerne '" + produktnavn + "' fra menyen?")
                if sikker == 'yes':
                    # Henter produktnr med en get()
                    produktnr = prodnr.get()

                    # Oppdaterer status i produkt-tabellen
                    markor = mindatabase.cursor()
                    update_produkt = ("UPDATE Produkt \
                                      SET Tilgjengelighet = 'Fjernet' \
                                      WHERE Produktnr = %s")
                    update_var = (produktnr)
                    markor.execute(update_produkt, update_var)

                    mindatabase.commit()
                    markor.close()
                    
                    # Oppdaterer meny etter at produkt er fjernet
                    oppdater_liste(tre_meny)
                    # Gir en melding at prosessen var vellykket
                    messagebox.showinfo("Vellykket","'" + produktnavn + "' er fjernet fra menyen")
            else:
                # Gir en feilmelding dersom ingen produkt er valgt
                messagebox.showerror("Error","Vennligst velg et produkt fra menyen")

        # Oppretter funksjon for hva som skjer når 'Endre pris' knappen blir trykt    
        def endre_pris_vindu():
            def endre_pris():
                # Henter produktnr og pris med en get()
                produktnr = prodnr.get()
                nytt_belop = pris.get()

                # Sjekker at begge felt er fylt ut
                if produktnr != '' and nytt_belop != '':
                    # Henter produktnavn ved å kjøre hent_produktnavn funskjonen
                    produktnavn = hent_produktnavn()
                    # Dersom bruker har lagt inn pris med komma endres denne til punktum for å legge inn in databasen
                    nytt_belop = nytt_belop.replace(',','.')
                    try:
                        # Gjør nytt_belop om til en float for å legge den inn i databasen.
                        nytt_belop = float(nytt_belop)
                        if produktnavn != '':
                            # Ber bruker bekrefte at han er sikker
                            sikker = messagebox.askquestion("Spørsmål", "Er du sikker på at du vil endre \nprisen på '" + produktnavn + "' til " + "{0:.2f}".format(nytt_belop) + "kr?", parent=prisvindu)
                            if sikker == 'yes':
                                    # Oppdaterer status i produkt-tabellen
                                    markor = mindatabase.cursor()
                                    update_produkt = ("UPDATE Produkt \
                                                      SET Pris = %s \
                                                      WHERE Produktnr = %s")
                                    update_var = (nytt_belop, produktnr)
                                    markor.execute(update_produkt, update_var)

                                    mindatabase.commit()
                                    markor.close()
                                    
                                    # Oppdaterer meny etter at pris er endret
                                    oppdater_liste(tre_meny)
                                    # Gir en melding at prisendring er vellykket
                                    messagebox.showinfo("Vellykket", "Prisen på '" + produktnavn + "' er endret til " + "{0:.2f}".format(nytt_belop) + "kr", parent=prisvindu)
                        else:
                            # Gir beskjed at produktnr ikke finnes
                            messagebox.showerror("Error", "Produktnr finnes ikke.", parent=prisvindu)
                    except:
                        # Gir en feilmelding på ugyldig inndata på pris
                        messagebox.showerror("Error", "Ugyldig inndata på pris", parent=prisvindu)
                else:
                    # Ber bruker fylle ut begge inndatafelt
                    messagebox.showerror("Error", "Vennligst fyll ut både produktnr og pris.\nHusk du kan også velge fra listen i hovedvinduet", parent=prisvindu)
            
                
            # Oppretter hovedvindu
            prisvindu = Toplevel()
            prisvindu.title("Cafè Renè: Endre pris")

            # Oppretter labels for overskrift og infotekst
            lbl_overskrift = Label(prisvindu, text='Endre pris på produkt', font=arial_deloverskrift).grid(row=0, column=0, columnspan=3, padx=10, pady=(0,5))
            lbl_info = Label(prisvindu, justify='center', font=arial, wraplength=190, text='Skriv inn produktnr og ny pris på varen. Du kan også velge fra listen i hovedvinduet og så endre pris')
            lbl_info.grid(row=1, column=0, columnspan=3, pady=(0,5))

            # Oppretter tekst og inndatafelt for produktnr og pris
            lbl_produktnr = Label(prisvindu, text='Produktnr:', font=arial).grid(row=2, column=0, pady=(0,5), sticky=E)
            ent_produktnr = Entry(prisvindu, width=5, textvariable=prodnr, font=arial, justify='center').grid(row=2, column=1, pady=(0,5), sticky=W)
            lbl_pris = Label(prisvindu, text='Pris:', font=arial).grid(row=3, column=0, pady=(0,5), sticky=E)
            ent_pris = Entry(prisvindu, width=5, textvariable=pris, font=arial, justify='center').grid(row=3, column=1, pady=(0,5), sticky=W)

            # Oppretter knapp for endring av pris
            btn_pris = ttk.Button(prisvindu, width=16, text='Oppdater', command=endre_pris)
            btn_pris.grid(row=5, column=0, columnspan=3, pady=5)

            # Oppretter tilbakeknapp
            btn_avslutt = ttk.Button(prisvindu, text='Tilbake', command=prisvindu.destroy)
            btn_avslutt.grid(row=6, column=0, columnspan=3, padx=10, pady=(5,5), sticky=EW)

        # Oppretter funksjon for hva som skjer når 'Nytt produkt' knappen blir trykt
        def nytt_produkt_vindu():
            def velge_kategori(event):
                # Henter data fra kategoriliste
                valgt_kategori = cmb_kategori.get()

                # Henter KategoriID
                markor = mindatabase.cursor()
                markor.execute("SELECT * FROM Kategori")

                for r in markor:
                    if r[1] == valgt_kategori:
                        kategoriid = r[0]

                markor.close()
                       
                katid.set(kategoriid)
                
            def registrer_produkt():
                # Henter informasjon fra inndatafeltene
                valgt_pris = pris.get()
                kategoriid = katid.get()
                produktnavn = prodnavn.get()
                # Dersom bruker har brukt punktum i produktnavn (for eksempel Cola 0.5l) endres dette til komma (Cola 0,5l)
                produktnavn = produktnavn.replace(".", ",")
                # Dersom bruker har brukt komma i pris (for eksempel Farris 0,5l) endres dette til punktum (Cola 0.5l) for å
                # kunne legges inn i databasen
                valgt_pris = valgt_pris.replace(",", ".")

                # Sjekker at produktnavn har verdi
                if produktnavn != '':
                    # Sjekker at kategori har verdi
                    if kategoriid != '':
                        # Oppretter markør og kobler mot databasen for å finne om produkt finnes fra før
                        markor= mindatabase.cursor()
                        markor.execute("SELECT Produktnavn, Produktnr, Tilgjengelighet FROM Produkt")
                        
                        produkt_finnes = False
                        produkt_fjernet = False
                        for r in markor:
                            # Dersom produkt finnes og Tilgjengelighet er satt til 'None' settes produkt_finnes til True
                            if produktnavn == r[0] and r[2] is None:
                                produkt_finnes = True
                            # Dersom produkt finnes og Tilgjengelighet er satt til 'Not None' (som betyr at den er fjernet) settes produkt_fjernet til True
                            elif produktnavn == r[0] and r[2] is not None:
                                produkt_fjernet = True
                                # Henter produktnr for å kunne bruke det eksisterende produktnr'et og oppdatere databasen istedenfor å legge til ny rad
                                produktnr = r[1]
                        if produkt_finnes:
                            # Dersom produkt finnes gis en feilmelding
                            messagebox.showerror("Error", "'" + produktnavn + "' finnes allerede i menyen", parent=produktvindu)
                        elif produkt_fjernet:
                            # Dersom produktet finnes, men har Tilgjengelighet satt til 'Fjernet' oppdateres det eksisterende produktet
                            markor = mindatabase.cursor()
                            update_produkt = ("UPDATE Produkt \
                                               SET Tilgjengelighet = NULL, Pris = %s \
                                               WHERE Produktnr = %s")
                            update_var = (valgt_pris, produktnr)
                            markor.execute(update_produkt, update_var)
                            mindatabase.commit()
                            markor.close()

                            # Oppdaterer menyen                        
                            oppdater_liste(tre_meny)
                            # Gir beskjed at produkt er lagt til i menyen
                            messagebox.showinfo("Vellykket", "'" +  produktnavn + "' er lagt til menyen!", parent=produktvindu)

                        else:
                            # Dersom produkt ikke finnes fra før blir det lagt til en ny rad
                            try:
                                # Genererer produtktnummer ved å hente siste registrerte 
                                # produktnummer i Produkt-tabellen og plusse på 1
                                markor = mindatabase.cursor()
                                markor.execute("SELECT Produktnr, Tilgjengelighet FROM Produkt ORDER BY Produktnr-0")

                                # Legger verdi 1 i prodnr dersom det ikke er noen varer i produkt-tabellen
                                prodnr = 1
                                # Dersom det er varer i produkt-tabellen hentes
                                # det siste registrerte nummeret og legger til 1
                                for r in markor:
                                    prodnr = int(r[0]) + 1

                                # Oppretter markør og legger data inn i databasetabellen med oppgitte verdier
                                markor = mindatabase.cursor()
                                insert_produkt = ("INSERT INTO Produkt"
                                                  "(Produktnr, Produktnavn, KategoriID, Pris, Tilgjengelighet)"
                                                  "VALUES(%s, %s, %s, %s, NULL)")
                                insert_var = (prodnr, produktnavn, kategoriid, valgt_pris)
                                markor.execute(insert_produkt, insert_var)
                                mindatabase.commit()
                                markor.close()

                                # Oppdaterer menyen
                                oppdater_liste(tre_meny)
                                # Gir en beskjed at produkt er lagt til i menyen
                                messagebox.showinfo("Vellykket", produktnavn + " er lagt til menyen!", parent=produktvindu)
                            except:
                                # Dersom bruker har oppgitt ugyldig data for pris gis en feilmelding
                                messagebox.showerror("Error", "Ugyldig inndata på pris!", parent=produktvindu)
                    else:
                        # Dersom kategori ikke har verdi gis en feilmelding
                        messagebox.showerror("Error", "Vennligst velg kategori fra listen!", parent=produktvindu)
                else:
                    # Dersom produktnavn ikke har verdi gis en feilmelding
                    messagebox.showerror("Error", "Produktnavn kan ikke være tom!", parent=produktvindu)
                  
            # Oppretter hovedvindu
            produktvindu = Toplevel()
            produktvindu.title("Cafè Renè: Nytt produkt")

            # Oppretter labels for overskrift og tekstinfo
            lbl_overskrift = Label(produktvindu, text='Legg til nytt produkt', font=arial_deloverskrift)
            lbl_overskrift.grid(columnspan=2, pady=(0,5))
            lbl_tekstinfo = Label(produktvindu, wraplength=260, text='Her kan du legge til et nytt produkt ved å skrive inn produktnavn, velge kategori og pris.', font=arial)
            lbl_tekstinfo.grid(row=1, column=0, columnspan=2)

            # Oppretter label og inndatafelt for produktnavn
            prodnavn = StringVar()
            lbl_produktnavn = Label(produktvindu, text='Produktnavn:', font=arial).grid(row=2, column=0, padx=(10,0), pady=(0,5), sticky=E)
            ent_produktnr = Entry(produktvindu, width=27, textvariable=prodnavn, justify='center').grid(row=2, column=1, padx=(0,10), pady=(0,5), sticky=E)

            # Oppretter label og combobox (nedtrekksliste) for kategorier
            kategori = StringVar()
            lbl_kategori = Label(produktvindu, text='Kategori:', font=arial).grid(row=3, column=0, pady=(0,5), sticky=E)
            cmb_kategori = ttk.Combobox(produktvindu, width=20, state='readonly', justify='center', textvariable=kategori, font=arial)
            cmb_kategori.grid(row=3, column=1, padx=(0,10), pady=(0,5), sticky=EW)

            # Oppretter variabel for å hente kategoriid
            katid = StringVar()
            ent_katid = Entry(produktvindu, textvariable=katid, font=arial)

            # Henter informasjon fra databasen hva som skal være i kategori-listen
            markor = mindatabase.cursor()
            markor.execute("SELECT Kategorinavn FROM Kategori")
            kategori_liste = []
            for r in markor:
                # Lager en liste med kategoriene
                kategori_liste += r
            # Legger lista inn i comboboxen (nedtrekkslista)
            cmb_kategori['values'] = (kategori_liste)
            cmb_kategori.bind('<<ComboboxSelected>>', velge_kategori)

            markor.close()

            # Oppretter label og inndatafelt for pris
            pris = StringVar()
            lbl_pris = Label(produktvindu, text='Pris:', font=arial).grid(row=4, column=0, pady=(0,5), sticky=E)
            ent_pris = Entry(produktvindu, width=5, textvariable=pris, font=arial, justify='center').grid(row=4, column=1, pady=(0,5), sticky=W)

            # Oppretter knapp for registrering
            btn_registrer = ttk.Button(produktvindu, width=16, text='Registrer', command=registrer_produkt).grid(row=5, column=0, columnspan=3, pady=(5,5))
            # Oppretter tilbakeknapp
            btn_tilbake = ttk.Button(produktvindu, text='Tilbake', command=produktvindu.destroy).grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky=EW)

        # Oppretter hovedvindu
        hovedvindu = Tk()
        hovedvindu.title("Cafè Renè")
        
        # Oppretter diverse fonter som skal brukes
        arial_overskrift = font.Font(family='Arial', size=20)
        arial_deloverskrift = font.Font(family='Arial', size=15)
        arial = font.Font(family='Arial', size=10)
        arial_kursiv = font.Font(family='Arial', size=10, slant='italic')

        # Lager labels for overskrift og tekstinfo
        lbl_overskrift = Label(hovedvindu, text='Cafè Renè', font=arial_overskrift).grid(row=0, column=0, columnspan=4, pady=(0,5))
        lbl_tekstinfo = Label(hovedvindu, height=4, wraplength=320, text='Velkommen til Cafè Renè administrasjonssystem.\nFor å selge et produkt kan du enten dobbelklikke på produktet du ønsker å selge, eller så kan du velge produkt fra listen og klikke på selg produkt knappen.', font=arial).grid(row=1, column=0, columnspan=4, pady=(0,5))

        # Oppretter scroll-funksjon til menylisten
        y_scroll_meny = Scrollbar(hovedvindu, orient=VERTICAL)
        y_scroll_meny.grid(row=2, rowspan=3, column=3, padx=(00,10), sticky=(NS, E))

        # Oppretter menyliste som en treeview
        tre_meny = ttk.Treeview(hovedvindu, yscrollcommand=y_scroll_meny.set)
        tre_meny.column("#0", width=0)
        tre_meny.grid(row=2, rowspan=3, column=0, columnspan=4, padx=(11,26), sticky=EW)
        # Kobler meny mot scrollbar
        y_scroll_meny["command"]=tre_meny.yview
     
        # Definerer anall kolonner, oppretter kolonnene og gir de ønsket størrelse og navn
        tre_meny["columns"]=("1","2","3",)
        tre_meny.column("1", width=150)
        tre_meny.heading("1", text="Produkt", anchor=W)
        tre_meny.column("2", width=50, anchor=E)
        tre_meny.heading("2", text="  Pris")
        tre_meny.column("3", width=90, anchor=CENTER)
        tre_meny.heading("3", text="Antall solgt")

        # Fyller meny med innhold ved å hente verdi fra oppdater_liste funksjonen
        tre_meny = oppdater_liste(tre_meny)

        # Oppretter kobling for hva som skjer når man klikker på et produkt i menyen
        tre_meny.bind('<ButtonRelease-1>', velge_vare)
        # Oppretter kobling for hva som skjer når man dobbelklikker på et produkt i menyen
        tre_meny.bind('<Double-Button-1>', dobbelklikk)

        # Oppretter knapp for salg av produkt
        btn_selg = ttk.Button(hovedvindu, text='Selg produkt', command=selge).grid(row=5, column=0, columnspan=4, padx=10, sticky=EW)

        # Oppretter knapper for nytt produkt, endre pris, fjern produkt og kategorioversikt
        btn_ny = ttk.Button(hovedvindu, width=27, text='Nytt produkt', command=nytt_produkt_vindu).grid(row=6, column=0, columnspan=2, padx=(10,0))
        btn_pris = ttk.Button(hovedvindu, width=27, text='Endre pris', command=endre_pris_vindu).grid(row=6, column=2, columnspan=2, padx=(0,10))
        btn_fjern = ttk.Button(hovedvindu, text='Fjern produkt', command=fjern_produkt_vindu).grid(row=7, column=0, columnspan=2, padx=(10,0), sticky=EW)
        btn_kategori = ttk.Button(hovedvindu, text='Kategorioversikt', command=kategori_oversikt).grid(row=7, column=2, columnspan=2, padx=(0,10), sticky=EW)

        # Oppretter variabel for henting av totalbeløp (penger i kassen) som skal vises på fremsiden
        totalbelop = StringVar()
        # Oppretter tekst- og inndatafelt for penger i kassen
        lbl_totalbelop = Label(hovedvindu, text='Penger i kassen:', font=arial_kursiv).grid(row=8, column=2, pady=(5,0), sticky=W)
        ent_totalbelop = Entry(hovedvindu, border=0, width=9, state='readonly', textvariable=totalbelop, justify='right', font=arial_kursiv).grid(row=8, column=2, columnspan=2, padx=(0,12), pady=(5,0), sticky=E)
        # Henter totalsummen fra oppdater_totalsum funksjonen
        totalsum = str(oppdater_totalsum())
        # Legger totalsum-verdien inn i inndatafelt for penger i kassen og legger til ,- for syns skyld
        totalbelop.set(totalsum +',-')
           
        # Oppretter entryfelt for å hente produktnr og pris
        prodnr = StringVar()
        ent_produktnr = Entry(hovedvindu, textvariable = prodnr, font=arial)
        pris = StringVar()
        ent_belop = Entry(hovedvindu, textvariable = pris, font=arial)
        prodnavn = StringVar()
        ent_produktnavn = Entry(hovedvindu, textvariable = prodnavn, font=arial)

        # Oppretter knapp for å avslutte programmet
        btn_avslutt = ttk.Button(hovedvindu, text='Avslutt', command=hovedvindu.destroy).grid(row=10, column=0, columnspan=4, padx=10, pady=5, sticky=(NS,EW))

        hovedvindu.mainloop()

    # Kaller på main funksjon
    main()
    # Stenger databasekoblingen
    mindatabase.close()

except pymysql.InternalError:
    messagebox.showerror("Error", "Database finnes ikke")
except pymysql.ProgrammingError:
    messagebox.showerror("Error", "Problemer med tabellene i databasen")

