class Employee:
    def __init__(self, name: str, experience: int, *, positions: [str] = None) -> None:
        self.name = name
        self.experience = experience
        self.positions = positions or []

    @property
    def forename(self) -> str:
        return self.name.split(" ")[0]

    @property
    def surname(self) -> str:
        surname = self.name.split(" ")[-1]
        return surname if surname != self.forename else None

    def add_experience(self) -> None:
        self.experience += 1

    def add_position(self, title: str) -> None:
        self.positions.append(title)
