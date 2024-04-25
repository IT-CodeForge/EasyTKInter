[zurück zur Hauptseite](./_Dokumentation)

# Dokumentation für ETKContainer

## Einführung
Die `ETKContainer`-Klasse ist eine Erweiterung der [ETKNoTkBaseEvents](./ETKNoTkBaseEvents)-Klasse und dient als Container für GUI-Elemente. Sie ermöglicht die Verwaltung und Platzierung von Elementen innerhalb eines Containers.

## Importieren von Modulen
```python
from ETKBaseWidget import ETKBaseWidget
from ETKNoTKEventBase import ETKNoTKEventBase
from ETKBaseObject import BaseEvents
from vector2d import vector2d
from enum import Enum
import logging
```

## Enums

### Alignments (Enum)
- `TOP_LEFT`: Oben links ausrichten.
- `TOP_CENTER`: Oben zentriert ausrichten.
- `TOP_RIGHT`: Oben rechts ausrichten.
- `MIDDLE_LEFT`: Mittig links ausrichten.
- `MIDDLE_CENTER`: Mittig zentriert ausrichten.
- `MIDDLE_RIGHT`: Mittig rechts ausrichten.
- `BOTTOM_LEFT`: Unten links ausrichten.
- `BOTTOM_CENTER`: Unten zentriert ausrichten.
- `BOTTOM_RIGHT`: Unten rechts ausrichten.

## Klasse

### ETKContainer
#### Konstruktor
```python
def __init__(self, gui_object=None):
```
- `gui_object`: GUI-Objekt, dem der Container zugeordnet ist. Wenn nicht angegeben, werden die Position und die Abmessungen manuell festgelegt.

#### Attribute
- `__elements`: Liste der im Container enthaltenen Elemente.
- `__anchor`: Position des Ankers des Containers.
- `__my_pos`: Position des Containers.
- `__dimensions`: Abmessungen des Containers.

#### Methoden
- `add_element(element, allignment:Alignments=Alignments.TOP_LEFT)`: Fügt ein Element zum Container hinzu.
- `remove_element(element)`: Entfernt ein Element aus dem Container.
- `detach()`: Löst das `<Detach>`-Event aus.

#### Interne Methoden
- `__place_elements()`: Platzierung der Elemente im Container.
- `__ev_element_configured()`: Ereignisbehandlung für konfigurierte Elemente.
- `__ev_element_detached(params)`: Ereignisbehandlung für entfernte Elemente.

## Hinweis
Die `ETKContainer`-Klasse ist eine Basisklasse für Container in der GUI-Bibliothek. Sie ermöglicht das Hinzufügen und Entfernen von Elementen sowie deren Platzierung innerhalb des Containers.