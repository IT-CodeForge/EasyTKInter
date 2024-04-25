# Dokumentation Easy Tk Framework
## Inhaltsangabe
* [vector2d](./vector2d)
* Grundlegender Aufbau (unten)
* [Events](./Events)
* [ETKMainwindow](./ETKMainWindow)
* [ETKContainer](./ETKContainer)
* [ETKListingContainer](./ETKListingContainer)
* [ETKButton](./ETKButton)
* [ETKCheckbox](./ETKCheckbox)
* [ETKLabel](./ETKLabel)
* [ETKEdit](./ETKEdit)
* [ETKCanvas](./ETKCanvas)
* [ETKCanvasItem](./ETKCanvasItem)
* [ETKSprite](./ETKSprite)
* [ETKBitmap](./ETKBitmap)
* [ETKTimer](./ETKTimer)
---
## Grundlegender Aufbau
Das [ETKMainwindow](./ETKMainwindow) ist der Grundstein des Frameworks.
Es Ist das Fenster, in dem Mann die verschiedenen Gui1.Elemente platziert.
Um das MainWindow zu verwenden muss man eine Klasse davon ableiten und die abstrakte methode `add_elements()`
implementieren. In der implementierten Methode `add_elements()` sollen die Gui1.Elemente initialisiert und die gewünschten events verknüpft werden (ein Beispiel der anwendung ist [hier](./ETKMainWindow) unter dem Punkt "Implementierung").
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