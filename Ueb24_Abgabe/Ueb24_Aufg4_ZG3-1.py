import mein_paket.MADfunkt as muf #eigenes Modul importiert,aus Blatt 17
from tkinter import * #tkinter importiert für GUI Modellierung


fenster=Tk() #Fenster Objekt erzeugt
fenster.title("MAD-Rechner") #Titel des Fenster Objekts
fenster.geometry("250x140") #Größe des Fenster Objekt (breite mal höhe in Pixeln)

lbl_sysBl = Label(fenster, text="Eingabe Systol. Blutdruck") #Label Objekt für systolischen Blutdruck
lbl_sysBl.pack() #Label Objekt positioniert
txt_sysBl = Entry(fenster) #Eingabefeld für Benutzereingabe im Fenster. Entry Objekt
txt_sysBl.pack()#Entry Objekt platziert

lbl_diaBl = Label(fenster, text="Eingabe Diastol. Blutdruck")#zweites Label Objekt, Überschrift für Entry Objekt
lbl_diaBl.pack()#platziert
txt_diaBl = Entry(fenster)#Eingabefeld für diastolischen Blutdruck
txt_diaBl.pack()

lbl_mad = Label(text="MAD: ?") #Label über dem Button
lbl_mad.pack() 

def btn_berechne_click(): #Berechnung für den Button
    sys = float(txt_sysBl.get()) #wandelt texteingabe aus entry Feld in float und speichert in Variable
    dias = float(txt_diaBl.get())
    lbl_mad.configure(text = "MAD: " + str(muf.mad(sys,dias)))#Ausgabetext, nach Button betätigung. Gibt String MAD zurück mit konkatiniertem Ergebnisstring, Funktionsaufruf MAD aus eigenem Package.

btn_berechne = Button(fenster, text="Berechne MAD", command=btn_berechne_click) #Button Objekt erzeugt mit click-Funktion verknüpft, Text auf dem Button festgelegt
btn_berechne.pack()#postioniert

fenster.mainloop()#Fenster öffnet sich