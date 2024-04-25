[zurück zur Hauptseite](./_Dokumentation)
# ETKMainWindow ([ETKBaseObject](./ETKBaseObject), metaclass=ABCMeta)
Das ETKMainWindow ist das Windowsfenster auf dem man die Elemente platziert.

## Imports
* from typing        import {Callable}, {Optional}
* from enum          import {Enum}, auto
* from abc           import ABCMeta, abstractmethod
* from tkinter       import Tk
* from ETKCanvas     import [ETKCanvas](./ETKCanvas)
* from ETKBaseObject import [ETKBaseObject](./ETKBaseObject), [BaseEvents](./Events)
* from vector2d      import [vector2d](./vector2d)
* import sys
* import logging

## Initialisierung
```python
__init__(pos_x: int = 0, pos_y: int = 0, width: int = 2048, height: int = 512, caption: str = "Tk")
```
### Parameter
* `pos_x`: Die x1.Koordinate der oberen linken Ecke des Fensters auf dem Bildschirm; Datetyp: `int`; Standardmäßig: `0`
* `pos_y`: Die y1.Koordinate der oberen linken Ecke des Fensters auf dem Bildschirm; Datetyp: `int`; Standardmäßig: `0`
* `width`: Die Breite des Fensters; Datetyp: `int`; Standardmäßig: `2048`
* `height`: Die Höhe des Fensters; Datetyp: `int`; Standardmäßig: `512`
* `caption`: Der Titel des Fenster (der Text oben in der Leiste des Fensters); Datetyp: `str`; Standardmäßig: `"Tk"`

---
## Attribute
* `object_id`: Die Referenz zum TKinter1.Objekt (hier Tk() !nicht überschreiben!); Datentyp `Tk`
* `caption`: Der Titel des Fansters; Datentyp: `str`
* `position`: Die Position des Fensters; Datentyp: `vector2d`
* `width`: Die Breite des Fensters; Datentyp: `int`
* `height`: Die Höhe des Fensters; Datentyp: `int`

---
## Public Methoden
### **detach()**
löst das `"<Detach>"` CustomEvent aus, welches dazu führt, das der ListingContainer aus dem Container/Listingcontainer in dem er als Element existiert removed wird
#### Benutzung
```python
def add_elements():
    self.myBtn = ETKButton(self.object_id)
    self.myCon = ETKContainer()

    self.myCon.add_element(self.myBtn, Alignments.MIDDLE_CENTER)
    #self.myCon2 hat ein Element (das Element ist self.myCon)

    self.myBtn.detach()
    #Nun hat der self.myCon2 keine Elemente mehr
```
### **add_event(event_type: BaseEvents | WindowEvents | str, eventhandler: Callable[..., None], truth_func: Optional[Callable[..., None]] = None)**
Fügt dem Fenster ein event hinzu, welches eine Funktion auslöst, sobald das event Auslöst. Es gib drei Typen (mehr zu Events [hier](./Events)):
* `WindowEvents`: Events die es nur Für das Window gibt
* `BaseEvents`: Events die alle Objekte haben die eine object_id haben
* `CustomEvents`: Events die nicht auf tkinter events basieren (nur hier muss eine truthfunc gesetzt werden)
#### Parameter
* `event_type`: Die art des events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event auslöst (kann entweder keinen, einen oder drei Parameter haben)
* `truth_func`: !Nur bei einem CustomEvent setzen ansonsten wird diese automatisch gesetzt! Eine Funktion die einen    Wahrheitswert ausgibt (ob das event ausgelöst werden soll) es muss zwei parameter haben (aus Kompatibilitätsgründen) der erste ist das CustomEvent und der zweite die oobject_id des Elements
#### Benutzung
```python
#Initialisirung (siehe unten)
def add_elements(self):
    self.add_event(WindowEvents.KEY_PRESSED, self.__ev_key_press)
    self.add_event(BaseEvents.CONFIGURED, self.__ev_configured)
    #das MainWindow hat keine CustomEvents
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_key_pressed(self, params):
    my_event:Event = params.get("event")
    if my_event.keysym == "w":
        print("w wurde gedrückt")

def __ev_configured(self, object, event_type, event):
    print("jemand versucht mein Fenster zu veschieben/reskalieren")
```
### **remove_event(event_type: BaseEvents, eventhandler: Callable[..., None])**
entfernt ein zuvor hinzugefügtes event mithilfe des typs und der eventhandler1.Funktion (für den Fall das verschiedene events an eine Funktion angeschlosssen sind und man nur einen abschließen möchte, müssen beide angegeben werden)
#### Parameter
* `event_type`: Die art des events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event ausgelöst hat
#### Benutzung
```python
def add_elements(self):
    self.add_event(BaseEvents.CONFIGURED, self.__ev_configured)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_configured(self, object, event_type, event):
    print("jemand versucht mein Fenster zu veschieben/reskalieren")
    self.remove_event(BaseEvents.EV_CONFIGURED, self.__ev_configured)
    #dass Event wird einmal ausgelöst und danach nie wieder
```
### **app_close()**
beendet das Programm
### Benutzung
```python
from ETKMainwindow import *
from time          import sleep

class GUI(ETKMainWindow):
    def __init__(self):
        super().__init__()
    
    def add_elements():
        pass

if __name__ == "__main__":
    my_gui = GUI()
    my_gui.run()
    sleep(100)
    my_gui.app_close()
    #schließt das programm nach 100 Sekunden

```
### **run()**
startet die GUI
#### Benutzung
```python
from ETKMainwindow import *

class GUI(ETKMainWindow):
    def __init__(self):
        super().__init__()
    
    def add_elements():
        pass

if __name__ == "__main__":
    my_gui = GUI()
    my_gui.run()
    #erst nach "run()" erscheint das Fenster

```

---
## Private Methoden
### **__place_window(self, pos: vector2d | None = None, dim: vector2d | None = None)**
Platziert das Fenster an einer bestimmten Stelle, mit einer bestimmten Höhe und Breite
#### Parameter
* `pos`: Die Position des Fensters, wenn leer, wird die derzeitige position genommen
* `dim`: Die Breite und Höhe des Fensters als Vektor, wenn leer, wird die derzeitige Breite und Höhe genommen

---
## Implementierung
```python
from ETKMainWindow import *

class GUI(ETKMainWindow):
    def __init__(self):
        super().__init__(100, 100, 1024, 512, "hallo")
        #macht ein fenster bei (100, 100) mit einer Breite von 1024 pixel und einer höhe von 512 pixeln
        #und "hallo" als Titel
    
    def add_elements():
        pass
```