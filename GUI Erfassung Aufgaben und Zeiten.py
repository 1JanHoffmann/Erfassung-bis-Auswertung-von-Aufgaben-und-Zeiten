import tkinter
import pandas as pd
import time
import Statistische_Auswertung_Automatic_Schedule_V4 as sa
from datetime import datetime
import datetime
import sys

'''
To Dos:

Zu welcher Tageszeit kann man welchen kohgnitiven load gut bewältigen?
Wie groß ist die Streuung?
Was macht den Unterschied zwischen guten und schlechten Zeitpunkten?

- Statistische Auswertung welcher Load zu welcher Tageszeit mit welcher Dauer möglich ist
weitere Faktoren denkbar:
- Motivation / persönliches Interesse abfragen
- Amount of Sleep
- Ernährung / Hydration
- Freitext was hat die Aufgabe gefördert 
- Freitextwas hat die Aufgabe gebremmst?
Visualisierung der gefundenen Daten und Nutzung zur Planung von Aufgaben und realistischen Einschätzung
Gezielt Flow-Faktoren finden und reproduzieren
'''


# Vorhandene Daten öffnen / neu erstellen und in "data" speichern
try:
    data = open("AufgabenZeiten.csv").read()
    print("________________________________")
    print("\nBestehende Aufgaben-Daten gefunden. \n")
except:
    data = open("AufgabenZeiten.csv", "w")
    print("\nNeue Aufgabenliste angelegt! \n")

def test():
    l3['text']='Hier würde ein neuer Text stehen'

def neu():
    global neu_fenster
    global l3
    global e3
    global e4

    l3.destroy()
    data = open("AufgabenZeiten.csv", "w")
    data.write("Aufgabe,Zeit\n")

    neu_fenster = tkinter.Tk()
    neu_fenster.title('Neu anlegen')
    l7 = tkinter.Label(master=neu_fenster, text='Aufgabe')
    l7.pack(padx=10, pady=10)
    e3 = tkinter.Entry(master=neu_fenster)
    e3.pack(padx=10)
    l8 = tkinter.Label(master=neu_fenster, text='Zeit [Minuten]')
    l8.pack(padx=10, pady=10)
    e4 = tkinter.Entry(master=neu_fenster)
    e4.pack(padx=10)
    bh2 = tkinter.Button(master=neu_fenster, text='Submit', command=lambda:[submit_neu(),aktualisieren()], fg='black')
    bh2.pack(pady=10)

    data = open("AufgabenZeiten.csv").read()
    l3 = tkinter.Label(master=f1, text=data)
    l3.grid(row=1, column=0, pady=12, padx=10, columnspan=5)

    l3['text']=' '
    data = open("AufgabenZeiten.csv").read()
    l3 = tkinter.Label(master=f1, text=data)
    l3.grid(row=1, column=0, pady=12, padx=10, columnspan=5)
    aktualisieren()
    

def aktualisieren():
    global l3
    l3.destroy()
    data = open("AufgabenZeiten.csv").read()
    l3 = tkinter.Label(master=f1, text=data)
    l3.grid(row=1, column=0, pady=12, padx=10, columnspan=5)
    print('Aktualisiert')
   
def hinzufügen():
    global hinzufügen_fenster
    global e1
    global e2
    hinzufügen_fenster = tkinter.Tk()
    hinzufügen_fenster.title('Hinzufügen')
    l9 = tkinter.Label(master=hinzufügen_fenster, text='Aufgabe')
    l9.pack(padx=10, pady=10)
    e1 = tkinter.Entry(master=hinzufügen_fenster)
    e1.pack(padx=20)
    l10 = tkinter.Label(master=hinzufügen_fenster, text='Zeit [Minuten]')
    l10.pack(padx=10, pady=10)
    e2 = tkinter.Entry(master=hinzufügen_fenster)
    e2.pack(padx=10)
    bh1 = tkinter.Button(master=hinzufügen_fenster, text='Submit', command=lambda:[submit_ergänzen(),aktualisieren()], fg='black')
    bh1.pack(pady=10)
    

