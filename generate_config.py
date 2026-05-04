import os
import json

def get_env(key, default=None, cast=str):
    value = os.getenv(key, default)
    if value is None:
        return None

    try:
        if cast == bool:
            return str(value).lower() in ("1", "true", "yes", "on")
        return cast(value)
    except Exception:
        return default

config = {
    "DiscordConfig": {
        "DiscordToken": get_env("DISCORD_TOKEN", ""),
        "DiscordBroadcastChannel": get_env("DISCORD_BROADCAST_CHANNEL", ""),
        "DiscordAlertUserID": get_env("DISCORD_ALERT_USER_ID", ""),
        "DiscordDebugChannel": get_env("DISCORD_DEBUG_CHANNEL", "")
    },
    "ArchipelagoConfig": {
        "ArchipelagoServer": get_env("ARCHIPELAGO_SERVER", "wss://archipelago.gg"),
        "ArchipelagoPort": get_env("ARCHIPELAGO_PORT", 12345, int),
        "ArchipelagoPassword": get_env("ARCHIPELAGO_PASSWORD", ""),
        "ArchipelagoBotSlot": get_env("ARCHIPELAGO_BOT_SLOT", "Bridgeipelago"),
        "ArchipelagoTrackerURL": get_env("ARCHIPELAGO_TRACKER_URL", ""),
        "ArchipelagoServerURL": get_env("ARCHIPELAGO_SERVER_URL", ""),
        "UniqueID": get_env("UNIQUE_ID", "")
    },
    "ItemFilterConfig": {
        "BotItemSpoilTraps": get_env("BOT_ITEM_SPOIL_TRAPS", True, bool),
        "BotItemFilterLevel": get_env("BOT_ITEM_FILTER_LEVEL", 0, int)
    },
    "RelayConfig": {
        "ChatMessages": get_env("CHAT_MESSAGES", True, bool),
        "ServerChatMessages": get_env("SERVER_CHAT_MESSAGES", True, bool),
        "GoalMessages": get_env("GOAL_MESSAGES", True, bool),
        "ReleaseMessages": get_env("RELEASE_MESSAGES", True, bool),
        "CollectMessages": get_env("COLLECT_MESSAGES", True, bool),
        "CountdownMessages": get_env("COUNTDOWN_MESSAGES", True, bool),
        "DeathlinkMessages": get_env("DEATHLINK_MESSAGES", True, bool),
        "APClientHelp": get_env("APCLIENT_HELP", False, bool),
        "APClientLicense": get_env("APCLIENT_LICENSE", False, bool),
        "APClientCountdown": get_env("APCLIENT_COUNTDOWN", False, bool),
        "APClientOptions": get_env("APCLIENT_OPTIONS", False, bool),
        "APClientAdmin": get_env("APCLIENT_ADMIN", False, bool),
        "APClientPlayers": get_env("APCLIENT_PLAYERS", False, bool),
        "APClientStatus": get_env("APCLIENT_STATUS", False, bool),
        "APClientRelease": get_env("APCLIENT_RELEASE", False, bool),
        "APClientCollect": get_env("APCLIENT_COLLECT", False, bool),
        "APClientRemaining": get_env("APCLIENT_REMAINING", False, bool),
        "APClientMissing": get_env("APCLIENT_MISSING", False, bool),
        "APClientChecked": get_env("APCLIENT_CHECKED", False, bool),
        "APClientAlias": get_env("APCLIENT_ALIAS", False, bool),
        "APClientGetItem": get_env("APCLIENT_GET_ITEM", False, bool),
        "APClientHint": get_env("APCLIENT_HINT", False, bool),
        "APClientHintLocation": get_env("APCLIENT_HINT_LOCATION", False, bool),
        "APClientVideo": get_env("APCLIENT_VIDEO", False, bool)
    },
    "DrawbridgeConfig": {
        "DiscordBridgeEnabled": get_env("DISCORD_BRIDGE_ENABLED", False, bool)
    },
    "MetaConfig": {
        "FlavorDeathlink": get_env("FLAVOR_DEATHLINK", False, bool),
        "DeathlinkLottery": get_env("DEATHLINK_LOTTERY", False, bool)
    },
    "AdvancedConfig": {
        "LoggingDirectory": get_env("LOGGING_DIRECTORY", "/logs/"),
        "PlayerRegistrationDirectory": get_env("PLAYER_REGISTRATION_DIRECTORY", "/RegistrationData/"),
        "PlayerItemQueueDirectory": get_env("PLAYER_ITEM_QUEUE_DIRECTORY", "/ItemQueue/"),
        "ArchipelagoDataDirectory": get_env("ARCHIPELAGO_DATA_DIRECTORY", "/ArchData/"),
        "QueueOverclock": get_env("QUEUE_OVERCLOCK", 1, int),
        "SnoozeCompletedGames": get_env("SNOOZE_COMPLETED_GAMES", False, bool),
        "JoinMessage": get_env("JOIN_MESSAGE", ""),
        "DebugMode": get_env("DEBUG_MODE", False, bool),
        "DiscordJoinOnly": get_env("DISCORD_JOIN_ONLY", False, bool),
        "SelfHostNoWeb": get_env("SELF_HOST_NO_WEB", False, bool),
        "CycleDiscord": get_env("CYCLE_DISCORD", 0, int)
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("config.json generated successfully.")
