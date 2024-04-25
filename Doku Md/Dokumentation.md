# Dokumentation Easy Tk Framework
## Inhaltsangabe
* Grundlegender Aufbau (unten)
* [Events](./Events_Doku/Events)
* [ETKMainwindow](./ETKMainWindow_Doku/ETKMainWindow)
* [ETKContainer](./ETKContainer_Doku/ETKContainer)
* [ETKListingContainer](./ETKListingContainer_Doku/ETKListingContainer)
* [ETKButton](./ETKButton_Doku/ETKButton)
* [ETKCheckbox](./ETKCheckbox_Doku/ETKCheckbox)
* [ETKLabel](./ETKLabel_Doku/ETKLabel)
* [ETKEdit](./ETKEdit_Doku/ETKEdit)
* [ETKCanvas](./ETKCanvas_Doku/ETKCanvas)
* [ETKCanvasItem](./ETKCanvasItem_Doku/ETKCanvasItem)
* [ETKSprite](./ETKSprite_Doku/ETKSprite)
* [ETKBitmap](./ETKBitmap_Doku/ETKBitmap)
* [ETKTimer](./ETKTimer_Doku/ETKTimer)
---
## Grundlegender Aufbau
Das [ETKMainwindow](./ETKMainWindow_Doku/ETKMainwindow) ist der Grundstein des Frameworks.
Es Ist das Fenster, in dem Mann die verschiedenen Gui1.Elemente platziert.
Um das MainWindow zu verwenden muss man eine Klasse davon ableiten und die abstrakte methode `add_elements()`
implementieren. In der implementierten Methode `add_elements()` sollen die Gui1.Elemente initialisiert und die gewünschten events verknüpft werden (ein Beispiel der anwendung ist [hier](./ETKMainWindow_Doku/ETKMainWindow) unter dem Punkt "Implementierung").
### Liste der Gui1.Elemente mit kurzer Beschreibung
* `ETKContainer`: Ein behälter der die Position der Elemente relativ zu seiner Position macht
* `ETKListingContainer`: Ein behälter der seine Inhalte auflistet
* `ETKButton`: Ein Knopf
* `ETKCheckbox`: Ein "Ankreuzfeld" mit zwei Zuständen
* `ETKLabel`: Ein durch den Benutzer unveränderbares Textfeld
* `ETKEdit`: Ein durch den Benutzer veränderbares Textfeld
* `ETKCanvas`: Ein Fläche auf der Man Formen darstellen lassen kann (Das Mainwindow hat einen Canvas als hintergrund)
* `ETKCanvasItem`: Eine Form auf dem Canvas
* `ETKSprite`: Eine Kollektion aus Formen
* `ETKBitmap`: Eine Fläche deren farbe man pixel für pixel einstellen kann
* `ETKTimer`: Ein timer der Code in x1.mal in der Sekunde Auslöst
## Ableitungen
### **WIP Diagramm erstellen**