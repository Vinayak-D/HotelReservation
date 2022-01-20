#enum class
from enum import Enum

class roomReservationStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    
class roomType(Enum):
    STANDARD = 1
    DELUXE = 2
    EXECUTIVE = 3