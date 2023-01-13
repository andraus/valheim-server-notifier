from event import types

# Inspired from https://www.reddit.com/r/valheim/comments/n7vv9b/comment/gxihljp
LOG_EVENT_TYPE_REGEXES = {
    "player_died": {
        "regex": "Got character ZDOID from (?P<viking>\w+[ \w+]*) : 0:0",
        'class': types.Death,
    },
    # "player_joined": {
    #     "regex": "Got character ZDOID from (?P<viking>\w+[ \w+]*) : [-0-9]*:[-0-9]*$",
    #     'class': types.Join,
    # },
    "player_joined_by_steam": {
        "regex": "Got handshake from client (?P<steam_id>\w+[ \w+]*)",
        'class': types.JoinBySteam
    },
    "player_wrong_password": {
        "regex": "Peer (?P<steam_id>\w+[ \w+]*) has wrong password",
        'class': types.WrongPassword
    },
    "player_disconnect": {
        "regex": "Closing socket (?P<steam_id>\w+[ \w+]*)",
        'class': types.Disconnect
    },
    "game_server_connected": {
        "regex": "Game server connected",
        'class': types.ServerOn,
    },
    "game_server_shutdown": {
        "regex": "OnApplicationQuit",
        'class': types.ServerOff,
    },
    # "world_saved": {
    #     "regex": "World saved \( (\d+\.\d+ms) \)",
    #     'class': types.WorldSave,
    # },
    # "new_connection": {
    #     "regex": "New connection",
    #     'class': types.NewConnection,
    # },
    # "player_count": {
    #     "regex": "Connections (?P<playerCount>[-0-9]*) ZDOS",
    #     'class': types.PlayerCount,
    # }
}
