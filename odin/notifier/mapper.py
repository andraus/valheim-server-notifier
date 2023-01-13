from event import types
from . import Template

class ServerOnTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        # payload['embeds'] = [{
        #     # 'author': {
        #     #     'name': 'Odin',
        #     #     'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
        #     # },
        #     'title': 'Valheim World Created',
        #     'description': 'This way, Tarnished.',
        # }]
        return payload



class ServerOffTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        # payload['embeds'] = [{
        #     # 'author': {
        #     #     'name': 'Odin',
        #     #     'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
        #     # },
        #     'title': 'Valheim World Ended...',
        #     'description': '...The battle is over, I see. To every living being, and every living soul.\rNow cometh the age of the stars.',
        # }]
        return payload



class JoinTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        # payload['embeds'] = [{
        #     # 'author': {
        #     #     'name': 'Odin',
        #     #     'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
        #     # },
        #     'title': f'{self.event.viking}, thou\'rt possessed of the power, no?',
        #     'description': 'But Tarnished, what business hast thou here?\rI have no memory of inking thee an invitation.',
        # }]
        return payload

class JoinBySteamTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        payload['embeds'] = [{
            'author': {
                'name': self.event.steam_user.nick,
                'icon_url': self.event.steam_user.avatar_url,
            },
            'title': f'I know thee, {self.event.steam_user.real_name}.',
            'description': 'heh',
        }]
        return payload

class DeathTemplate(Template):
    def get_payload(self) -> dict:
        payload = super().get_payload()
        # payload['embeds'] = [{
        #     # 'author': {
        #     #     'name': 'Odin',
        #     #     'icon_url': 'https://static.wikia.nocookie.net/marvel-contestofchampions/images/4/47/Odin_portrait.png/revision/latest?cb=20210307223313',
        #     # },
        #     'title': f'Quite the sleuth, aren\'t we, {self.event.viking}? But sadly for thee, destined death is here.',
        #     'description': 'Enough of thy unbearable breath.',
        # }]
        return payload

class NewConnectionTemplate(Template):
    def get_payload(self) -> dict:
        return super().get_payload()

class PlayerCountTemplate(Template):
    def get_payload(self) -> dict:
        return super().get_payload()

class WorldSaveTemplate(Template):
    pass


MAP = {
    types.ServerOn: ServerOnTemplate,
    types.ServerOff: ServerOffTemplate,
    types.Join: JoinTemplate,
    types.JoinBySteam: JoinBySteamTemplate,
    types.Death: DeathTemplate,
    types.WorldSave: WorldSaveTemplate,
    types.NewConnection: NewConnectionTemplate,
    types.PlayerCount: PlayerCountTemplate
}


def build_template(event: types.Event) -> Template:
    template = MAP.get(type(event))
    if not template:
        raise Exception(f'Template mapping for given event <{type(event)}> not found')

    return template(event)