def submit_ergänzen():
    result_e1 = e1.get()
    result_e2 = e2.get()
    data = open("AufgabenZeiten.csv", "a")
    toWrite = str(result_e1 + "," + result_e2)
    data.write(toWrite)
    data.write("\n")
    data.close()
    hinzufügen_fenster.destroy()

def submit_neu():
    result_e3 = e3.get()
    result_e4 = e4.get()
    data = open("AufgabenZeiten.csv", "a")
    toWrite = str(result_e3 + "," + result_e4)
    data.write(toWrite)
    data.write("\n")
    data.close()
    neu_fenster.destroy()
    
def nachtragen():
    global e5, e6, e7, e8, nachtragen_fenster

    # Fenster erstellen
    nachtragen_fenster = tkinter.Tk()
    nachtragen_fenster.title('Nachtragen')

    l12 = tkinter.Label(master=nachtragen_fenster, text='Aufgabe')
    l12.pack(padx=10, pady=10)
    e5 = tkinter.Entry(master=nachtragen_fenster)
    e5.pack(padx=20)

    l13 = tkinter.Label(master=nachtragen_fenster, text='Wann war die Aufgabe fertig? [hh:mm]')
    l13.pack(padx=10, pady=10)
    e6 = tkinter.Entry(master=nachtragen_fenster)
    e6.pack(padx=20)

    l14 = tkinter.Label(master=nachtragen_fenster, text='Verwendete Zeit [Minuten]')
    l14.pack(padx=10, pady=10)
    e7 = tkinter.Entry(master=nachtragen_fenster)
    e7.pack(padx=20)

    l15 = tkinter.Label(master=nachtragen_fenster, text='Kommentar zu der Aufgabe')
    l15.pack(padx=10, pady=10)
    e8 = tkinter.Entry(master=nachtragen_fenster)
    e8.pack(padx=20)

    bh1 = tkinter.Button(master=nachtragen_fenster, text='Submit', command=lambda:[submit_nachtragen(),aktualisieren_statistik()], fg='black')
    bh1.pack(pady=10)

def submit_nachtragen():
    global l1

    # Einholer von User-Informationen
    fertig = e6.get() 
    aufgabe = e5.get()
    zeit = e7.get()
    kommentar = e8.get()
    # Vollumfänglichen Timestamp von heute nehmen, zu einer Liste aufsplitten  
    date = datetime.datetime.now()
    usedate = str(date.strftime("%c"))
    date_liste = usedate.split()
    # Die Uhrzeitangabe gegen die User-Eingabe austauschen, wieder zu einem ganzen String joinen
    date_liste[3] = fertig + ":00"
    usedate = ' '.join(date_liste)
    # Neue Daten in das Dokument schreiben
    data = open("ErledigteAufgaben.csv", "a")
    toWrite = str(usedate + "," + zeit + "," + aufgabe + ","  + kommentar)
    data.write(toWrite)
    data.write("\n")
    data.close()
    print("\nAufgabe erfolgreich nachgetragen!\n")
    l1_aktualisieren()
    nachtragen_fenster.destroy()

def aktualisieren_statistik():
    sa.auswertung()

