from lib.config import DANTE_STEAM_ID
from . import Event

from notifier.steam import get_steam_user

class Death(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking
        self.isDante = viking == 'Dantez'

    def __str__(self) -> str:
        return f'Quite the sleuth, aren\'t we, Queer Tarnished **{self.viking}**? Be gone. Hapless scum.' if self.isDante else f'Death beckons, **{self.viking}**. Still, I have high hopes for thee.'


class Join(Event):
    viking: str

    def __init__(self, viking: str) -> None:
        self.viking = viking
        self.isDante = viking == 'Dantez'

    def __str__(self) -> str:
        return f'Trifle not with me, Queer Tarnished **{self.viking}**.' if self.isDante else  f'A pleasure to meet thee, Tarnished **{self.viking}**.'

class JoinBySteam(Event):
    steam_id: str

    def __init__(self, steam_id: str) -> None:
        self.steam_id = steam_id

        self.steam_user = get_steam_user(self.steam_id)
        self.steam_user.is_dante = self.steam_user.steam_id == DANTE_STEAM_ID

    def __str__(self) -> str:
        return f'Trifle not with me, Queer Tarnished **{self.steam_user.nick}**.' if self.steam_user.isDante else f'A pleasure to meet thee, Tarnished **{self.steam_user.nick}**.'

class PlayerCount(Event):
    def __init__(self, playerCount: str) -> None:
        self.playerCount = playerCount
    
    def __str__(self) -> str:
        return f'**{self.playerCount}** *Tarnished hunting for glory.*'

class ServerOn(Event):
    def __str__(self) -> str:
        return '🟢 Server is ON and Running 🟢 - *This way, Tarnished.*'


class ServerOff(Event):
    def __str__(self) -> str:
        return '🛑 Server is OFF 🛑 - *...The battle is over, I see. To every living being, and every living soul. Now cometh the age of the stars.*'

class NewConnection(Event):
    def __str__(self) -> str:
        return 'Incoming Tarnished...'

class WorldSave(Event):
    duration: str

    def __init__(self, duration) -> None:
        self.duration = duration

    def __str__(self) -> str:
        return f'*World has been saved. It took {self.duration}!*'
