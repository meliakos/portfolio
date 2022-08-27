#PRG1100-Oblig2-AMHK

from tkinter import *
import mysql.connector
from mysql.connector.errors import DatabaseError


def open_legg_student_vindu():
    
    def finn_studentnr():
        #Finner siste studentnr og kalkulerer et nytt
        siste_studentnr=0
        finne_studentnr_markor=mindatabase.cursor()
        
        finne_studentnr_markor.execute("SELECT MAX(Studentnr) FROM Student")
        
        for rad in finne_studentnr_markor:
            siste_studentnr += int(rad[0])
        
        studentnr.set(siste_studentnr+1)
        
        
        finne_studentnr_markor.close()

    def lagre_student():
        try:
            #Legger til studentinformasjonen
            legg_til_student_markor=mindatabase.cursor()
            
            legg_til = ("INSERT INTO Student"
                        "(Studentnr,Fornavn,Etternavn,Epost,Telefon)"
                        "VALUES(%s,%s,%s,%s,%s)"
                        )
            
            data_ny_student = (studentnr.get(),fornavn.get(),etternavn.get(),epost.get(),telefon.get())
            
            legg_til_student_markor.execute(legg_til,data_ny_student)
            
            mindatabase.commit()

            tilbakemelding_vindu=Toplevel(legg_student_vindu)
            tilbakemelding_vindu.title('Lagring utført')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Studenten ble lagret i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()
            legg_til_student_markor.close()
            
        except DatabaseError:
            
            tilbakemelding_vindu=Toplevel(legg_student_vindu)
            tilbakemelding_vindu.title('Lagring feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()        




    legg_student_vindu=Toplevel(window)
    legg_student_vindu.title('Legg til student')


    lbl_studentnr=Label(legg_student_vindu,text='Nytt studentnr: ')
    lbl_studentnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    studentnr=StringVar()
    ent_studentnr=Entry(legg_student_vindu, width=6, textvariable=studentnr)
    ent_studentnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)
    
    btn_studentnr=Button(legg_student_vindu,text='Kalkuler nytt studentnr',command=finn_studentnr)
    btn_studentnr.grid(row=1,column=1,padx=5,pady=5,sticky=E)

    lbl_fornavn=Label(legg_student_vindu, text='Oppgi fornavn: ')
    lbl_fornavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    fornavn=StringVar()
    ent_fornavn=Entry(legg_student_vindu, width=10, textvariable=fornavn)
    ent_fornavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_etternavn=Label(legg_student_vindu, text='Oppgi etternavn: ')
    lbl_etternavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    etternavn=StringVar()
    ent_etternavn=Entry(legg_student_vindu, width=10, textvariable=etternavn)
    ent_etternavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_epost=Label(legg_student_vindu,text='Oppgi e-post: ')
    lbl_epost.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    epost=StringVar()
    ent_epost=Entry(legg_student_vindu, width=15, textvariable=epost)
    ent_epost.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_telefon=Label(legg_student_vindu, text='Oppgi telefon: ')
    lbl_telefon.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    telefon=StringVar()
    ent_telefon=Entry(legg_student_vindu, width=10, textvariable=telefon)
    ent_telefon.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    #Lagre-knapp
    btn_lagre=Button(legg_student_vindu, text='Lagre student',command=lagre_student)
    btn_lagre.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Avslutt-knapp
    btn_avslutt=Button(legg_student_vindu, text='Tilbake',command=legg_student_vindu.destroy)
    btn_avslutt.grid(row=8, column=2, padx=5, pady=(20,5),sticky=E)




    legg_student_vindu.mainloop()


