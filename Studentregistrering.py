import os

def nystudent():
    
    funnet=False

    nyregistrering=True
    while nyregistrering==True:


        print()
        print('Du har valgt å registrere ny student.')
        print()
        
        inndata = input('Skriv inn studentnummer: ')
        
        #åpne studentfilen
        studentfil=open('student.txt', 'r')
        #Lese første
        studentnummer=studentfil.readline()

        #løkke for å finne studentnr
        while studentnummer!='':
            studentnummer=studentnummer.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')
            
            

            #Hvis student allerede er registrert
            if studentnummer == inndata:
                funnet=True
                print()
                print('Denne studenten er allerede registrert')
                print()
                
                
            #Leser neste    
            studentnummer=studentfil.readline()
            
           
        studentfil.close()
        
        if not funnet: 
            #Begynne registreringsprosessen
            
            print('Vennligst fyll inn informasjon om studenten')
            fornavn=input('Skriv inn fornavn: ')
            etternavn=input('Skriv inn etternavn: ')
            studie=input('Skriv inn studie: ')

            #åpne fil i append
            studentfil=open('student.txt', 'a')

            #Skriv inn i fil
            studentfil.write(str(inndata) + '\n')
            studentfil.write(fornavn + '\n')
            studentfil.write(etternavn + '\n')
            studentfil.write(studie + '\n')

            studentfil.close()
            print('Studenten er nå registrert.')

        valg=input('Ønsker du å gjøre en ny registrering? ja/nei ')
        if valg=='ja':
            nyregistrering=True
        if valg=='nei':
            nyregistrering=False
        



def slettstudent():

    funnet=False
    
    nysletting=True
    while nysletting==True:

        print()
        print('Du har valgt å slette student.')
        print()

        inndata=input('Skriv inn studentnummer: ')
        #Sjekker om studenten er i eksamensfilen
        
        eksamensfil=open('eksamensresultat.txt', 'r')

        #Leser første linje i eksamensfil

        fagkode=eksamensfil.readline()

        while fagkode!='':
            fagkode=fagkode.rstrip('\n')
            studentnummer=eksamensfil.readline().rstrip('\n')
            karakter=eksamensfil.readline().rstrip('\n')

            if studentnummer == inndata:
                funnet=True
            
            
            #Leser neste post

            fagkode=eksamensfil.readline()

        if studentnummer==inndata:
            print()
            print('Kan ikke utføre sletting')
            print('Studenten har én eller flere eksamenskarakterer registrert.')
            print('Dette gjør at studenten ikke kan slettes.')
            print()

            #Betingelse for sletting av student


        eksamensfil.close()
        

        if not funnet:

            
            studentfil=open('student.txt' , 'a')
            temp_fil=open('temp_fil.txt', 'w')

            studentnummer=studentfil.readline()
            
            while studentnummer!='':
                studentnummer=studentnummer.rstrip('\n')
                fornavn=studentfil.readline().rstrip('\n')
                etternavn=studentfil.readline().rstrip('\n')
                studium=studentfil.readline().rstrip('\n')

                if studentnummer!= inndata:
                    temp_fil.write(studentnummer + '\n')
                    temp_fil.write(fornavn + '\n')
                    temp_fil.write(etternavn + '\n')
                    temp_fil.write(studium + '\n')

                if studentnummer == inndata:
                    funnet=True

                studentnummer=studentfil.readline()

            studentfil.close()
            temp_fil.close()

            os.remove('student.txt')
            os.rename('temp_fil.txt','student.txt')

            print('Studenten er slettet')
            
            
        valg=input('Ønsker du å gjøre en ny sletting? ja/nei ')
        if valg=='ja':
            nysletting=True
        if valg=='nei':
            nysletting=False
         


def karakterutskrift():

  
    funnet=False
    
    nysletting=True
    while nysletting==True:

            print()
            print('Du har valgt å skrive ut karakterutskrift.')
            print()
            
            inndata=input('Skriv inn studentnummer: ')
        
            
            eksamensfil=open('eksamensresultat.txt', 'r')

            

            fagkode=eksamensfil.readline()

            while fagkode!='':
                fagkode=fagkode.rstrip('\n')
                studentnummer=eksamensfil.readline().rstrip('\n')
                karakter=eksamensfil.readline().rstrip('\n')

                if studentnummer == inndata:
                    print(studentnummer, fagkode, karakter)
                    funnet=True
                
                

                fagkode=eksamensfil.readline()

           
            eksamensfil.close()

            if not funnet:
                print('Du har skrevet et ugyldig studentnummer')

            if funnet:

                
                studentfil=open('student.txt' , 'r')
                

                studentnummer=studentfil.readline()
                
                while studentnummer!='':
                    studentnummer=studentnummer.rstrip('\n')
                    fornavn=studentfil.readline().rstrip('\n')
                    etternavn=studentfil.readline().rstrip('\n')
                    studium=studentfil.readline().rstrip('\n')


                    if studentnummer == inndata:
                        funnet=True
                        print(fornavn, etternavn, studium)

                    studentnummer=studentfil.readline()

                studentfil.close()


                emnefil=open('emne.txt', 'r')

                emnekode=emnefil.readline()

                while emnekode !='':
                    emnekode=emnekode.rstrip('\n')
                    fag=emnefil.readline().rstrip('\n')

                    if emnekode == fagkode:
                        funnet=True
                        print(fag)

                    emnekode=emnefil.readline()

                emnefil.close()

        
            
            
            valg=input('Ønsker du å gjøre en ny utskrift? ja/nei ')
            if valg=='ja':
                nysletting=True
            if valg=='nei':
                nysletting=False
         
    
def main():

    meny=True
    while meny==True:
        print()
        print('HOVEDMENY')
        print('-----------------------------------------------------------')
        print('1 - Legg til ny student')
        print('2 - Slett student')
        print('3 - Skriv ut karakterliste')
        print()
        print('4 - Avslutt prgrammet')
        print('-----------------------------------------------------------')
        print()

        print('Hva ønsker du å gjøre?')
        valg=int(input('Tast 1 , 2 , 3 eller 4 : '))        
        if valg==1:
            nystudent()
        elif valg==2:
            slettstudent()
        elif valg==3:
            karakterutskrift()
        elif valg==4:
            meny=False
            print()
            print('Du har valgt å avslutte programmet ')
            print('Programmet avsluttes')
            
        else:
            print('Du har tastet et ugyldig nummer')
            print()



main()
            

    
    

