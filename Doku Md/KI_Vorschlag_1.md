### Documentation for ETKBaseWidget class

The `ETKBaseWidget` class is a base class for creating widgets in a GUI (Graphical User Interface) application. It provides functionality for managing widget properties such as position, size, visibility, and enabling/disabling.

#### Import Statements:
```python
from typing import Any
from vector2d import vector2d
from ETKBaseObject import ETKBaseObject
import logging
```

#### Logging Configuration (Optional):
The logging functionality is configured to log debug information to a file named `project.log` if the `LOG` variable is set to `True`. You can disable logging by setting `LOG` to `False`.

#### Class: ETKBaseWidget

##### Attributes:
- `object_id`: Stores a reference to the widget object.
- `__visibility`: Stores the visibility state of the widget.
- `__object_pos`: Stores the position of the widget.
- `__dimensions`: Stores the dimensions (size) of the widget.
- `__anchor`: Stores the anchor point relative to which the widget is positioned.
- `_state`: Stores the state of the widget (enabled or disabled).

##### Constructor:
```python
def __init__(self, pos: vector2d, dim: vector2d) -> None:
    """
    Initializes an instance of the ETKBaseWidget class.

    Args:
        pos (vector2d): The initial position of the widget.
        dim (vector2d): The initial dimensions (size) of the widget.
    """
```

##### Properties:
- `anchor`: Gets or sets the anchor point of the widget.
- `pos`: Gets or sets the position of the widget.
- `width`: Gets or sets the width of the widget.
- `height`: Gets or sets the height of the widget.
- `visible`: Gets or sets the visibility of the widget.
- `enabled`: Gets or sets the enabled state of the widget.

##### Methods:
- `move(self, mov_vec: vector2d)`: Moves the widget by the specified vector.
- `detach(self)`: Triggers a detach event for the widget.

##### Private Methods:
- `__place_object(self, pos: vector2d | None = None, dim: vector2d | None = None)`: Places the widget at a specified position with optional dimensions.

#### Example Usage:
```python
# Create an instance of ETKBaseWidget
widget = ETKBaseWidget(vector2d(100, 100), vector2d(200, 50))

# Set properties
widget.width = 300
widget.visible = True
widget.enabled = False

# Move the widget
widget.move(vector2d(50, 50))

# Detach the widget
widget.detach()
```

This documentation provides an overview of the `ETKBaseWidget` class, its attributes, properties, methods, and their usage.