def stoppuhr():
    '''
    (Destroy Label l6)
    Erzeuge auf dem Space (im neuen Fenster) 2 neue Label: 
        Startzeit: %Timestamp [hh:mm]
        Button: Fertig
    Bei Klick auf Button fertig:
        öffne neues Fenster 'Stoppuhr'
        - Textfeld Name der Aufgabe
        - Textfeld Kommentar
        - Label Aktueller Timestamp- Timestamp zu Beginn: Du hast X Minuten gearbeitet.
        - Button Submit der die Eingaben in die Datenbank schreibt und das Fenster schließt
    '''
    from datetime import datetime
    timestamp_start = time.time()
    date_time = datetime.fromtimestamp(timestamp_start)
    str_date_time = date_time.strftime("%H:%M")
    startzeit = str_date_time



    

    def abschließen():
        #global endzeit, es1, es2
        global load, difficulty

        '''Hier einfügen:
        kognitiver Load und Anstrengung, jeweils 5-stufig.
        Bei der Erstellung der ErledigteAufgaben.csv -Datei die Spalten 'Kognitiver Load' und 'Anstrengung' ergänzen '''
        ls8 = tkinter.Label(master=stoppuhr_fenster, text='Kognitiver Load Aufgabe:')
        ls8.grid(row=3, column=1, pady=12, padx=10)
        ls9 = tkinter.Label(master=stoppuhr_fenster, text='Gefühl beim abarbeiten')
        ls9.grid(row=5, column=1, pady=12, padx=10)
        load = tkinter.StringVar()
        difficulty = tkinter.StringVar()
        options = [
            'sehr leicht', 
            'leicht', 
            'mittel', 
            'schwer', 
            'sehr schwer'
            ]
        #load.set(options[2])
        #difficulty.set(options[2])
        om1 = tkinter.OptionMenu(stoppuhr_fenster, load, *options)
        om1.config(fg='black')
        om1.grid(row=4, column=1, sticky='ew')
        om2 = tkinter.OptionMenu(stoppuhr_fenster, difficulty, *options)
        om2.config(fg='black')
        om2.grid(row=6, column=1, sticky='ew')
        #load = load.get()
        #difficulty = difficulty.get()

        def submit_stoppuhr():
            global l1, load, difficulty
            load = load.get()
            difficulty = difficulty.get()
            # Einholer von User-Informationen
            fertig = endzeit
            aufgabe = es1.get()
            kommentar = es2.get()
            date = datetime.now()
            usedate = str(date.strftime("%c"))
            # Neue Daten in das Dokument schreiben
            data = open("ErledigteAufgaben.csv", "a")
            ''' 
           load = load.get()
            difficulty = difficulty.get()
            '''

            toWrite = str(usedate + "," + str(zeit) + "," + aufgabe + ","  + kommentar + ","  + str(load) + ","  + str(difficulty))
            data.write(toWrite)
            data.write("\n")
            data.close()
            print("\nAufgabe erfolgreich nachgetragen!\n")
            l1 = tkinter.Label(master=f2, text=aktuell_df_cut, anchor='w')#
            l1.grid(row=1, column=0, pady=12, padx=10, sticky='n')
            l1_aktualisieren()
            stoppuhr_fenster.destroy()

        bs2.destroy()
        timestamp_ende = time.time()
        date_time = datetime.fromtimestamp(timestamp_ende)
        str_date_time = date_time.strftime("%H:%M")
        endzeit = str_date_time

        startzeit_stunden = int(startzeit[:2])
        startzeit_minuten = int(startzeit[3:])
        endzeit_stunden = int(endzeit[:2])
        endzeit_minuten = int(endzeit[3:])
        zeit = (endzeit_stunden - startzeit_stunden) * 60 + endzeit_minuten - startzeit_minuten

        ls5 = tkinter.Label(master=stoppuhr_fenster, text=f'Du hast {zeit} Minuten gearbeitet.')
        ls5.grid(row=2, column=0, pady=12, padx=10)
        ls3 = tkinter.Label(master=stoppuhr_fenster, text='Aufgabe')
        ls3.grid(row=3, column=0, pady=12, padx=10)
        # Aufgabe
        es1 = tkinter.Entry(master=stoppuhr_fenster)
        es1.grid(row=4, column=0)
        ls4 = tkinter.Label(master=stoppuhr_fenster, text='Kommentar')
        ls4.grid(row=5, column=0, pady=12, padx=10)
        # Kommentar
        es2 = tkinter.Entry(master=stoppuhr_fenster)
        es2.grid(row=6, column=0)
        bs1 = tkinter.Button(master=stoppuhr_fenster, text='Submit', command= submit_stoppuhr, width=9, fg='black')
        bs1.grid(row=7, column=0)
        ls6 = tkinter.Label(master=stoppuhr_fenster, text='Endzeit:')
        ls6.grid(row=1, column=0, pady=12, padx=10)
        ls7 = tkinter.Label(master=stoppuhr_fenster, text=endzeit)
        ls7.grid(row=1, column=1, pady=12, padx=10)

      




        
        
    stoppuhr_fenster = tkinter.Tk()
    stoppuhr_fenster.title('Stoppuhr')
    ls1 = tkinter.Label(master=stoppuhr_fenster, text='Startzeit:')
    ls1.grid(row=0, column=0, pady=12, padx=10)
    ls2 = tkinter.Label(master=stoppuhr_fenster, text=startzeit)
    ls2.grid(row=0, column=1, pady=12, padx=10)
    bs2 = tkinter.Button(master=stoppuhr_fenster, text='Abschließen', command=abschließen, width=9, fg='black')
    bs2.grid(row=1, column=0)

