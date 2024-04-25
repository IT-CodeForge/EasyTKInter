[zurück zur Hauptseite](./_Dokumentation)

# Dokumentation für ETKBaseObject

## Einführung
Die `ETKBaseObject`-Klasse ist eine Basisklasse für Objekte in der GUI-Bibliothek. Sie ermöglicht das Hinzufügen und Entfernen von Ereignissen sowie das Handhaben von GUI-Ereignissen wie Mausklicks, Tastendrücken usw.

## Importieren von Modulen
```python
from asyncio import events
from enum import Enum, auto
from abc import abstractmethod
from tkinter import Event, EventType
from typing import Any, Callable
import logging
```

## Konfiguration der Protokollierung
Die Konfiguration des Loggings kann über die Variable `LOG` gesteuert werden. Wenn `LOG` auf `True` gesetzt ist, werden Ereignisse in einer Protokolldatei ("project.log") protokolliert.

## Klassen und Enums

### BaseEvents (Enum)
- `MOUSE_DOWN`: Maustaste wird gedrückt.
- `MOUSE_UP`: Maustaste wird losgelassen.
- `HOVERED`: Mauszeiger betritt das Objekt.
- `LEAVE`: Mauszeiger verlässt das Objekt.
- `CONFIGURED`: Das Objekt wurde konfiguriert.

### ETKBaseObject
#### Konstruktor
```python
def __init__(self) -> None:
```
- `object_id`: ID des Objekts.
- `_event_lib`: Enthält Ereignisinformationen.
- `__type_trans`: Übersetzt Ereignistypen.
- `__event_trans`: Übersetzt Ereignisse in Standardereignisse.
- `__event_truth_funcs`: Funktionen zur Überprüfung der Ereigniswahrheit.

#### Methoden
- `add_event(event_type:BaseEvents, eventhandler:Callable[...,None], sequence:str=None, truth_func:Callable[..., None]|None=None)`: Fügt ein Ereignis hinzu.
- `remove_event(event_type:BaseEvents, eventhandler:Callable[..., None], sequence:str=None)`: Entfernt ein Ereignis.
- `_eventhandler(event:Event)`: Handhabt GUI-Ereignisse.

## Hinweis
Die `ETKBaseObject`-Klasse ist eine Basisklasse und erfordert eine spezifische Implementierung für die Verwendung in der GUI-Bibliothek.