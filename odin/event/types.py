from . import Event


class Death(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking
        self.isDante = viking == 'Dantez'

    def __str__(self) -> str:
        return f'**Death beckons, Queer Tarnished {self.viking}. Be gone. Hapless scum.**' if self.isDante else f'**Death beckons, {self.viking}. Still, I have high hopes for thee.**'


class Join(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking
        self.isDante = viking == 'Kiazyd'

    def __str__(self) -> str:
        return f'**Trifle not with me, Queer Tarnished {self.viking}.**' if self.isDante else  f'**A pleasure to meet thee, Tarnished {self.viking}.**'


class ServerOn(Event):
    def __str__(self) -> str:
        return '🟢 **Server is ON and Running** 🟢'


class ServerOff(Event):
    def __str__(self) -> str:
        return f'🛑 **Server is OFF** 🛑'


class WorldSave(Event):
    duration: str

    def __init__(self, duration) -> None:
        self.duration = duration

    def __str__(self) -> str:
        return f'*World has been saved. It took {self.duration}!*'