def custom():
    global custom_fenster
    def schließen():
        custom_fenster.destroy()
    custom_fenster = tkinter.Tk()
    custom_fenster.title('Custom')
    # Deepdive
    bc1 = tkinter.Button(master=custom_fenster, text='Statistik', command=schließen, width=9, fg='black')
    bc1.pack()
    # Beispielsweise Morgenroutine
    bc2 = tkinter.Button(master=custom_fenster, text='Feste Programme', command=schließen, width=9, fg='black')
    bc2.pack()
    bc3 = tkinter.Button(master=custom_fenster, text='Ziele', command=ziele_öffnen, width=9, fg='black')
    bc3.pack()
    bc4 = tkinter.Button(master=custom_fenster, text='DUMMY', command=schließen, width=9, fg='black')
    bc4.pack()
    bc5 = tkinter.Button(master=custom_fenster, text='Schließen', command=schließen, width=9, fg='black')
    bc5.pack(pady=20)

def l1_aktualisieren():
    global aktuell_df_cut, l1

    l1.destroy()
    # Erledigte Aufgaben einlesen und Datum formatieren, in neue Spalten schreiben
    link ='ErledigteAufgaben.csv'
    df = pd.read_csv(link)
    df[['Day','Month',"Number","Time", "year"]] = df.Datum.str.split(expand=True) 

    # Aktuellen Timestamp holen und nach den Bestanteilen in eine Liste schreiben
    timestamp = datetime.datetime.now()
    usedate = str(timestamp.strftime("%c"))
    date_liste = usedate.split()

    # Den bestehenden df filtern, danach die unnötigen Zeilen ausschneiden
    aktuell_df = df[(df.year == date_liste[4]) & (df.Month == date_liste[1]) & (df.Number == date_liste[2])]
    aktuell_df_cut = aktuell_df[['Aufgabentext', '[Minuten]']]

    l1 = tkinter.Label(master=f2, text=aktuell_df_cut, anchor='n')
    l1.grid(row=1, column=0, pady=12, padx=10)


