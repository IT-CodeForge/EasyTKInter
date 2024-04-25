[zurück zur Hauptseite](../Dokumentation)
# ETKButton
Der ETKButton ist ein Knopf. Man kann ihm Events geben, fürs drücken und Loslassen des Knopfs. Diese Events lösen nur aus, wenn der Knopf aktiviert ist.
## Initialisierung
```python
__init__(myTk:Tk, txt:str="", pos_x:int=0, pos_y:int=0, width:int=80, height:int=17, fill:int=0xEEEEEE, text_col:int=0x0)
```
### Parameter
* `myTk`: Das Tk-Objekt (in der Regle self.object_id vom ETKMainwindow); Datentyp: `Tk`
* `txt`: Der Text der auf dem Knopf steht; Datentyp: `str`; Standard: `""`
* `pos_x`: Die x-Position der oberen linken Ecke des Knopfes; Datentyp: `int`; Standard: `0`
* `pos_y`: Die y-Position der oberen linken Ecke des Knopfes; Datentyp: `int`; Standard: `0`
* `width`: Die Breite des Knopfes; Datentyp: `int`; Standard: `80`
* `height`: Die Höhe des Knopfes; Datentyp: `int`; Standard: `17`
* `fill`: Die Hintergrundfarbe des Knopfes; Datentyp: `int` (Farbe mit `0xRRGGBB`); Standard: `0xEEEEEE` (helles grau)
* `text_col`: Die Textfarbe des textes auf dem Knopf; Datentyp: `int` (Farbe mit `0xRRGGBB`); Standard: `0x000000` (schwarz)
---
## Attribute
* `anchor`: Die Position des Ursprungpunkts des Knopfes (`pos` ist relativ zu `anchor`); Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `pos`: Die Position des Knopfes; Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `width`: Die Breite des Knopfes wenn =None dann ist die Breite dynamisch (an Elemente angepasst); Datentyp: `int`; Standard: `None`
* `height`: Die Höhe des Knopfes; Datentyp: `int`; Standard: `None`
* `text`: Der Text auf dem Knopf; Datentyp: `str`; Standard: `""`
* `visible`: Ob der Knopf angezeigt werden soll oder nicht; Datentype: `bool`; Standard: `True`
* `enabled`: Ob der Knopf aktiviert oder deaktiviert ist, ein deaktivierter Knopf löst keine ButtonEvents aus; Datentyp: `bool`; Standard: `True`
## Methoden
### **move(move_vec:vector2d)**
Bewegt den Knopf um einen Vektor (`neue_pos = alte_pos + move_vec`)
### Parameter
* `move_vec`: Der Vektor um den der Knopf verschoben werden soll; Datentyp: `vector2d`
### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id, pos_x = 10, pos_y=10)
    print(self.myBtn.pos) #gibt <10,10> zurück -> oberer linke ecke des Knopfs
    self.myBtn.move(vector2d(10,5))
    print(self.myBtn.pos) #gibt <20,15> zurück -> Knopf wurde um <10,5> veschoben
```
### **add_event(event_type: BaseEvents | WindowEvents | str, eventhandler: Callable[..., None], truth_func: Optional[Callable[..., None]] = None)**
Fügt dem Knopf ein event hinzu, welches eine Funktion auslöst, sobald das event auslöst. Es gibt einen Eventtyp (mehr zu Events [hier](../Events_Doku/Events)):
* `ButtonEvents`: Events, die nur der Knopf hat
* `BaseEvents`: Events die alle Objekte haben die eine object_id haben
* `CustomEvents`: Events die nicht auf tkinter events basieren (nur hier muss eine truthfunc gesetzt werden)
#### Parameter
* `event_type`: Die Art des Events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event auslöst (kann entweder keinen, einen oder drei Parameter haben)
* `truth_func`: !Nur bei einem CustomEvent setzen ansonsten wird diese automatisch gesetzt! Eine Funktion die einen    Wahrheitswert ausgibt (ob das event ausgelöst werden soll) es muss zwei parameter haben (aus Kompatibilitätsgründen) der erste ist das CustomEvent und der zweite die object_id des Elements
#### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id)
    self.myBtn.add_event(ButtonEvents.BTN_PRESSED, self.__ev_press)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_press(self, object, event_type, event):
    print("jemand hat den knopf gedrückt")
```
### **remove_event(event_type: BaseEvents, eventhandler: Callable[..., None])**
entfernt ein zuvor hinzugefügtes event mithilfe des typs und der eventhandler1.Funktion (für den Fall das verschiedene events an eine Funktion angeschlosssen sind und man nur einen abschließen möchte, müssen beide angegeben werden)
#### Parameter
* `event_type`: Die art des events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event ausgelöst hat
#### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id)
    myBtn.add_event(ButtonEvents.BTN_PRESSED, self.__ev_press)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_press(self, object, event_type, event):
    print("jemand hat den Knopf gedrückt")
    self.myBtn.remove_event(ButtonEvents.BTN_PRESSED, self.__ev_press)
    #dass Event wird einmal ausgelöst und danach nie wieder
```
### **detach()**
löst das `"<Detach>"` CustomEvent aus, welches dazu führt, das der Knopf aus dem Container/Listingcontainer in dem er als Element existiert removed wird
#### Benutzung
```python
def add_elements():
    self.myCon = ETKContainer()
    self.myBtn = ETKButton(self.object_id)

    self.myCon.add_element(self.myBtn, Alignments.MIDDLE_CENTER)
    #self.myCon2 hat ein Element (das Element ist self.myCon)

    self.myBtn.detach()
    #Nun hat der self.myCon keine Elemente mehr
```
---
## Implementierung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id, "Ich bin ein Knopf", 20, 10, 128, 32, 0xFF0000, 0x00FF00)
    #Ein roter Knopf bei <20,10> mit einer Breite von 128 und einer Höhe von 32
    #auf dem in blauer Schrift steht: "Ich bin ein Knopf".
```