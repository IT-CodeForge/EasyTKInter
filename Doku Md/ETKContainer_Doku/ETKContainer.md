[zurück zur Hauptseite](../Dokumentation)
# ETKContainer
Der ETKContainer bietet die möglichkeit Objekte relativ zu sich selbst zu positionieren. So kann man bestimmen, ob das Element (wenn`element.pos = vector2d(0,0)` ist) oben links im Container ist, in der mitte, etc. (weitere informationen in der methode `add_element` unten). Der Container erlaubt den Elementen das behalten ihrer Position nur das sie nach der inklusion einen anderen Ursprung (anchor) haben und dieser von dann an unveränderbar ist.
## Initialisierung
```python
__init__(gui_object:ETKBaseWidget|ETKNoTkEventBase=None)
```
### parameter
* `gui_object`: Ein GUI_Element welches die pos, width und height des containers setzt; Datetyp: `ETKBaseWidget`(alle, die davon abgeleitet sind)

---
## Attribute
* `anchor`: Die Position des Ursprungpunkts des Containers (`pos` ist relativ zu `anchor`); Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `pos`: Die Position des Containers; Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `width`: Die Breite des Containers; Datentyp wenn =None dann ist die Breite dynamisch (an Elemente angepasst): `int`; Standard: `None`
* `height`: Die Höhe des Containers wenn =None dann ist die Höhe dynamisch (an Elemente angepasst); Datentyp: `int`; Standard: `None`
* `visible`: Ob das Element angezeigt werden soll oder nicht; Datentype: `bool`; Standard: `True`
---
## Methoden
### **add_element(element:ETKBaseWidget|ETKNoTkEventBase, allignment:Alignments=Alignments.TOP_LEFT)**
Fügt dem Container ein Element hinzu, setzt denn `anchor` des Elements und verknüpft das Element mit dem container (damit er abfangen kann, wenn beispielsweise der `anchor` des Elements geändert wird und diese Änderung verhindert)
#### Parameter
* `element`: Ein Element, welches in den Container reingemacht werden soll (das Element ist entweder von ETKBaseWidget oder ETKNoTkEventBase abgeleitet (volständige Liste [hier](../Dokumentation) unter Ableitungsaufbau))
* `allignment`: Bestimmt relativ zu welchem Punkt der anchor gesetzt wird:
    - `Alignments.TOP_LEFT`: Das Element liegt oben links im Container
    - `Alignments.TOP_CENTER`: Das Element liegt oben in der Mitte des Containers
    - `Alignments.TOP_RIGHT`: Das Element liegt oben rechts im Container
    - `Alignments.MIDDLE_LEFT`: Das Element liegt mittig links im Container
    - `Alignments.MIDDLE_CENTER`: Das Element liegt mittig in der Mitte des Containers
    - `Alignments.MIDDLE_RIGHT`: Das Element liegt mittig rechts im Container
    - `Alignments.BOTTOM_LEFT`: Das Element liegt unten links im Container
    - `Alignments.BOTTOM_CENTER`: Das Element liegt unten in der Mitte des Containers
    - `Alignments.BOTTOM_RIGHT`: Das Element liegt unten rechts im Container
#### Benutzung
```python
#GUI Initialisierungscode
def add_elements():
    self.myCon = ETKContainer()
    self.myBtn = ETKButton(self.object_id)

    self.myCon.add_element(self.myBtn, Alignments.MIDDLE_CENTER)
    #Button wurde zu dem Container hinzugefügt
```
### **remove_element(element:ETKBaseWidget|ETKNoTkEventBase)**
Entnimmt ein Element wieder aus dem Container und setzt den `anchor` auf `vector2d(0,0)`
#### Parameter
* `element`: : Ein Element, welches aus den Container entfernt werden soll (das Element ist entweder von ETKBaseWidget oder ETKNoTkEventBase abgeleitet (volständige Liste [hier](../Dokumentation) unter Ableitungsaufbau))
#### Benutzung
```python
#GUI Initialisierungscode
def add_elements():
    self.myCon = ETKContainer()
    self.myBtn = ETKButton(self.object_id)
    self.myCon.add_element(self.myBtn, Alignments.MIDDLE_CENTER)

    self.myCon.remove_element(self.myBtn)
    #Button wurde wieder aus dem Container entfernt
```
### **detach()**
löst das `"<Detach>"` CustomEvent aus, welches dazu führt, das der Container aus dem Container/Listingcontainer in dem er als Element existiert removed wird
#### Benutzung
```python
def add_elements():
    self.myCon = ETKContainer()
    self.myCon2 = ETKContainer()
    self.myBtn = ETKButton(self.object_id)

    self.myCon.add_element(self.myBtn, Alignments.MIDDLE_CENTER)
    self.myCon2.add_element(self.myCon, Alignments.MIDDLE_CENTER)
    #self.myCon2 hat ein Element (das Element ist self.myCon)

    self.myCon.detach()
    #Nun hat der self.myCon2 keine Elemente mehr
```
### **add_event(event_type: BaseEvents | WindowEvents | str, eventhandler: Callable[..., None], truth_func: Optional[Callable[..., None]] = None)**
Fügt dem Container ein event hinzu, welches eine Funktion auslöst, sobald das event Auslöst. Es gibt einen Eventtyp (mehr zu Events [hier](../Events_Doku/Events)):
* `CustomEvents`: Events die nicht auf tkinter events basieren (nur hier muss eine truthfunc gesetzt werden)
#### Parameter
* `event_type`: Die Art des Events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event auslöst (kann entweder keinen, einen oder drei Parameter haben)
* `truth_func`: !Nur bei einem CustomEvent setzen ansonsten wird diese automatisch gesetzt! Eine Funktion die einen    Wahrheitswert ausgibt (ob das event ausgelöst werden soll) es muss zwei parameter haben (aus Kompatibilitätsgründen) der erste ist das CustomEvent und der zweite die oobject_id des Elements
#### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myCon = ETKContainer()
    self.myCon.add_event("<Detach>", self.__ev_detached)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_detached(self, object, event_type, event):
    print("Das Element, wurde gedetached")
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
    self.myCon = ETKContainer()
    myCon.add_event("<Detach>", self.__ev_detached)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_detached(self, object, event_type, event):
    print("Das Element, wurde gedetached")
    self.myCon.remove_event("<Detach>", self.__ev_configured)
    #dass Event wird einmal ausgelöst und danach nie wieder
```
---
## Implementierung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id)
    self.myCon = ETKContainer(self.myBtn)
```