def ziele_öffnen():
    custom_fenster.destroy()
    try:
        ziele_kf = open("Ziele_kf.csv").read()
        print("________________________________")
        print("\nBestehende Ziel-Daten-kf gefunden. \n")
    except:
        ziele_kf = open("Ziele_kf.csv", "w")
        print("\nNeue Ziel-Liste_kf angelegt! \n")
    try:
        ziele_mf = open("Ziele_mf.csv").read()
        print("________________________________")
        print("\nBestehende Ziel-Daten-mf gefunden. \n")
    except:
        ziele_mf = open("Ziele_mf.csv", "w")
        print("\nNeue Ziel-Liste_mf angelegt! \n")
    try:
        ziele_lf = open("Ziele_lf.csv").read()
        print("________________________________")
        print("\nBestehende Ziel-Daten-lf gefunden. \n")
    except:
        ziele_lf = open("Ziele_lf.csv", "w")
        print("\nNeue Ziel-Liste_lf angelegt! \n")

    ziele_fenster = tkinter.Tk()
    ziele_fenster.title('Ziele')
    lz1 = tkinter.Label(master=ziele_fenster, text='kf', width=25, bg='green', fg='white')
    lz1.grid(row=0, column=0, padx=10, pady=15)
    lz1a = tkinter.Label(master=ziele_fenster, text=ziele_kf, width=25, fg='white')
    lz1a.grid(row=1, column=0, padx=10)
   

    lz2 = tkinter.Label(master=ziele_fenster, text='mf', width=25, bg='green', fg='white')
    lz2.grid(row=0, column=1, padx=5, pady=15)
    lz2a = tkinter.Label(master=ziele_fenster, text=ziele_mf, width=25, fg='white')
    lz2a.grid(row=1, column=1, padx=5)

    lz3 = tkinter.Label(master=ziele_fenster, text='lf', width=25, bg='green', fg='white')
    lz3.grid(row=0, column=2, padx=10, pady=15)
    lz3a = tkinter.Label(master=ziele_fenster, text=ziele_lf, width=25, fg='white')
    lz3a.grid(row=1, column=2, padx=10)

def login():
    print('Das ist ein Test')






















data = pd.read_csv('AufgabenZeiten.csv')
data = data.set_index('Aufgabe')
root = tkinter.Tk()
root.title('AufgabenZeiten')
#root.geometry('500x350')


# Frames: rows=2, columns=3 
# Clomun 1
f1 = tkinter.Frame(master=root, highlightbackground='green', highlightthickness=1)
f1.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
# Column 2
f2 = tkinter.Frame(master=root, highlightbackground='green', highlightthickness=1)
f2.grid(row=0, column=1, padx=10, pady=10)
f3 = tkinter.Frame(master=root, highlightbackground='green', highlightthickness=1)
f3.grid(row=1, column=1, padx=10, pady=10)
# Column 3
f4 = tkinter.Frame(master=root)
f4.grid(row=0, column=2, padx=10, pady=10)
f5 = tkinter.Frame(master=root)
f5.grid(row=1, column=2, padx=10, pady=10)


# Dataframe für Label 1 generieren
# Erledigte Aufgaben einlesen und Datum formatieren, in neue Spalten schreiben
link ='ErledigteAufgaben.csv'
df = pd.read_csv(link)
df[['Day','Month',"Number","Time", "year"]] = df.Datum.str.split(expand=True) 

# Aktuellen Timestamp holen und nach den Bestanteilen in eine Liste schreiben
timestamp = datetime.datetime.now()
usedate = str(timestamp.strftime("%c"))
date_liste = usedate.split()

# Den bestehenden df filtern, danach die unnötigen Zeilen ausschneiden
aktuell_df = df[(df.year == date_liste[4]) & (df.Month == date_liste[1]) & (df.Number == date_liste[2])]
aktuell_df_cut = aktuell_df[['Aufgabentext', '[Minuten]']]
aktuell_df_cut = aktuell_df_cut.groupby('Aufgabentext', sort=False).sum()
heutige_Aufgabe_series = aktuell_df['Aufgabentext']
heutige_Zeiten_series = aktuell_df['[Minuten]']



 # Daten als DataFrame einlesen
link = "/Users/janhoffmann/ErledigteAufgaben.csv"
data_ErledigteAufgaben = pd.read_csv(link)
# Tabelle nach Aufgabentext mit der Funktion 'Summe' gruppieren und nach absteigender Gesamtdauer sortieren
categories = data_ErledigteAufgaben.groupby(['Aufgabentext']).sum()
categories = categories.sort_values(by=['[Minuten]'], ascending=False)
categories_top7 = categories[:7]
#categories_top7 = categories_top7.drop(['Load', 'Difficulty'], axis=1)

