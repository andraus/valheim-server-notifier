from requests import get

from lib.config import STEAM_API_ID
from . import Template

STEAM_API_URL_PLAYER_SUMMARY = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002'

class SteamUser(object):
    pass

def get_steam_user(steam_user_id: str):

    payload = get(STEAM_API_URL_PLAYER_SUMMARY,
        params={
            'key': STEAM_API_ID,
            'steamids': steam_user_id
        }).json()

    steam_user = SteamUser()
    steam_user.nick = payload['response']['players'][0]['personaname']
    steam_user.avatar = payload['response']['players'][0]['avatarfull']
    steam_user.real_name = payload['response']['players'][0]['realname']
    steam_user.steam_id = payload['response']['players'][0]['steamid']

    return steam_user

