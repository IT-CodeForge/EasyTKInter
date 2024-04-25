[zurück zur Hauptseite](./_Dokumentation)
# vector2d
## Imports
* from \_\_future\_\_ import {annotations}
* from typing import {Optional}
* import math

## Initialisierung
```python
__init__(self, x:Optional[float]=None, y:Optional[float]=None, lenght:Optional[float]=None, radians:Optional[float]=None)
```
Man kann einen 2d-Vektor auf zwei Arten Initialisieren. Mithilfe der x-y-Schreibweise (also wird der `x` und der `y` Parameter verwendet und die anderen nicht gesetzt). Mithilfe der Länge-Drehung-Schreibweise hier wird ein vektor mit der Länge `lenght` auf die x-Achse gelegt und danach um `radians` gedreht (also wird der `lenght` und der `radians` Parameter verwendet und die anderen nicht gesetzt). Der Default (also wenn die Falschen oder keine Parameter gesetzt werden) ist immer ein Null-Vektor
### Parameter (x-y-Schreibweise)
* `x`: Der x-Wert des Vektors
* `y`: Der y-Wert des Vektors
### Parameter (lenght-radians-Schreibweise)
* `lenght`: Die länge des Vektors
* `radians`: Um wie viele Bogenmaße, Der Vektor von der x-Achse nach links gdreht wird

---
## Attribute
* `lenght`: Die Länge des Vektors

---
## Operatoren
* `str`: `f"<{self.x},{self.y}>"`
* `+, +=`: `vector2d(self.x+other.x,self.y+other.y)`
* `-, -=`: `vector2d(self.x-other.x,self.y-other.y)`
* `*, *=`: `vector2d(self.x*other.x,self.y*other.y)`
* `/, /=`: `vector2d(self.x/other.x,self.y/other.y)`
* `//, //=`: `vector2d(self.x//other.x,self.y//other.y)`
* `%, %=`: `vector2d(self.x%other.x,self.y%other.y)`
* `**, **=`: `vector2d(self.x**other.x,self.y**other.y)`
* `==`: `self.x == other.x && self.y == other.y` oder `self.lenght == other`
* `<`: `self.x < other.x && self.y < other.y` oder `self.lenght < other`
* `<=`: `self.x <= other.x && self.y <= other.y` oder `self.lenght <= other`
* `>`: `self.x > other.x && self.y > other.y` oder `self.lenght > other`
* `<=`: `self.x >= other.x && self.y >= other.y` oder `self.lenght >= other`

---
## Public Methods
### **get_rotation()->float**
Gibt an wie viele Bogemaße der Vektor in Relation zur x-Achse gdreht ist.
#### Benutzung
```python
my_vec = vector2d(1, 1)
print(my_vec.get_rotation()) #gibt 0.785398 zurück
```
### **normalize(change_self:bool=True)->vector2d**
Normalisiert den Vektor (setzt seine Länge auf 1).
#### Parameter
* `change_self`: Wenn `True`, wird die normalisierung, auf den Vektor angewendet, Wenn `False` wird das Ergebnis nur zurückgegeben
#### Benutzung
```python
my_vec = vector2d(lenght=2, radians=6)
my_vec.normalize()
print(my_vec.lenght) #gibt 1 zurück
```
### **rotate(radians:float, change_self:bool=True)->vector2d**
dreht den Vektor um den Angegebenen Wert (In Bogenmaß) in Linksrichtung von der x-Achse aus.
#### Parameter
* `radians`: Um wie viel der Vektor gedreht werden soll (in Bogenmaß)
* `change_self`: Wenn `True`, wird die normalisierung, auf den Vektor angewendet, Wenn `False` wird das Ergebnis nur zurückgegeben
#### Benutzung
```python
my_vec = vector2d(lenght=1; radians=0)
my_vec.rotate(math.pi)
print(my_vec) #gibt <0,1> zurück
```
### **switch(change_self:bool=True)->vector2d**
wechselt die x-Koordinate mit der y-Koordinate des Vektors.
#### Parameter
* `change_self`: Wenn `True`, wird die normalisierung, auf den Vektor angewendet, Wenn `False` wird das Ergebnis nur zurückgegeben
#### Benutzung
```python
my_vec = vector2d(2,4)
print(my_vec.switch()) #gibt <4,2> zurück
```
### **get_angle_to_vec(vector:vector2d)->float**
Gibt den (kleineren) Winkel zwischen zwei Vektoren zurück (in Bogenmaß)
#### Parameter
* `vector`: Der vektor, zu dem der Winkel berechnet wird
#### Benutzung
```python
my_vec1 = vector2d(1,0)
my_vec2 = vector2d(-2,0)
print(my_vec1.get_angle_to_vec(my_vec2)) #gibt pi (3.1415) zurück
```
### **dotproduct(vector:vector2d)->float**
Gibt das Skalarprodukt (x1\*x2+y1\*y2) von diesem und dem Parameter-Vektor zurück.
#### Parameter
* `vector`: Der vektor, zu dem der Skalarprodukt berechnet wird berechnet wird
#### Benutzung
```python
my_vec1 = vector2d(1,3)
my_vec2 = vector2d(-2,4)
print(my_vec1.dotproduct(my_vec2)) #gibt pi 10 zurück
```
### **crossproduct(vector:vector2d)->float**
Gibt das Kreuzprodukt (x1\*y2-x2\*y1) von diesem und dem Parameter-Vektor zurück.
#### Parameter
* `vector`: Der vektor, zu dem das Kreuzprodukt berechnet wird berechnet wird
#### Benutzung
```python
my_vec1 = vector2d(1,3)
my_vec2 = vector2d(-2,4)
print(my_vec1.dotproduct(my_vec2)) #gibt pi 10 zurück
```

---
## Private Methoden
### **__get_lenght()->float**
Gibt die Länge zurück

---
## Impelmentierung
```python
my_vec = vector2d(3,5)
```