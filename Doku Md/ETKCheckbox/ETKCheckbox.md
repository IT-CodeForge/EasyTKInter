[zurück zur Hauptseite](../Dokumentation)
# ETKCheckbox



## Initialisierung
```python
__init__(myTk:Tk, txt:str="", pos_x:int=0, pos_y:int=0, width:int=80, height:int=17, fill:int=0xEEEEEE, text_col:int=0x0)
```
### Parameter
* `myTk`: Das Tk-Objekt (in der Regle self.object_id vom ETKMainwindow); Datentyp: `Tk`
* `txt`: Der Text der auf der Checkbox steht; Datentyp: `str`; Standard: `""`
* `pos_x`: Die x-Position der oberen linken Ecke der Checkbox; Datentyp: `int`; Standard: `0`
* `pos_y`: Die y-Position der oberen linken Ecke der Checkbox; Datentyp: `int`; Standard: `0`
* `width`: Die Breite der Checkbox; Datentyp: `int`; Standard: `80`
* `height`: Die Höhe der Checkbox; Datentyp: `int`; Standard: `17`
* `fill`: Die Hintergrundfarbe der Checkbox; Datentyp: `int` (Farbe mit `0xRRGGBB`); Standard: `0xEEEEEE` (helles grau)
* `text_col`: Die Textfarbe des textes auf der Checkbox; Datentyp: `int` (Farbe mit `0xRRGGBB`); Standard: `0x000000` (schwarz)
---
## Attribute
* `anchor`: Die Position des Ursprungpunkts der Checkbox (`pos` ist relativ zu `anchor`); Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `pos`: Die Position der Checkbox; Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `width`: Die Breite der Checkbox wenn =None dann ist die Breite dynamisch (an Elemente angepasst); Datentyp: `int`; Standard: `None`
* `height`: Die Höhe der Checkbox; Datentyp: `int`; Standard: `None`
* `text`: Der Text auf der Checkbox; Datentyp: `str`; Standard: `""`
* `state`: Ob der haken gesetzt ist, oder nicht; Datentyp: `bool`; Standard: `False`
* `visible`: Ob die Checkbox angezeigt werden soll oder nicht; Datentype: `bool`; Standard: `True`
* `enabled`: Ob die Checkbox aktiviert oder deaktiviert ist, eine deaktivierte Checkbox löst keine CheckboxEvents aus; Datentyp: `bool`; Standard: `True`
## Methoden
### **move(move_vec:vector2d)**
Bewegt die Checkbox um einen Vektor (`neue_pos = alte_pos + move_vec`)
### Parameter
* `move_vec`: Der Vektor um den dei Checkbox verschoben werden soll; Datentyp: `vector2d`
### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myChb = ETKCheckbox(self.object_id, pos_x = 10, pos_y=10)
    print(self.myChb.pos) #gibt <10,10> zurück -> oberer linke ecke des Knopfs
    self.myChb.move(vector2d(10,5))
    print(self.myChb.pos) #gibt <20,15> zurück -> Checkbox wurde um <10,5> veschoben
```
### **add_event(event_type: BaseEvents | WindowEvents | str, eventhandler: Callable[..., None], truth_func: Optional[Callable[..., None]] = None)**
Fügt der Checkbox ein event hinzu, welches eine Funktion auslöst, sobald das event auslöst. Es gibt einen Eventtyp (mehr zu Events [hier](../Events_Doku/Events)):
* `CheckboxEvents`: Events, die nur die Checkbox hat
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
    self.myBtn.add_event(CheckboxEvents.CH_TOGGLED, self.__ev_press)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_press(self, object, event_type, event):
    print("jemand hat die Checkbox gedrückt")
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
    myBtn.add_event(ButtonEvents.CH_TOGGLED, self.__ev_press)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_press(self, object, event_type, event):
    print("jemand hat die Checkbox gedrückt")
    self.myBtn.remove_event(CheckboxEvents.BTN_PRESSED, self.__ev_press)
    #dass Event wird einmal ausgelöst und danach nie wieder
```
---
## Implementierung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myChb = ETKheckbox(self.object_id, "Ich bin eine Checkbox", 20, 10, 128, 32, 0xFF0000, 0x00FF00)
    #Eine roter Checkbox bei <20,10> mit einer Breite von 128 und einer Höhe von 32
    #auf dem in blauer Schrift steht: "Ich bin eine Checkbox".
```