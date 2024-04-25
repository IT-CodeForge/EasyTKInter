[zurück zur Hauptseite](../Dokumentation)
# ETKListingContainer
Der ETKListingContainer biete die Möglichkeit Elemente beliebig aufzulisten. Hierfür setzt es anchor und position des Elements. Somit ist ein Element in der Liste nicht verschiebbar (Änderungen von `anchor` und `pos` werden abgefangen und verhindert). Die Alignments, habe die selbe Funktion wie im [ETKContainer](../ETKContainer_Doku/ETKContainer) bloß hier auf die gesamte Auflistung angewandt Anstelle den einzelnen Elementen. Zudem kann man einen Auflistungstyp setzen, der Einstellt was für eine Liste man haben möchte (sollen die Elemente von links nach rechts, rechts nach links, oben nach unten oder unten nach oben aufgelistet werden).
## Initialisierung
```python
__init__(gui_object:ETKBaseWidget|ETKNoTkEventBase=None, offset:int = 10, alignment:Alignments=Alignments.MIDDLE_LEFT, listing_type:ListingTypes=ListingTypes.TOP_TO_BOTTOM)
```
### Parameter
* `gui_object`: Ein GUI_Element welches die pos, width und height des containers setzt; Datetyp: `ETKBaseWidget`(alle, die davon abgeleitet sind)
* `offset`: Der Abstand zwischen den aufgelisteten Elementen in Pixeln
* `alignment`: Bestimmt wo die Elemente im Container die aufgelistet werden:
    - `Alignments.TOP_LEFT`: Die Liste beginnt oben links im Container
    - `Alignments.TOP_CENTER`: Die Liste liegt oben im Zentrum des Containers
    - `Alignments.TOP_RIGHT`: Die Liste endet oben rechts im Container
    - `Alignments.MIDDLE_LEFT`: Die Liste liegt mittig links im Container
    - `Alignments.MIDDLE_CENTER`: Die Liste liegt mittig im Zentrum des Containers
    - `Alignments.MIDDLE_RIGHT`: Die Liste liegt mittig rechts im Container
    - `Alignments.BOTTOM_LEFT`: Die Liste beginnt unten links im Container
    - `Alignments.BOTTOM_CENTER`: Das Element liegt unten im Zentrum des Containers
    - `Alignments.BOTTOM_RIGHT`: Die Liste endet unten rechts im Container
* `listing_type`: Bestimmt die Art der Liste:
    - `ListingTypes.TOP_TO_BOTTOM`: Die Elemente werden von oben nach unten gelistet
    - `ListingTypes.BOTTOM_TO_TOP`: Die Elemente werden von unten nach oben gelistet
    - `ListingTypes.LEFT_TO_RIGHT`: Die Elemente werden von links nach rechts gelistet
    - `ListingTypes.RIGHT_TO_LEFT`: Die Elemente werden von rechts nach links gelistet

---
## Attribute
* `anchor`: Die Position des Ursprungpunkts des ListingContainers (`pos` ist relativ zu `anchor`); Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `pos`: Die Position des ListingContainers; Datentyp: `vector2d`; Standard: `vector2d(0,0)`
* `width`: Die Breite des ListingContainers wenn =None dann ist die Breite dynamisch (an Elemente angepasst); Datentyp: `int`; Standard: `None`
* `height`: Die Höhe des ListingContainers wenn =None dann ist die Höhe dynamisch (an Elemente angepasst); Datentyp: `int`; Standard: `None`
* `visible`: Ob das Element angezeigt werden soll oder nicht; Datentype: `bool`; Standard: `True`
* `alignments`: der Alignmenttyp des ListingContainers; Datentyp: `Allignments`; Standard: `Alignments.MIDDLE_LEFT`
* `listing_type`: Der Auflistungstyp des ListingContainers; Datentyp: `ListingTypes`; Standard: `ListingTypes.TOP_TO_BOTTOM`
* `elements`: Die Liste, mit allen GUI-Elementen die in der Liste sind. Zum Anhängen von GUI-Elementen einfach die Liste überschreiben (`myListCon.elements = [self.E1, self.E2, ...]`) oder über die Standard-Python-Listen-Befehle (Bspw.: `myListCon.elements.append(self.E1)` oder `myListCon.elements.remove(self.E1)` oder etc.); Datentyp `ObservableList`; Standard: `[]`
---
## Methoden
### **detach()**
löst das `"<Detach>"` CustomEvent aus, welches dazu führt, das der ListingContainer aus dem Container/Listingcontainer in dem er als Element existiert removed wird
#### Benutzung
```python
def add_elements():
    self.myListCon = ETKListingContainer()
    self.myCon2 = ETKContainer()
    self.myBtn = ETKButton(self.object_id)

    self.myListCon.elements.append(self.myBtn)
    self.myCon2.add_element(self.myListCon, Alignments.MIDDLE_CENTER)
    #self.myCon2 hat ein Element (das Element ist self.myCon)

    self.myListCon.detach()
    #Nun hat der self.myCon2 keine Elemente mehr
```
### **add_event(event_type: BaseEvents | WindowEvents | str, eventhandler: Callable[..., None], truth_func: Optional[Callable[..., None]] = None)**
Fügt dem ListingContainer ein event hinzu, welches eine Funktion auslöst, sobald das event Auslöst. Es gibt einen Eventtyp (mehr zu Events [hier](../Events_Doku/Events)):
* `CustomEvents`: Events die nicht auf tkinter events basieren (nur hier muss eine truthfunc gesetzt werden)
#### Parameter
* `event_type`: Die Art des Events (hier wird einer der drei Typen eingetragen (bei CustomEvent den string des Events))
* `eventhandler`: Die Funktion die aufgerufen wird, sobald das Event auslöst (kann entweder keinen, einen oder drei Parameter haben)
* `truth_func`: !Nur bei einem CustomEvent setzen ansonsten wird diese automatisch gesetzt! Eine Funktion die einen    Wahrheitswert ausgibt (ob das event ausgelöst werden soll) es muss zwei parameter haben (aus Kompatibilitätsgründen) der erste ist das CustomEvent und der zweite die oobject_id des Elements
#### Benutzung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myListCon = ETKListingContainer()
    self.myListCon.add_event("<Detach>", self.__ev_detached)
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
    self.myListCon = ETKListingContainer()
    myListCon.add_event("<Detach>", self.__ev_detached)
    #die Funktionen müssen nicht "privat" sein aber so ist da "Good practice"

def __ev_detached(self, object, event_type, event):
    print("Das Element, wurde gedetached")
    self.myListCon.remove_event("<Detach>", self.__ev_detached)
    #dass Event wird einmal ausgelöst und danach nie wieder
```
---
## Implementierung
```python
#Initialisierung siehe ETKMainWindow
def add_elements(self):
    self.myBtn = ETKButton(self.object_id)
    self.myListCon = ETKListingContainer(
        offset=20,
        alignment=Alignments.MIDDLE_CENTER,
        listing_type=ListingTypes.LEFT_TO_RIGHT)
    self.myListCon.elements = [self.myBtn]
```