link = "/Users/janhoffmann/Ziele_kf.csv"
ziele_kf = pd.read_csv(link, names=None, header=None) #header=None, names=None,
link = "/Users/janhoffmann/Ziele_mf.csv"
ziele_mf = pd.read_csv(link, names=None, header=None)
link = "/Users/janhoffmann/Ziele_lf.csv"
ziele_lf = pd.read_csv(link, names=None, header=None)




# Labels
l1 = tkinter.Label(master=f2, text=aktuell_df_cut, anchor='n') # vorher: aktuell_df_cut
l1.grid(row=1, column=0, pady=12, padx=10, sticky='n')
l2 = tkinter.Label(master=f1, text='Folgende Aufgaben stehen Heute an:', fg='white', bg='green', width=55)
l2.grid(row=0, column=0, pady=12, padx=0, columnspan=5)
l3 = tkinter.Label(master=f1, text=data)
l3.grid(row=1, column=0, pady=12, padx=10, columnspan=5)
#l4 = tkinter.Label(master=f1, text='Konsolenausgabe')
#l4.grid(row=2, column=0, pady=12, padx=10, columnspan=5)
l5 = tkinter.Label(master=f1, text='Aktuelle Aufgabe', fg='white', bg='black', width=15)
l5.grid(row=3, column=2, pady=12, padx=10, columnspan=3)
l6 = tkinter.Label(master=f1, text='Timer', fg='white', bg='black', width=15)
l6.grid(row=4, column=2, pady=12, padx=10, columnspan=3)
l11 = tkinter.Label(master=f1, text='')
l11.grid(row=6, column=0, pady=12, padx=10, columnspan=3)

label_titel_heutige_aufgaben = tkinter.Label(master=f2, text='Heute erledigt:', fg='white', bg='green', width=15)
label_titel_heutige_aufgaben.grid(row=0, column=0, pady=0, padx=10)
label_titel_auswertung = tkinter.Label(master=f3, text='Gesamt Auswertung:', fg='white', bg='green', width=15)
label_titel_auswertung.grid(row=0, column=0, pady=0, padx=10)
label_auswertung = tkinter.Label(master=f3, text=categories_top7, anchor='n') # categories_aufgaben
label_auswertung.grid(row=1, column=0, pady=12, padx=10)


# Buttons
b1 = tkinter.Button(master=f1, text='Löschen & neu', command=neu, width=9, fg='red')
b1.grid(row=3, column=0, pady=12, padx=10)
b2 = tkinter.Button(master=f1, text='Ergänzen', command=hinzufügen, width=9, fg='black')
b2.grid(row=3, column=1, pady=12, padx=10)
b3 = tkinter.Button(master=f1, text='Nachtragen', command=nachtragen, width=9, fg='black')
b3.grid(row=4, column=0, pady=12, padx=10)
b4 = tkinter.Button(master=f1, text='Auswertung', command=login, width=9, fg='violet')
b4.grid(row=4, column=1, pady=12, padx=10)
b5 = tkinter.Button(master=f1, text='Aufgabe Stoppuhr', command=stoppuhr, width=10, fg='black')
b5.grid(row=5, column=3, pady=12, padx=10)
b6 = tkinter.Button(master=f1, text='Weiter', command=login, width=9, fg='violet')
b6.grid(row=5, column=4, pady=12, padx=10)
b7 = tkinter.Button(master=f1, text='Custom', command=custom, width=9, fg='blue')
b7.grid(row=5, column=0, pady=12, padx=10)
b8 = tkinter.Button(master=f1, text='Aktualisieren', command=l1_aktualisieren, width=9, fg='black')
b8.grid(row=5, column=1, pady=12, padx=10)
    

root.mainloop()