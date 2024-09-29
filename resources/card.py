class Card:
    def __init__(self, color: str, value: str):
        self.color = color
        self.value = value
        self._string_rep = f"{self.color}{self.value}"
        
    def __str__(self) -> str:
        return self._string_rep
        
    def __repr__(self) -> str:
        return self._string_rep
 