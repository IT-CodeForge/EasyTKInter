from ETKV2.Internal.ETKBaseObject import BaseEvents
from ETKV2.ETKBitmap import ETKBitmap
from ETKV2.ETKButton import ETKButton, ButtonEvents
from ETKV2.ETKCanvas import ETKCanvas
from ETKV2.ETKCanvasCircle import ETKCanvasCircle
from ETKV2.ETKCanvasItem import ETKCanvasItem  # NOTE
from ETKV2.ETKCanvasLine import ETKCanvasLine
from ETKV2.ETKCanvasOval import ETKCanvasOval
from ETKV2.ETKCanvasRectangle import ETKCanvasRectangle
from ETKV2.ETKCanvasSquare import ETKCanvasSquare
from ETKV2.ETKCheckbox import ETKCheckbox, CheckboxEvents
from ETKV2.Internal.ETKBaseContainer import Alignments, ContainerSize
from ETKV2.ETKContainer import ETKContainer
from ETKV2.ETKEdit import ETKEdit, EditEvents
from ETKV2.ETKLabel import ETKLabel
from ETKV2.ETKListingContainer import ETKListingContainer, ListingTypes
from ETKV2.ETKMainWindow import ETKMainWindow, WindowEvents
from ETKV2.ETKTimer import ETKTimer
from ETKV2.vector2d import vector2d


if __name__ == "__main__":
    # Alles importierte wird einmal verwendet, damit keine "WirdNichtVerwendet" Warnung getriggert wird.
    BaseEvents.ENTER
    ETKBitmap.abs_enabled
    ETKButton.abs_enabled
    ButtonEvents.PRESSED
    ETKCanvas.abs_enabled
    ETKCanvasCircle.background_color
    ETKCanvasItem.background_color
    ETKCanvasLine.background_color
    ETKCanvasOval.background_color
    ETKCanvasRectangle.background_color
    ETKCanvasSquare.background_color
    ETKCheckbox.abs_enabled
    CheckboxEvents.CHECKED
    Alignments.BOTTOM_CENTER
    ContainerSize.copy
    ETKContainer.abs_enabled
    ETKEdit.abs_enabled
    EditEvents.CHANGED
    ETKLabel.abs_enabled
    ETKListingContainer.abs_enabled
    ListingTypes.BOTTOM_TO_TOP
    ETKMainWindow.abs_pos
    WindowEvents.EXIT
    ETKTimer.mro
    vector2d.mro