def open_endre_student_vindu():
    
    def finn_student():
        #Finner studentinformasjon
        funnet=False
        valgt=studentnr.get()
        
        finne_student_markor=mindatabase.cursor()
        finne_student_markor.execute("SELECT * FROM Student")
        
        for row in finne_student_markor:
            if valgt == row[0]:
                fornavn.set(row[1])
                etternavn.set(row[2])
                epost.set(row[3])
                telefon.set(row[4])
                funnet=True
                
        finne_student_markor.close()
        
        if not funnet:
            
            tilbakemelding_vindu=Toplevel(endre_student_vindu)
            tilbakemelding_vindu.title('Fant ikke studentnr')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Kunne ikke finne studentnummeret i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()        
            
    def lagre_student():
        try:
            #Legger til oppdatert info i databasen
            data_studentnr=studentnr.get()
            data_fornavn=fornavn.get()
            data_etternavn=etternavn.get()
            data_epost=epost.get()
            data_telefon=telefon.get()
            
            
            legg_til_student_markor=mindatabase.cursor()
            
            
            legg_til= """ UPDATE Student 
                        SET Fornavn = '%s', Etternavn = '%s', Epost = '%s', Telefon = '%s'
                        WHERE Studentnr = '%s' """ % (data_fornavn,data_etternavn,data_epost,data_telefon,data_studentnr)
            
            legg_til_student_markor.execute(legg_til)
            
            mindatabase.commit()
            
            legg_til_student_markor.close()

            tilbakemelding_vindu=Toplevel(endre_student_vindu)
            tilbakemelding_vindu.title('Lagring utført')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Studenten ble lagret i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()
            
        except DatabaseError:
            
            tilbakemelding_vindu=Toplevel(endre_student_vindu)
            tilbakemelding_vindu.title('Lagring feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()               



    endre_student_vindu=Toplevel(window)
    endre_student_vindu.title('Oppdater informasjon om student')

    lbl_studentnr=Label(endre_student_vindu,text='Oppgi studentnr: ')
    lbl_studentnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    studentnr=StringVar()
    ent_studentnr=Entry(endre_student_vindu, width=6, textvariable=studentnr)
    ent_studentnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btn_finn=Button(endre_student_vindu,text='Finn student',command=finn_student)
    btn_finn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lbl_fornavn=Label(endre_student_vindu, text='Oppgi fornavn: ')
    lbl_fornavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    fornavn=StringVar()
    ent_fornavn=Entry(endre_student_vindu, width=10, textvariable=fornavn)
    ent_fornavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_etternavn=Label(endre_student_vindu, text='Oppgi etternavn: ')
    lbl_etternavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    etternavn=StringVar()
    ent_etternavn=Entry(endre_student_vindu, width=10, textvariable=etternavn)
    ent_etternavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_epost=Label(endre_student_vindu,text='Oppgi e-post: ')
    lbl_epost.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    epost=StringVar()
    ent_epost=Entry(endre_student_vindu, width=15, textvariable=epost)
    ent_epost.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_telefon=Label(endre_student_vindu, text='Oppgi telefon: ')
    lbl_telefon.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    telefon=StringVar()
    ent_telefon=Entry(endre_student_vindu, width=10, textvariable=telefon)
    ent_telefon.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    #Lagre-knapp
    btn_lagre=Button(endre_student_vindu, text='Lagre student',command=lagre_student)
    btn_lagre.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Tilbake-knapp
    btn_avslutt=Button(endre_student_vindu, text='Tilbake',command=endre_student_vindu.destroy)
    btn_avslutt.grid(row=8, column=2, padx=5, pady=(20,5),sticky=E)



    endre_student_vindu.mainloop()
  
        
def open_slett_student_vindu():

    def finn_student():
        #Finner student
        funnet=False
        valgt=studentnr.get()
        
        finne_student_markor=mindatabase.cursor()
        finne_student_markor.execute("SELECT * FROM Student")
        
        for row in finne_student_markor:
            if valgt == row[0]:
                fornavn.set(row[1])
                etternavn.set(row[2])
                epost.set(row[3])
                telefon.set(row[4])
                funnet=True
                
        finne_student_markor.close()
        
        if not funnet:
            
            tilbakemelding_vindu=Toplevel(slett_student_vindu)
            tilbakemelding_vindu.title('Fant ikke studentnr')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Kunne ikke finne studentnummeret i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop() 
            
    def slett_student():
        
        try:
            #Sletter student fra databasen
            valgt=studentnr.get()
            
            slette_resultat_markor=mindatabase.cursor()
            slette_student_markor=mindatabase.cursor()
            
                
            slett_resultat="DELETE FROM Eksamensresultat WHERE Studentnr= '%s'" %(valgt)
            slett_student="DELETE FROM Student WHERE Studentnr= '%s'" % (valgt)
            
            slette_resultat_markor.execute(slett_resultat)
            mindatabase.commit()
            slette_student_markor.execute(slett_student)
            mindatabase.commit()
            
            
            tilbakemelding_vindu=Toplevel(slett_student_vindu)
            
            tilbakemelding_vindu.title('Sletting utført')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Studenten ble slettet fra databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()

            slette_resultat_markor.close()
            slette_student_markor.close()
            
        except DatabaseError:
            
            tilbakemelding_vindu=Toplevel(slett_student_vindu)
            tilbakemelding_vindu.title('Sletting feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved sletting i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()
    
        


    slett_student_vindu=Toplevel(window)
    slett_student_vindu.title('Slett student')

    lbl_studentnr=Label(slett_student_vindu,text='Oppgi studentnr: ')
    lbl_studentnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    studentnr=StringVar()
    ent_studentnr=Entry(slett_student_vindu, width=6, textvariable=studentnr)
    ent_studentnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btn_finn=Button(slett_student_vindu,text='Finn student',command=finn_student)
    btn_finn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lbl_fornavn=Label(slett_student_vindu, text='Fornavn: ')
    lbl_fornavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    fornavn=StringVar()
    ent_fornavn=Label(slett_student_vindu, textvariable=fornavn)
    ent_fornavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_etternavn=Label(slett_student_vindu, text='Etternavn: ')
    lbl_etternavn.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    etternavn=StringVar()
    ent_etternavn=Label(slett_student_vindu, textvariable=etternavn)
    ent_etternavn.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_epost=Label(slett_student_vindu,text='E-post: ')
    lbl_epost.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    epost=StringVar()
    ent_epost=Label(slett_student_vindu, textvariable=epost)
    ent_epost.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_telefon=Label(slett_student_vindu, text='Telefon: ')
    lbl_telefon.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    telefon=StringVar()
    ent_telefon=Label(slett_student_vindu, textvariable=telefon)
    ent_telefon.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    #Lagre-knapp
    btn_lagre=Button(slett_student_vindu, text='Slett student',command=slett_student)
    btn_lagre.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Avslutt-knapp
    btn_avslutt=Button(slett_student_vindu, text='Tilbake',command=slett_student_vindu.destroy)
    btn_avslutt.grid(row=8, column=2, padx=5, pady=(20,5),sticky=E)

    slett_student_vindu.mainloop()
    

def open_karakterliste_student():

    def finn_eksamensresultat():
        
        
        #Finner eksamensresultater pr student i databasen
        valgt=sok_studentnr_variabel.get()
        eksamens_info=[]
        funnet=False

        hent_eksamen_markor=mindatabase.cursor()

        hent_eksamen_markor.execute("SELECT Eksamensresultat.*, Emnenavn,Studiepoeng FROM Eksamensresultat, Emne WHERE Eksamensresultat.Emnekode = Emne.Emnekode GROUP BY Eksamensresultat.Studentnr,Eksamensresultat.Emnekode,Emne.Emnenavn,Emne.Studiepoeng, Eksamensresultat.Dato,Eksamensresultat.Karakter ORDER BY Eksamensresultat.Dato")


        for rad in hent_eksamen_markor:
            if valgt == rad[0]:
                eksamens_info +=[[rad[2],rad[1],rad[4],rad[3],rad[5]]]
                funnet=True
            
        innhold_i_eksamener.set(tuple(eksamens_info))


        hent_eksamen_markor.close()
            
        if not funnet:
                        
            tilbakemelding_vindu=Toplevel(karakterliste_student_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne studentnummeret i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  
        
        

    karakterliste_student_vindu=Toplevel(window)
    karakterliste_student_vindu.title('Karakterliste for student')


    lbl_sok_studentnr=Label(karakterliste_student_vindu,text='Oppgi studentnr: ')
    lbl_sok_studentnr.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    sok_studentnr_variabel=StringVar()
    ent_sok_studentnr=Entry(karakterliste_student_vindu,width=8,textvariable=sok_studentnr_variabel)
    ent_sok_studentnr.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    btn_sok_studentnr=Button(karakterliste_student_vindu,text='Finn eksamensresultater',command=finn_eksamensresultat)
    btn_sok_studentnr.grid(row=1,column=4,padx=(5,20),pady=5,sticky=E)


    lbl_rom_emnekode_studentnr=Label(karakterliste_student_vindu,text='Dato |   Emnekode | Emnenavn   | Karakter | Studiepoeng')
    lbl_rom_emnekode_studentnr.grid(row=0,column=0,padx=50,pady=5, sticky=W)

    y_scroll=Scrollbar(karakterliste_student_vindu,orient=VERTICAL)
    y_scroll.grid(row=1,column=1,rowspan=10,padx=(0,30),pady=(5,10),sticky=NS)

    innhold_i_eksamener=StringVar()
    liste_eksamener=Listbox(karakterliste_student_vindu,width=50,height=10,listvariable=innhold_i_eksamener,yscrollcommand=y_scroll.set)
    liste_eksamener.grid(row=1,column=0,rowspan=10,padx=(50,0),pady=(5,10),sticky=E)

    y_scroll["command"] = liste_eksamener.yview

    btn_tilbake=Button(karakterliste_student_vindu,text='Tilbake',command=karakterliste_student_vindu.destroy)
    btn_tilbake.grid(row=9,column=4,padx=10,pady=(50,5),sticky=E)

    karakterliste_student_vindu.mainloop()
    

def open_vitnemal_vindu():
    
    def finn_student():
        funnet=False 
        vitnemal_liste=[]
        valgt=studentnr.get()
        karakter_markor=mindatabase.cursor()
        
        
        finn_karakter="SELECT Eksamensresultat.Studentnr,Eksamensresultat.Emnekode, Emne.Emnenavn, MIN(Karakter), Emne.Studiepoeng,SUBSTRING(Eksamensresultat.Emnekode,1,3) AS Bokstaver, SUBSTRING(Eksamensresultat.Emnekode,4,7) AS Nummer\
                        FROM Eksamensresultat,Emne \
                        WHERE Eksamensresultat.Emnekode = Emne.Emnekode\
                        AND Studentnr = '%s'\
                        GROUP BY Eksamensresultat.Emnekode\
                        ORDER BY Nummer ASC, Bokstaver ASC" % (valgt)
        
        karakter_markor.execute(finn_karakter)
        
        studiepoeng_liste=[]
        #Tester på studentnr
        #Fjerner stryk-karakterer og ikke-satt-karakterer
        for row in karakter_markor:
            if row[0]==valgt:
                funnet=True
                if row[3] != 'F' and row[3] != '':
                    vitnemal_liste+=[[row[1],row[2],row[3]]]
                    studiepoeng_liste += [row[4]]
                    
    
            
        innhold_i_eksamensresultat.set(tuple(vitnemal_liste))
        studiepoeng.set(sum(studiepoeng_liste))

    
        karakter_markor.close()
        
        #Henter ut navn på student  
        student_info_markor=mindatabase.cursor()
        
        student_info_markor.execute("SELECT * FROM Student ")
        
        for rad in student_info_markor:
            if rad[0]== valgt:
                fornavn.set(rad[1])
                etternavn.set(rad[2])
                
        student_info_markor.close()

        if not funnet:
                        
            tilbakemelding_vindu=Toplevel(vitnemal_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne studentnummeret i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()      



    vitnemal_vindu=Toplevel(window)
    vitnemal_vindu.title('Vitnemålutskrift')


    lbl_studentnr=Label(vitnemal_vindu,text='Oppgi studentnr: ')
    lbl_studentnr.grid(row=0,column=0,padx=(60,1),pady=10,sticky=W)

    studentnr=StringVar()
    ent_studentnr=Entry(vitnemal_vindu,width=8,textvariable=studentnr)
    ent_studentnr.grid(row=0,column=0,padx=(200,5),pady=10,sticky=W)

    btn_finn_student=Button(vitnemal_vindu,width=8,text='Lag Vitnemål',command=finn_student)
    btn_finn_student.grid(row=0,column=1,padx=(0,130),pady=10,sticky=E)

    lbl_vitnemal=Label(vitnemal_vindu,text='Vitnemål for: ')
    lbl_vitnemal.grid(row=1,column=0,padx=(60,10), sticky=W)


    fornavn=StringVar()
    ent_fornavn=Label(vitnemal_vindu,textvariable=fornavn)
    ent_fornavn.grid(row=1,column=0,padx=(70,10),pady=5)

    etternavn=StringVar()
    ent_etternavn=Label(vitnemal_vindu,textvariable=etternavn)
    ent_etternavn.grid(row=1,column=0,padx=(190,0),pady=5)

    lbl_studiepoeng=Label(vitnemal_vindu,text='Sum studiepoeng: ')
    lbl_studiepoeng.grid(row=2,column=0,padx=(60,10),pady=(5,20),sticky=W)

    studiepoeng=StringVar()
    ent_studiepoeng=Label(vitnemal_vindu,textvariable=studiepoeng)
    ent_studiepoeng.grid(row=2,column=0,padx=(200,10),pady=(5,20),sticky=W)

    lbl_beskrivelse=Label(vitnemal_vindu,text=' Emnekode  |   Emnenavn     |   Karakter')
    lbl_beskrivelse.grid(row=3,column=0,columnspan=2,padx=60,pady=0, sticky=W)

    y_scroll=Scrollbar(vitnemal_vindu,orient=VERTICAL)
    y_scroll.grid(row=40,column=2,rowspan=10,padx=(0,50),pady=5,sticky=NS)

    innhold_i_eksamensresultat=StringVar()
    liste_eksamensresultat=Listbox(vitnemal_vindu,width=50,height=10,listvariable=innhold_i_eksamensresultat,yscrollcommand=y_scroll.set)
    liste_eksamensresultat.grid(row=40,column=0,columnspan=2,rowspan=10,padx=(50,0),pady=5,sticky=E)
  
    y_scroll["command"] = liste_eksamensresultat.yview

    btn_tilbake=Button(vitnemal_vindu,text='Tilbake',command=vitnemal_vindu.destroy)
    btn_tilbake.grid(row=50,column=2,padx=5,pady=(50,5),sticky=E)

    vitnemal_vindu.mainloop()
    
    

def open_legg_eksamen_vindu():
    
    def lagre_eksamensinfo():
            
        try:
            opptatt=False
            sjekk_ledighet_markor=mindatabase.cursor()
            eksamens_database=[]
            
            data_emnekode=emnekode.get()
            data_dato=dato.get()
            data_romnr=romnr.get()
            
            sjekk_ledighet_markor.execute("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Romnr FROM Eksamen")
            
            for row in sjekk_ledighet_markor:
                eksamens_database += [[row[0],row[1],row[2]]]
            
            
            for rad in range(0,len(eksamens_database),1):   
                if (eksamens_database[rad][1]== data_dato) and (eksamens_database[rad][2]== data_romnr):
                    opptatt=True
                    
                    
                    
            sjekk_ledighet_markor.close()
            
            if opptatt:
                
                tilbakemelding_vindu=Toplevel(legg_eksamen_vindu)
                tilbakemelding_vindu.title('Rom opptatt')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Rommet er opptatt. Vennligst velg et annet rom.')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()
                
                    
            if not opptatt:
            
                legge_til_eksamen_markor=mindatabase.cursor()
                
                legge_til_eksamen=("INSERT INTO Eksamen"
                                    "(Emnekode,Dato,Romnr)"
                                    "VALUES(%s,%s,%s)" )
                
                data_ny_eksamen=(data_emnekode,data_dato,data_romnr)
                
                legge_til_eksamen_markor.execute(legge_til_eksamen,data_ny_eksamen)
                
                
                mindatabase.commit()
                
                legge_til_eksamen_markor.close()

                tilbakemelding_vindu=Toplevel(legg_eksamen_vindu)
                tilbakemelding_vindu.title('Lagring utført')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Eksamen ble lagret i databasen')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()
        
        except DatabaseError:
        
            tilbakemelding_vindu=Toplevel(legg_eksamen_vindu)
            tilbakemelding_vindu.title('Lagring feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  
        



    legg_eksamen_vindu=Toplevel(window)
    legg_eksamen_vindu.title('Legge til en eksamen')

    lbl_emnekode=Label(legg_eksamen_vindu,text='Oppgi emnekode: ')
    lbl_emnekode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(legg_eksamen_vindu, width=6, textvariable=emnekode)
    ent_emnekode.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    lbl_dato=Label(legg_eksamen_vindu, text='Oppgi dato: ')
    lbl_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    dato=StringVar()
    ent_dato=Entry(legg_eksamen_vindu, width=10, textvariable=dato)
    ent_dato.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    lbl_romnr=Label(legg_eksamen_vindu, text='Oppgi romnr: ')
    lbl_romnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    romnr=StringVar()
    ent_romnr=Entry(legg_eksamen_vindu, width=10, textvariable=romnr)
    ent_romnr.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    #Lagre-knapp
    btn_lagre=Button(legg_eksamen_vindu, text='Lagre eksamen',command=lagre_eksamensinfo)
    btn_lagre.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Avslutt-knapp
    btn_avslutt=Button(legg_eksamen_vindu, text='Tilbake',command=legg_eksamen_vindu.destroy)
    btn_avslutt.grid(row=8, column=2, padx=5, pady=(20,5),sticky=E)

    legg_eksamen_vindu.mainloop()
   
    
def open_endre_eksamen_vindu():
    
    def finn_eksamen():
        #Finner eksisterende eksamen i databasen
        funnet=False
        valgt_emnekode=emnekode.get()
        valgt_dato=dato.get()
        finn_eksamen_markor=mindatabase.cursor()
        
        finn_eksamensdata = ("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Romnr FROM Eksamen")
        
        finn_eksamen_markor.execute(finn_eksamensdata)
        
        for row in finn_eksamen_markor: 
            if (row[0]==valgt_emnekode) and (row[1]==valgt_dato):
                o_emnekode.set(valgt_emnekode)
                o_dato.set(valgt_dato)
                o_romnr.set(row[2])
                funnet=True
                
        finn_eksamen_markor.close()
            
        if not funnet:
        
            tilbakemelding_vindu=Toplevel(endre_eksamen_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensdata i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop() 

    def lagre_eksamensinfo():
        
        #Sjekker om rommet er ledig og legger inn i databasen
        try:
            opptatt=False
            sjekk_ledighet_markor=mindatabase.cursor()
            eksamens_database=[]
            
            data_emnekode=o_emnekode.get()
            data_dato=o_dato.get()
            data_romnr=o_romnr.get()
            
            sjekk_ledighet_markor.execute("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Romnr FROM Eksamen")
            
            for row in sjekk_ledighet_markor:
                eksamens_database += [[row[0],row[1],row[2]]]
            
            
            for rad in range(0,len(eksamens_database),1):   
                if (eksamens_database[rad][1]== data_dato) and (eksamens_database[rad][2]== data_romnr):
                    opptatt=True
                    
                            
            sjekk_ledighet_markor.close()
            
            if opptatt:
                
                tilbakemelding_vindu=Toplevel(endre_eksamen_vindu)
                tilbakemelding_vindu.title('Rom opptatt')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Rommet er opptatt. Vennligst velg et annet rom.')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()
                
                    
            if not opptatt: 
                
                
                legge_til_dato_markor=mindatabase.cursor()
                
            
                legge_til_data_eksamen = "UPDATE Eksamen SET Romnr = '%s' WHERE Emnekode= '%s' AND Dato = '%s'" % (data_romnr,data_emnekode,data_dato)
                
                
                legge_til_dato_markor.execute(legge_til_data_eksamen)
                
                
                mindatabase.commit()
                
                legge_til_dato_markor.close()
                

                tilbakemelding_vindu=Toplevel(endre_eksamen_vindu)
                tilbakemelding_vindu.title('Lagring utført')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Eksamen ble lagret i databasen')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()
                
                
                
            
        except DatabaseError:
        
            tilbakemelding_vindu=Toplevel(endre_eksamen_vindu)
            tilbakemelding_vindu.title('Lagring feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  
            



    endre_eksamen_vindu=Toplevel(window)
    endre_eksamen_vindu.title('Endre eksamensinformasjon')

    lbl_emnekode=Label(endre_eksamen_vindu,text='Oppgi emnekode: ')
    lbl_emnekode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(endre_eksamen_vindu, width=8, textvariable=emnekode)
    ent_emnekode.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    lbl_dato=Label(endre_eksamen_vindu, text='Oppgi dato: ')
    lbl_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    dato=StringVar()
    ent_dato=Entry(endre_eksamen_vindu, width=8, textvariable=dato)
    ent_dato.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    btn_finn=Button(endre_eksamen_vindu,text='Finn eksamensinfo', command=finn_eksamen)
    btn_finn.grid(row=2,column=1,padx=5,pady=(5,10),sticky=E)

    #Oppdatere info felt
    lbl_o_emnekode=Label(endre_eksamen_vindu,text='Emnekode: ')
    lbl_o_emnekode.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    o_emnekode=StringVar()
    ent_o_emnekode=Label(endre_eksamen_vindu,textvariable=o_emnekode)
    ent_o_emnekode.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_o_dato=Label(endre_eksamen_vindu, text='Dato: ')
    lbl_o_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    o_dato=StringVar()
    ent_o_dato=Label(endre_eksamen_vindu,textvariable=o_dato)
    ent_o_dato.grid(row=4, column=1, padx=5, pady=5, sticky=W)
    #siste

    lbl_o_romnr=Label(endre_eksamen_vindu, text='Oppdater romnr: ')
    lbl_o_romnr.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    o_romnr=StringVar()
    ent_o_romnr=Entry(endre_eksamen_vindu, width=6, textvariable=o_romnr)
    ent_o_romnr.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    #Lagre-knapp
    btn_lagre=Button(endre_eksamen_vindu, text='Lagre eksamen',command=lagre_eksamensinfo)
    btn_lagre.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Avslutt-knapp
    btn_avslutt=Button(endre_eksamen_vindu, text='Tilbake',command=endre_eksamen_vindu.destroy)
    btn_avslutt.grid(row=9, column=1, padx=5, pady=(20,5),sticky=E)

    endre_eksamen_vindu.mainloop()
           

def open_slett_eksamen_vindu():
    
    def finn_eksamen():
        funnet=False
        data_emnekode=emnekode.get()
        data_dato=dato.get()
        
        finne_eksamen_markor=mindatabase.cursor()
        finne_eksamen_markor.execute("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Romnr FROM Eksamen")
        
        for row in finne_eksamen_markor:
            if (data_emnekode == row[0]) and (data_dato==row[1]):
                s_emnekode.set(data_emnekode)
                s_dato.set(data_dato)
                s_romnr.set(row[2])
                funnet=True
                
        finne_eksamen_markor.close()
        
        if not funnet:
            
            tilbakemelding_vindu=Toplevel(slett_eksamen_vindu)
            tilbakemelding_vindu.title('Fant ikke eksamen')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Kunne ikke finne eksamensinfo i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop() 
            
    def slett_eksamen():
        
        try:
            data_emnekode=emnekode.get()
            data_dato=dato.get()
            
            
            slette_1_markor=mindatabase.cursor()
            slette_2_markor=mindatabase.cursor()
            
            slett_eksamensresultat=("DELETE FROM Eksamensresultat WHERE Emnekode = '%s' AND Dato = '%s'") % (data_emnekode,data_dato)
            slett_eksamenen=("DELETE FROM Eksamen WHERE Emnekode = '%s' AND Dato = '%s'") % (data_emnekode,data_dato)
            
            slette_1_markor.execute(slett_eksamensresultat) 
            mindatabase.commit()
            slette_2_markor.execute(slett_eksamenen)
            mindatabase.commit()
            
            slette_1_markor.close()
            slette_2_markor.close()        
            
            
            tilbakemelding_vindu=Toplevel(slett_eksamen_vindu)
            
            tilbakemelding_vindu.title('Sletting utført')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Eksamen ble slettet fra databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()


            
        except DatabaseError:
            
            tilbakemelding_vindu=Toplevel(slett_eksamen_vindu)
            tilbakemelding_vindu.title('Sletting feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved sletting i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()
    
        

    slett_eksamen_vindu=Toplevel(window)
    slett_eksamen_vindu.title('Slett Eksamen')

    lbl_emnekode=Label(slett_eksamen_vindu,text='Oppgi Emnekode: ')
    lbl_emnekode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(slett_eksamen_vindu, width=6, textvariable=emnekode)
    ent_emnekode.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    lbl_dato=Label(slett_eksamen_vindu,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(slett_eksamen_vindu,width=8,textvariable=dato)
    ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btn_finn=Button(slett_eksamen_vindu,text='Finn Eksamen',command=finn_eksamen)
    btn_finn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    lbl_s_emnekode=Label(slett_eksamen_vindu, text='Emnekode: ')
    lbl_s_emnekode.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    s_emnekode=StringVar()
    ent_s_emnekode=Label(slett_eksamen_vindu, textvariable=s_emnekode)
    ent_s_emnekode.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    lbl_s_dato=Label(slett_eksamen_vindu, text='Eksamensdato: ')
    lbl_s_dato.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    s_dato=StringVar()
    ent_s_dato=Label(slett_eksamen_vindu, textvariable=s_dato)
    ent_s_dato.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    lbl_s_romnr=Label(slett_eksamen_vindu,text='Romnr: ')
    lbl_s_romnr.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    s_romnr=StringVar()
    ent_s_romnr=Label(slett_eksamen_vindu, textvariable=s_romnr)
    ent_s_romnr.grid(row=5, column=1, padx=5, pady=5, sticky=W)


    #Lagre-knapp
    btn_slett=Button(slett_eksamen_vindu, text='Slett eksamen',command=slett_eksamen)
    btn_slett.grid(row=8, column=1, padx=5, pady=(20,5),sticky=W)


    #Avslutt-knapp
    btn_avslutt=Button(slett_eksamen_vindu, text='Tilbake',command=slett_eksamen_vindu.destroy)
    btn_avslutt.grid(row=8, column=2, padx=5, pady=(20,5),sticky=E)




    slett_eksamen_vindu.mainloop()
    
    
def open_ustkrift_eksamen_vindu():
    
    def sok_dato():
        funnet=False
        valgt= sok_dato_variabel.get()
        eksamens_info=[]
        
        hent_eksamen_markor=mindatabase.cursor()

        
        hent_eksamensinfo = "SELECT \
                            Eksamen.Emnekode,DATE_FORMAT(Eksamen.Dato,'%Y%m%d'),Eksamen.Romnr,Emne.Emnenavn,Rom.Antallplasser \
                            FROM Eksamen \
                            INNER JOIN Emne ON Eksamen.Emnekode = Emne.Emnekode \
                            INNER JOIN Rom ON Eksamen.Romnr = Rom.Romnr \
                            ORDER BY Dato"
                                            
        
        hent_eksamen_markor.execute(hent_eksamensinfo)


        for rad in hent_eksamen_markor:
            if rad[1]==valgt:
                eksamens_info += [[rad[1],rad[0],rad[3],rad[2],rad[4]]]
                funnet=True
        
            
        
        innhold_i_eksamener.set(tuple(eksamens_info))
        
        hent_eksamen_markor.close()
        
        if not funnet:
                    
            tilbakemelding_vindu=Toplevel(utskrift_eksamen_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensinformasjon i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  
        
        
    def sok_periode():
        funnet=False
        valgt_fra_dato=sok_periode_variabel_fra.get()
        valgt_til_dato=sok_periode_variabel_til.get()
        
        eksamens_info=[]
        hent_eksamen_markor=mindatabase.cursor()

        
        hent_eksamensinfo = "SELECT \
                            Eksamen.Emnekode,DATE_FORMAT(Eksamen.Dato,'%Y%m%d'),Eksamen.Romnr,Emne.Emnenavn,Rom.Antallplasser \
                            FROM Eksamen \
                            INNER JOIN Emne ON Eksamen.Emnekode = Emne.Emnekode \
                            INNER JOIN Rom ON Eksamen.Romnr = Rom.Romnr \
                            ORDER BY Dato"
                            
        
        hent_eksamen_markor.execute(hent_eksamensinfo)


        for rad in hent_eksamen_markor:
            if rad[1]>=valgt_fra_dato and rad[1]<=valgt_til_dato:
                eksamens_info += [[rad[1],rad[0],rad[3],rad[2],rad[4]]]
                funnet=True
        
        innhold_i_eksamener.set(tuple(eksamens_info))
        
        hent_eksamen_markor.close()
        
        if not funnet:
                    
            tilbakemelding_vindu=Toplevel(utskrift_eksamen_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensinformasjon i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  



    utskrift_eksamen_vindu=Toplevel(window)
    utskrift_eksamen_vindu.title('Oversikt over eksamener')

    lbl_sok_dato=Label(utskrift_eksamen_vindu,text='Søk etter dato: ')
    lbl_sok_dato.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    sok_dato_variabel=StringVar()
    ent_sok_dato=Entry(utskrift_eksamen_vindu,width=8,textvariable=sok_dato_variabel)
    ent_sok_dato.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    btn_sok_dato=Button(utskrift_eksamen_vindu,width=8,text='Søk dato',command=sok_dato)
    btn_sok_dato.grid(row=1,column=4,padx=(5,20),pady=5,sticky=E)


    lbl_fra=Label(utskrift_eksamen_vindu,text='Fra dato:')
    lbl_fra.grid(row=2,column=2,padx=5,pady=5,sticky=E)


    sok_periode_variabel_fra=StringVar()
    ent_sok_periode_fra=Entry(utskrift_eksamen_vindu,width=8,textvariable=sok_periode_variabel_fra)
    ent_sok_periode_fra.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    lbl_til=Label(utskrift_eksamen_vindu,text='Til: ')
    lbl_til.grid(row=3,column=2,padx=5,pady=5,sticky=E)

    sok_periode_variabel_til=StringVar()
    ent_sok_periode_til=Entry(utskrift_eksamen_vindu,width=8,textvariable=sok_periode_variabel_til)
    ent_sok_periode_til.grid(row=3,column=3,padx=5,pady=5,sticky=W)

    btn_sok_periode=Button(utskrift_eksamen_vindu,text='Søk periode', command=sok_periode)
    btn_sok_periode.grid(row=3,column=4,padx=(5,20),pady=5,sticky=E)

    lbl_rom_emnekode_dato=Label(utskrift_eksamen_vindu,text='  Dato       |   Emnekode  |      Emnenavn     |  Rom  |  Antall plasser ')
    lbl_rom_emnekode_dato.grid(row=0,column=0,padx=45,pady=5, sticky=W)

    y_scroll=Scrollbar(utskrift_eksamen_vindu,orient=VERTICAL)
    y_scroll.grid(row=1,column=1,rowspan=10,padx=(0,50),pady=5,sticky=NS)

    innhold_i_eksamener=StringVar()
    liste_eksamener=Listbox(utskrift_eksamen_vindu,width=50,height=10,listvariable=innhold_i_eksamener,yscrollcommand=y_scroll.set)
    liste_eksamener.grid(row=1,column=0,rowspan=10,padx=(50,0),pady=5,sticky=E)

    y_scroll["command"] = liste_eksamener.yview

    btn_tilbake=Button(utskrift_eksamen_vindu,text='Tilbake',command=utskrift_eksamen_vindu.destroy)
    btn_tilbake.grid(row=9,column=4,padx=5,pady=(50,5),sticky=E)

    utskrift_eksamen_vindu.mainloop()
     

def open_emne_karakterliste_vindu():
    
    def finn_karakterliste():
        
        valgt=emnekode_variabel.get()
        valgt_ar=arstall.get()
        eksamens_info=[]
        funnet=False
        
        hent_eksamen_markor=mindatabase.cursor()

        hent_eksamen_markor.execute("SELECT Studentnr,Emnekode,Dato,Karakter,DATE_FORMAT(Dato,'%Y') FROM Eksamensresultat WHERE Karakter IS NOT NULL ORDER BY Studentnr")


        for rad in hent_eksamen_markor:
            if valgt == rad[1] and rad[4]==valgt_ar:
                eksamens_info +=[[rad[0],rad[1],rad[2],rad[3]]]
                funnet=True
            
        
        innhold_i_eksamener.set(tuple(eksamens_info))
        
        
        hent_eksamen_markor.close()
        
        if not funnet:
            tilbakemelding_vindu=Toplevel(emne_karakterliste_vindu)
            tilbakemelding_vindu.title('Det skjedde en feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne emnet i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  
            
        
 

    emne_karakterliste_vindu=Toplevel(window)
    emne_karakterliste_vindu.title('Karakterliste')


    lbl_emnekode=Label(emne_karakterliste_vindu,text='Oppgi emnekode: ')
    lbl_emnekode.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    emnekode_variabel=StringVar()
    ent_emnekode=Entry(emne_karakterliste_vindu,width=8,textvariable=emnekode_variabel)
    ent_emnekode.grid(row=1,column=3,padx=5,pady=5,sticky=W)
    
    lbl_ar=Label(emne_karakterliste_vindu,text='Oppgi år: ')
    lbl_ar.grid(row=2,column=2,padx=5,pady=5,sticky=E)
    
    arstall=StringVar()
    ent_ar=Entry(emne_karakterliste_vindu,width=4,textvariable=arstall)
    ent_ar.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    btn_sok=Button(emne_karakterliste_vindu,text='Finn eksamensresultater',command=finn_karakterliste)
    btn_sok.grid(row=3,column=3,padx=(5,20),pady=5,sticky=E)



    lbl_rom_emnekode_dato=Label(emne_karakterliste_vindu,text='Studentnr | Emnekode | Dato | Karakter')
    lbl_rom_emnekode_dato.grid(row=0,column=0,padx=45,pady=5, sticky=W)

    y_scroll=Scrollbar(emne_karakterliste_vindu,orient=VERTICAL)
    y_scroll.grid(row=1,column=1,rowspan=10,padx=(0,50),pady=(5,10),sticky=NS)

    innhold_i_eksamener=StringVar()
    liste_eksamener=Listbox(emne_karakterliste_vindu,width=50,height=10,listvariable=innhold_i_eksamener,yscrollcommand=y_scroll.set)
    liste_eksamener.grid(row=1,column=0,rowspan=10,padx=(50,0),pady=(5,10),sticky=E)

    y_scroll["command"] = liste_eksamener.yview

    btn_tilbake=Button(emne_karakterliste_vindu,text='Tilbake',command=emne_karakterliste_vindu.destroy)
    btn_tilbake.grid(row=10,column=4,padx=5,pady=(50,5),sticky=E)

    emne_karakterliste_vindu.mainloop()
    
    
        
def open_legg_eksamensresultat_vindu():
    
    def finn_eksamen():
        
        def registrer_karakter():
            try:
                
                #Lage liste til entryer og kombinererer i ny liste med studentnr
            
                karakterliste=[]
                entry_liste=[]
                for entries in ent_liste:
                    entry_liste += [str(entries.get())]
                
                for x in range(ant_studentnr):
                    karakterliste += [[studentnr_liste[x][0],entry_liste[x][0]]]
                    
                    
                    
                #legger listeelementer i variabler for så å legge det inn i databasen med for-løkke
                #Legger listen inn i databasen pr studentnr
                
                for a in karakterliste:
                    valgt_studentnr=str(a[0])
                    valgt_karakter=str(a[1])
                    
                    oppdater_markor=mindatabase.cursor()
                    oppdater="UPDATE Eksamensresultat \
                                SET Karakter='%s' \
                                WHERE Emnekode='%s' AND Dato='%s' AND Studentnr='%s'" % (valgt_karakter,valgt_emnekode,valgt_dato,valgt_studentnr)
                    oppdater_markor.execute(oppdater)
                    mindatabase.commit()
                    oppdater_markor.close()
                    
                

                
                tilbakemelding_vindu=Toplevel(registrerings_vindu)
                tilbakemelding_vindu.title('Lagring utført')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Eksamenskarakterene ble lagret i databasen')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()
            
            except DatabaseError:
            
                tilbakemelding_vindu=Toplevel(registrerings_vindu)
                tilbakemelding_vindu.title('Lagring feilet')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()  
                
            except IndexError:
                tilbakemelding_vindu=Toplevel(registrerings_vindu)
                tilbakemelding_vindu.title('Lagring feilet')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Alle studentnr må tildeles en karakter før lagring i databasen kan utføres.')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()  
            
         
        
        #Finner eksisterende eksamen i databasen
        funnet=False
        valgt_emnekode=emnekode.get()
        valgt_dato=eks_dato.get()
        finn_eksamen_markor=mindatabase.cursor()
        
        finn_eksamensdata = ("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Romnr FROM Eksamen")
        
        finn_eksamen_markor.execute(finn_eksamensdata)
        
        for row in finn_eksamen_markor: 
            if (row[0]==valgt_emnekode) and (row[1]==valgt_dato):
                funnet=True
                
        finn_eksamen_markor.close()
            
        if not funnet:
        
            tilbakemelding_vindu=Toplevel(legg_eksamensresultat_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensdata i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop() 
            
            
        if funnet:
            
            #Åpner nytt vindu dersom eksamen eksisterer
            
            studentnr_liste=[]
            ant_studentnr_liste=[]
            finne_ant_studentnr_markor=mindatabase.cursor()
            finne_ant_studentnr_markor.execute("SELECT Emnekode,Studentnr,Karakter FROM Eksamensresultat WHERE Karakter=''")
            
            #Henter ut kun studentnr med blankt karakterfelt
            
            #Legger ant studentnr i liste
            for row in finne_ant_studentnr_markor:
                if row[0]==valgt_emnekode:
                    studentnr_liste += [[row[1]]]
                    
                    ant_studentnr_liste +=  [row[1]]
            
            
            
            ant_studentnr=len(ant_studentnr_liste)
            
            
            #Leger inn en feilmelding hvis det ikke er funnet studentnr i databasen oppmeldt til eksamen
            
            if not ant_studentnr:
                tilbakemelding_vindu=Toplevel(legg_eksamensresultat_vindu)
                tilbakemelding_vindu.title('Ingen registrerte studenter')
                
                lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det er ingen oppmeldte studenter til denne eksamenen.')
                lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
                
                btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
                btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
                
                tilbakemelding_vindu.mainloop()  
            
            #Har funnet ant studentnr 
            #Går videre for å legge inn Entry-felt for studentnr og karakter
            ent_liste=[]
            #Lager vindu for karakter-input
            
            
            registrerings_vindu=Toplevel(legg_eksamensresultat_vindu)
            registrerings_vindu.title('Registrer karakterer')  
            
            ramme=Frame(registrerings_vindu) 
            canvas_innhold=Canvas(ramme,width=270,height=550)
            y_scroll=Scrollbar(ramme,orient=VERTICAL,command=canvas_innhold.yview)

            scroll_vindu=Frame(canvas_innhold)

            scroll_vindu.bind("<Configure>",lambda e: canvas_innhold.configure(scrollregion=canvas_innhold.bbox("all")))

            canvas_innhold.create_window((0, 0), window=scroll_vindu, anchor="nw")

            canvas_innhold.configure(yscrollcommand=y_scroll.set)



            lbl_studentnr=Label(scroll_vindu,text='Studentnr:')
            lbl_studentnr.grid(row=2,column=0,padx=(20,10),pady=5,sticky=E)

            lbl_karakter=Label(scroll_vindu,text='Karakter:')
            lbl_karakter.grid(row=2,column=1,padx=5,pady=5,sticky=W)
            
            
            for x in range(ant_studentnr):
                studentnr=StringVar()
                ent_studentnr=Label(scroll_vindu,width=6,textvariable=studentnr)
                ent_studentnr.grid(row=x+3,column=0,padx=(20,5),pady=5,sticky=E)
                studentnr.set(studentnr_liste[x][0])
                
                
                ent_karakter=Entry(scroll_vindu,width=3)
                ent_karakter.grid(row=x+3,column=1,padx=5,pady=5,sticky=W)
                ent_liste+=[ent_karakter]
                
            
                
            btn_lagre=Button(scroll_vindu,text='Lagre karakterer',command=registrer_karakter)
            btn_lagre.grid(row=202,column=0,columnspan=2,padx=20,pady=20)
                        
            btn_avslutt=Button(scroll_vindu,text='Tilbake',command=legg_eksamensresultat_vindu.destroy)
            btn_avslutt.grid(row=202,column=2,padx=5,pady=5,sticky=W)

            ramme.pack()
            canvas_innhold.pack(side="left", fill="both", expand=True)
            y_scroll.pack(side="right", fill="y")
                
                
            registrerings_vindu.mainloop()
            



    legg_eksamensresultat_vindu=Toplevel(window)
    legg_eksamensresultat_vindu.title('Registrer karakterer')


    lbl_emnekode=Label(legg_eksamensresultat_vindu,text='Emnekode: ')
    lbl_emnekode.grid(row=0,column=2,padx=5,pady=5,sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(legg_eksamensresultat_vindu,width=8,textvariable=emnekode)
    ent_emnekode.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    lbl_dato=Label(legg_eksamensresultat_vindu,text='Eksamensdato: ')
    lbl_dato.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    eks_dato=StringVar()
    ent_eks_dato=Entry(legg_eksamensresultat_vindu,width=8,textvariable=eks_dato)
    ent_eks_dato.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    btn_finn_eksamen=Button(legg_eksamensresultat_vindu,text='Finn eksamen',command=finn_eksamen)
    btn_finn_eksamen.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    btn_avslutt=Button(legg_eksamensresultat_vindu, text='Tilbake',command=legg_eksamensresultat_vindu.destroy)
    btn_avslutt.grid(row=3, column=3, padx=5, pady=(20,5),sticky=E)



    legg_eksamensresultat_vindu.mainloop()
    
        
def open_endre_eksamensresultat_vindu():
    
    def finn_karakter():
        #Finner eksisterende karakter i databasen
        funnet=False
        valgt_studentnr=studentnr.get()
        valgt_emnekode=emnekode.get()
        valgt_dato=dato.get()

        finn_eksamen_markor=mindatabase.cursor()

        finn_eksamensdata = ("SELECT Studentnr, Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Karakter FROM Eksamensresultat")

        finn_eksamen_markor.execute(finn_eksamensdata)
        
        for row in finn_eksamen_markor:
            if (valgt_studentnr==row[0]) and (valgt_emnekode==row[1]) and (valgt_dato==row[2]):
                karakter.set(row[3])
                funnet=True
                
        finn_eksamen_markor.close()
                
        if not funnet:
            
            tilbakemelding_vindu=Toplevel(endre_eksamensresultat_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensdata i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop() 
                
    def endre_karakter():
        #Legger inn oppdatert resultat i databasen
        try: 
            valgt_studentnr=studentnr.get()
            valgt_emnekode=emnekode.get()
            valgt_dato=dato.get()
            valgt_karakter=karakter.get()
            
            oppdater_markor=mindatabase.cursor()
            
            legg_til_oppdatering= ("UPDATE Eksamensresultat \
                                    SET Karakter = '%s' \
                                    WHERE Studentnr = '%s'AND Emnekode = '%s' AND Dato = '%s' ") %(valgt_karakter,valgt_studentnr,valgt_emnekode,valgt_dato)
            
            oppdater_markor.execute(legg_til_oppdatering)
            mindatabase.commit()
            oppdater_markor.close()
            
            tilbakemelding_vindu=Toplevel(endre_eksamensresultat_vindu)
            tilbakemelding_vindu.title('Lagring utført')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Eksamenskarakteren ble oppdatert i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()
        
        except DatabaseError:
        
            tilbakemelding_vindu=Toplevel(endre_eksamensresultat_vindu)
            tilbakemelding_vindu.title('Lagring feilet')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil ved lagring i databasen')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()      


    endre_eksamensresultat_vindu=Toplevel(window)
    endre_eksamensresultat_vindu.title('Endre Eksamensresultat')

    lbl_studentnr=Label(endre_eksamensresultat_vindu,text='Studentnr: ')
    lbl_studentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studentnr=StringVar()
    ent_studentnr=Entry(endre_eksamensresultat_vindu,width=6,textvariable=studentnr)    
    ent_studentnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lbl_emnekode=Label(endre_eksamensresultat_vindu,text='Oppgi emnekode:')
    lbl_emnekode.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(endre_eksamensresultat_vindu,width=8,textvariable=emnekode)
    ent_emnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lbl_dato=Label(endre_eksamensresultat_vindu,text='Oppgi eksamensdato: ')
    lbl_dato.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(endre_eksamensresultat_vindu,width=8,textvariable=dato)
    ent_dato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    btn_finn=Button(endre_eksamensresultat_vindu,text='Finn karakter',command=finn_karakter)
    btn_finn.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    lbl_karakter=Label(endre_eksamensresultat_vindu,text='Karakter: ')
    lbl_karakter.grid(row=4,column=0,padx=5,pady=10,sticky=E)

    karakter=StringVar()
    ent_karakter=Entry(endre_eksamensresultat_vindu,width=4,textvariable=karakter)
    ent_karakter.grid(row=4,column=1,padx=5,pady=10,sticky=W)

    btn_registrer=Button(endre_eksamensresultat_vindu,text='Endre karakter',command=endre_karakter)
    btn_registrer.grid(row=5,column=1,padx=5,pady=(50,5),sticky=E)       

    btn_avslutt=Button(endre_eksamensresultat_vindu, text='Tilbake',command=endre_eksamensresultat_vindu.destroy)
    btn_avslutt.grid(row=6, column=1, padx=5, pady=(20,5),sticky=E) 
        
        
    endre_eksamensresultat_vindu.mainloop()
    
def open_karakterstatistikk_vindu():   
    
    def finn_karakterstatistikk():
        funnet=False
        karakter_liste=[]
        data_dato=dato.get()
        data_emnekode=emnekode.get()
        ant_karakterer=0
        
        ant_a=0
        ant_b=0
        ant_c=0
        ant_d=0
        ant_e=0
        ant_f=0
        
        finn_karakterer_markor=mindatabase.cursor()
        finn_karakterer=("SELECT Emnekode,DATE_FORMAT(dato,'%Y%m%d'),Karakter FROM Eksamensresultat")
        finn_karakterer_markor.execute(finn_karakterer)
        
        for row in finn_karakterer_markor:
            if (row[0] == data_emnekode) and (row[1] == data_dato): 
                funnet=True
                karakter_liste += [[row[0],row[1],row[2]]]
            
        #Legger til alle karakterer i lister
        for row in range(0,len(karakter_liste),1):
            if karakter_liste[row][2]=='A':
                ant_a = ant_a + 1
                ant_karakterer = ant_karakterer + 1
            if karakter_liste[row][2]=='B':
                ant_b = ant_b + 1
                ant_karakterer = ant_karakterer + 1
            if karakter_liste[row][2]=='C':
                ant_c = ant_c + 1
                ant_karakterer = ant_karakterer + 1
            if karakter_liste[row][2]=='D':
                ant_d = ant_d + 1
                ant_karakterer = ant_karakterer + 1
            if karakter_liste[row][2]=='E':
                ant_e = ant_e + 1
                ant_karakterer = ant_karakterer + 1
            if karakter_liste[row][2]=='F':
                ant_f = ant_f + 1
                ant_karakterer = ant_karakterer + 1
           
        #Setter summen av karakterlistene inn i GUI-laget
        kA.set(ant_a)
        kB.set(ant_b)
        kC.set(ant_c)
        kD.set(ant_d)
        kE.set(ant_e)
        kF.set(ant_f)
        ant_kar.set(ant_karakterer)
        
        #Finner emneinformasjon
        finn_emneinfo_markor=mindatabase.cursor()
        finn_emne=("SELECT Emnenavn, Studiepoeng \
                                    FROM Emne \
                                    WHERE Emnekode = '%s' ") % (data_emnekode)
        finn_emneinfo_markor.execute(finn_emne)
        
        for emne in finn_emneinfo_markor:
            emnenavn.set(emne[0])
            studiepoeng.set(emne[1])
        
        finn_karakterer_markor.close()
        finn_emneinfo_markor.close()
        
            
        if not funnet:
            tilbakemelding_vindu=Toplevel(karakterstatistikk_vindu)
            tilbakemelding_vindu.title('Feil')
            
            lbl_tilbakemelding=Label(tilbakemelding_vindu,text='Det skjedde en feil. Kunne ikke finne eksamensinformasjon i databasen.')
            lbl_tilbakemelding.grid(row=0,column=0,padx=10,pady=20)
            
            btn_ok=Button(tilbakemelding_vindu,width=4,text='Lukk',command=tilbakemelding_vindu.destroy)
            btn_ok.grid(row=1,column=1,padx=5,pady=5,sticky=E)
            
            tilbakemelding_vindu.mainloop()  




    karakterstatistikk_vindu=Toplevel(window)
    karakterstatistikk_vindu.title('Eksamensstatistikk')

    lbl_emnekode=Label(karakterstatistikk_vindu,text='Emnekode: ')
    lbl_emnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    emnekode=StringVar()
    ent_emnekode=Entry(karakterstatistikk_vindu,width=8,textvariable=emnekode)
    ent_emnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lbl_dato=Label(karakterstatistikk_vindu,text='Eksamensdato: ')
    lbl_dato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(karakterstatistikk_vindu,width=8,textvariable=dato)
    ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btn_sok=Button(karakterstatistikk_vindu,text='Finn karakterstatistikk',command=finn_karakterstatistikk)
    btn_sok.grid(row=2,column=1,padx=5,pady=5,sticky=E)

    lbl_emnenavn=Label(karakterstatistikk_vindu,text='Emnenavn: ')
    lbl_emnenavn.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    emnenavn=StringVar()
    ent_emnenavn=Label(karakterstatistikk_vindu,textvariable=emnenavn)
    ent_emnenavn.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    lbl_studiepoeng=Label(karakterstatistikk_vindu,text='Studiepoeng: ')
    lbl_studiepoeng.grid(row=4,column=0,padx=5,pady=5,sticky=E)

    studiepoeng=StringVar()
    ent_studiepoeng=Label(karakterstatistikk_vindu,textvariable=studiepoeng)
    ent_studiepoeng.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    lbl_A=Label(karakterstatistikk_vindu,text='A:')
    lbl_A.grid(row=5,column=0,padx=5,pady=5,sticky=E)

    kA=StringVar()
    ent_A=Label(karakterstatistikk_vindu,textvariable=kA)
    ent_A.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    lbl_B=Label(karakterstatistikk_vindu,text='B:')
    lbl_B.grid(row=6,column=0,padx=5,pady=5,sticky=E)

    kB=StringVar()
    ent_B=Label(karakterstatistikk_vindu,textvariable=kB)
    ent_B.grid(row=6,column=1,padx=5,pady=5,sticky=W)

    lbl_C=Label(karakterstatistikk_vindu,text='C:')
    lbl_C.grid(row=7,column=0,padx=5,pady=5,sticky=E)

    kC=StringVar()
    ent_C=Label(karakterstatistikk_vindu,textvariable=kC)
    ent_C.grid(row=7,column=1,padx=5,pady=5,sticky=W)

    lbl_D=Label(karakterstatistikk_vindu,text='D:')
    lbl_D.grid(row=8,column=0,padx=5,pady=5,sticky=E)

    kD=StringVar()
    ent_D=Label(karakterstatistikk_vindu,textvariable=kD)
    ent_D.grid(row=8,column=1,padx=5,pady=5,sticky=W)

    lbl_E=Label(karakterstatistikk_vindu,text='E:')
    lbl_E.grid(row=9,column=0,padx=5,pady=5,sticky=E)

    kE=StringVar()
    ent_E=Label(karakterstatistikk_vindu,textvariable=kE)
    ent_E.grid(row=9,column=1,padx=5,pady=5,sticky=W)

    lbl_F=Label(karakterstatistikk_vindu,text='F:')
    lbl_F.grid(row=10,column=0,padx=5,pady=5,sticky=E)

    kF=StringVar()
    ent_F=Label(karakterstatistikk_vindu,textvariable=kF)
    ent_F.grid(row=10,column=1,padx=5,pady=5,sticky=W)
    
    lbl_ant_kar=Label(karakterstatistikk_vindu,text='Antall kandidater:')
    lbl_ant_kar.grid(row=11,column=0,padx=5,pady=5,sticky=E)
    
    ant_kar=StringVar()
    ent_ant_kar=Label(karakterstatistikk_vindu,textvariable=ant_kar)
    ent_ant_kar.grid(row=11,column=1,padx=5,pady=5,sticky=W)

    btn_avslutt=Button(karakterstatistikk_vindu,text='Tilbake', command=karakterstatistikk_vindu.destroy)
    btn_avslutt.grid(row=13,column=1,padx=(5,10),pady=5,sticky=E)


    karakterstatistikk_vindu.mainloop() 


#Kobler mot database
mindatabase=mysql.connector.connect(
    host='localhost', 
    port=3306, 
    user='Eksamenssjef ',
    passwd='oblig2021', 
    db='oblig2021')

window=Tk()
window.title('Hovedmeny')

#Student-meny

lbl_studentmeny=Label(window,text='Studentmeny:',font='Calibri 13 bold')
lbl_studentmeny.grid(row=0,column=0,padx=5,pady=10,sticky=W)

btn_leggtil_student=Button(window,width=30,text='Legg til student',command=open_legg_student_vindu)
btn_leggtil_student.grid(row=1,column=0,columnspan=2,padx=10,pady=5)
#Legg til student
btn_endre_student=Button(window,width=30,text='Endre studentinformasjon',command=open_endre_student_vindu)
btn_endre_student.grid(row=2,column=0,columnspan=2,padx=10,pady=5)
#Endre student
btn_slett_student=Button(window,width=30,text='Slett en student',command=open_slett_student_vindu)
btn_slett_student.grid(row=3,column=0,columnspan=2,padx=10,pady=5)
#Slette student
btn_eksamensres_student=Button(window,width=30,text='Skriv ut eksamensresultater for student',command=open_karakterliste_student)
btn_eksamensres_student.grid(row=4,column=0,columnspan=2,padx=10,pady=5)
#Skriv ut eksamensresultater for en student
btn_vitnemal=Button(window,width=30,text='Skriv ut et vitnemål',command=open_vitnemal_vindu)
btn_vitnemal.grid(row=5,column=0,columnspan=2,padx=10,pady=5)


#Skriv ut Vitnemål
lbl_eksamensmeny=Label(window,text='Eksamensmeny:',font='Calibri 13 bold')
lbl_eksamensmeny.grid(row=6,column=0, padx=5,pady=(20,10), sticky=W)
#Eksamen-meny#
btn_registrer_eksamen=Button(window,width=30,text='Registrer en eksamen',command=open_legg_eksamen_vindu)
btn_registrer_eksamen.grid(row=7,column=0,columnspan=2,padx=10,pady=5)
#Registrer eksamen
btn_endre_eksamen=Button(window,width=30,text='Endre eksamensinformasjon',command=open_endre_eksamen_vindu)
btn_endre_eksamen.grid(row=8,column=0,columnspan=2,padx=10,pady=5)
#Endre eksamensinfo
btn_slett_eksamen=Button(window,width=30,text='Slett en eksamen', command=open_slett_eksamen_vindu)
btn_slett_eksamen.grid(row=9,column=0,columnspan=2,padx=10,pady=5)
#Slett eksamen
btn_oversikt_eksamen=Button(window,width=30,text='Skriv ut oversikt over eksamener',command=open_ustkrift_eksamen_vindu)
btn_oversikt_eksamen.grid(row=10,column=0,columnspan=2,padx=10,pady=5)
#Skriv ut oversikt over eksamener


lbl_eksamensresultatmeny=Label(window,text='Eksamensresultatmeny:',font='Calibri 13 bold')
lbl_eksamensresultatmeny.grid(row=11,column=0, padx=5,pady=(20,10), sticky=W)
#Eksamensresultater-meny#
btn_karakterliste=Button(window,width=30,text='Skriv ut karakterliste for et emne',command=open_emne_karakterliste_vindu)
btn_karakterliste.grid(row=12,column=0,columnspan=2,padx=10,pady=5)
#Eksamensresultater pr emne (karakterliste)
btn_legg_til_eksamenres=Button(window,width=30,text='Registrer karakterer for en eksamen',command=open_legg_eksamensresultat_vindu)
btn_legg_til_eksamenres.grid(row=13,column=0,columnspan=2,padx=10,pady=5)
#Legg til eksamensresultater
btn_endre_eksamensres=Button(window,width=30,text='Endre eksamensresultat for student', command=open_endre_eksamensresultat_vindu)
btn_endre_eksamensres.grid(row=14,column=0,columnspan=2,padx=10,pady=5)
#Endre eksamensresultater
btn_karakterstatistikk=Button(window,width=30,text='Se karakterstatistikk for et fag',command=open_karakterstatistikk_vindu)
btn_karakterstatistikk.grid(row=15,column=0,columnspan=2,padx=10,pady=5)
#Legg til samlede karakterer for en eksamen
#Karakterstatistikk 
btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=16,column=1,padx=10,pady=(20,5),sticky=E)

window.mainloop()

mindatabase.close()
