[zurück zur Hauptseite](./_Dokumentation)

# Dokumentation für ETKListingContainer

## Einführung
Die `ETKListingContainer`-Klasse ist eine Erweiterung der [ETKNoTkBaseEvents](./ETKNoTkBaseEvents)-Klasse und stellt einen Container dar, der seine enthaltenen Elemente in einer bestimmten Anordnung darstellt. Dieser Container unterstützt verschiedene Anordnungstypen wie von oben nach unten, von unten nach oben, von links nach rechts und von rechts nach links.

## Importieren von Modulen
```python
from typing import Any, Iterable
from ETKNoTKEventBase import ETKNoTKEventBase
from ETKBaseObject import BaseEvents, ETKBaseObject
from ETKBaseWidget import ETKBaseWidget
from vector2d import vector2d
from math import pi
from enum import Enum, auto
from ObservableTypes import ObservableList
from ETKContainer import Alignments, ETKContainer
```

## Klassen und Enums

### ListingTypes (Enum)
- `TOP_TO_BOTTOM`: Elemente werden von oben nach unten angeordnet.
- `BOTTOM_TO_TOP`: Elemente werden von unten nach oben angeordnet.
- `LEFT_TO_RIGHT`: Elemente werden von links nach rechts angeordnet.
- `RIGHT_TO_LEFT`: Elemente werden von rechts nach links angeordnet.

### ETKListingContainer

#### Konstruktor
```python
def __init__(self, gui_object=None, offset:int = 10, alignment:Alignments=Alignments.MIDDLE_LEFT, listing_type:ListingTypes=ListingTypes.TOP_TO_BOTTOM):
```
- `gui_object`: GUI-Objekt, dem der Container zugeordnet ist. Wenn nicht angegeben, werden die Position und die Abmessungen manuell festgelegt.
- `offset`: Abstand zwischen den Elementen im Container.
- `alignment`: Ausrichtung des Containers.
- `listing_type`: Anordnungstyp der Elemente im Container.

#### Attribute
- `anchor`: Position des Ankers des Containers.
- `pos`: Position des Containers.
- `width`: Breite des Containers.
- `height`: Höhe des Containers.
- `visible`: Sichtbarkeit des Containers.
- `alignment`: Ausrichtung des Containers.
- `listing_type`: Anordnungstyp der Elemente im Container.
- `offset`: Abstand zwischen den Elementen im Container.
- `elements`: Liste der im Container enthaltenen Elemente.

#### Methoden
- `detach()`: Löst das `<Detach>`-Event aus.

#### Interne Methoden
- `__place_elements()`: Platzierung der Elemente im Container.
- `__calc_child_pos(index:int, dynamic_dim:vector2d, vec_mask:vector2d, element_list:list) -> vector2d`: Berechnet die Position eines Kindelements basierend auf dem Index und den Dimensionen.
- `__get_mask_vec_and_dynamic_dim() -> Tuple[vector2d, vector2d]`: Berechnet die Vektoren und Dimensionen basierend auf dem Anordnungstyp.

## Hinweis
Die `ETKListingContainer`-Klasse erfordert die Verwendung anderer Module und Klassen wie `ETKNoTKEventBase`, `ETKBaseObject`, `ETKBaseWidget` usw. für ihre Funktionalität.