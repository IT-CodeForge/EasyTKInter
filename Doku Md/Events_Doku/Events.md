[zurück zur Hauptseite](../Dokumentation)
//devnote evtl. mit gifs
# Events
Es gibt verschiedene Arten von Events. jedes Gui1.Element und das ETKMainWindow haben `BaseEvents`. Manche Objekte haben zusätzlich noch eigene Events, welche beim deaktivieren (`myElement.enabled = False`) nicht auslösen.

---
## BaseEvents
Diese events, kann man nur Elementen vom typ:
* [ETKMainWindow](../ETKMainWindow_Doku/ETKMainWindow)
* [ETKButton](../ETKButton_Doku/ETKButton)
* [ETKCheckbox](../ETKCheckbox_Doku/ETKCheckbox)
* [ETKLabel](../ETKLabel_Doku/ETKLabel)
* [ETKEdit](../ETKEdit_Doku/ETKEdit)
* [ETKCanvas](../ETKCanvas/ETKCanvas)
### BaseEvents.MOUSE_DOWN
Dieses Event löst aus, wenn der beutzer auf das Element klickt, zu dem es geaddet wurde.
### BaseEvents.MOUSE_UP
Dieses Event löst aus, wenn der beutzer aufhört auf das Element zu klicken, zu dem es geaddet wurde.
### BaseEvents.HOVERED
Dieses Event löst aus sobald der Benutzer mit seiner Maus auf das Element fährt.
### BaseEvents.LEAVE
Dieses Event löst aus sobald der Benutzer mit seiner Maus das Element verlässt.
### BaseEvents.CONFIGURED
Dieses Event löst aus wenn das Element verändert wird. Das heißt Position oder Größe wird verändert.

---
## WindowEvents
Diese Events, kann man nur Elementen vom Typ [ETKMainWindow](../ETKMainWindow_Doku/ETKMainWindow) hinzufügen.
### WindowEvents.MOUSE_MOVED
Dieses Event löst aus, wenn man die Maus über dem Fenster bewegt (und das Fenster im Fokus ist).
### WindowEvents.KEY_PRESSED
Dieses Event löst aus, wenn man eine Taste auf der Tastatur drückt.
### WindowEvents.KEY_RELEASED
Dieses Event löst aus, wenn man eine Taste auf der Tastatur loslässt.

---
## ButtonEvents
Diese Events, kann man nur Elementen vom Typ [ETKButton](../ETKMainWindow_Doku/ETKMainWindow) hinzufügen.
### ButtonEvents.BTN_PRESSED
Dieses Event löst aus, wenn man den Knopf drückt und dieser nicht deaktiviert ist.
### ButtonEvents.BTN_RELEASED
Dieses Event löst aus, wenn man den Knopf loslässte und dieser nicht deaktiviert ist.

---
## CheckboxEvents
Diese Events, kann man nur Elementen vom Typ [ETKButton](../ETKCheckbox_Doku/ETKCheckbox) hinzufügen.
### CheckboxEvents.CB_CHECKED
Dieses Event löst aus, wenn man in der Checkbox das Kreuz gesetzt wird und diese nicht deaktiviert ist.
### CheckboxEvents.EV_UNCHECKED
Dieses Event löst aus, wenn man in der Checkbox das Kreuz abgewählt wird und diese nicht deaktiviert ist.
### CheckboxEvents.EV_TOGGLED
Dieses Event löst aus, wenn sich der Zustand der Checkbox ändert und diese nicht deaktiviert ist.

---
## EditEvents
Diese Events, kann man nur Elementen vom Typ [ETKButton](../ETKMEdit_Doku/ETKEdit) hinzufügen.
### EditEvents.EV_CHANGED
Dieses Event löst aus, wenn man die Schrift des Edit's verändert und dieses nicht deaktiviert ist.

---
## CustomEvents
Diese events, kann man nur Elementen vom typ:
* [ETKMainWindow](../ETKMainWindow_Doku/ETKMainWindow)
* [ETKContainer](../ETKContainer_Doku/ETKContainer)
* [ETKListingContainer](../ETKListingContainer_Doku/ETKLstingContainer)
* [ETKButton](../ETKButton_Doku/ETKButton)
* [ETKCheckbox](../ETKCheckbox_Doku/ETKCheckbox)
* [ETKLabel](../ETKLabel_Doku/ETKLabel)
* [ETKEdit](../ETKEdit_Doku/ETKEdit)
* [ETKCanvas](../ETKCanvas/ETKCanvas)
* [ETKBitmap](../ETKBitmap_Doku/ETKBitmap)
### "<Visible\>"
Dieses Event löst aus, wenn das Element sichtbar oder Unsichtbar gemacht wird
### "<Detach\>"
Dieses Event löst aus, wenn der `detach()` Befehl ausgelöst wird.