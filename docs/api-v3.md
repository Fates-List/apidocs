# API v3
**API URL**: ``https://next.fateslist.xyz`` *or* ``https://api.fateslist.xyz`` (for now, can change in future)

## Authorization

- **Bot:** These endpoints require a bot token. 
You can get this from Bot Settings. Make sure to keep this safe and in 
a .gitignore/.env. A prefix of `Bot` before the bot token such as 
`Bot abcdef` is supported and can be used to avoid ambiguity but is not 
required. The default auth scheme if no prefix is given depends on the
endpoint: Endpoints which have only one auth scheme will use that auth 
scheme while endpoints with multiple will always use `Bot` for 
backward compatibility

- **Server:** These endpoints require a server
token which you can get using ``/get API Token`` in your server. 
Same warnings and information from the other authentication types 
apply here. A prefix of ``Server`` before the server token is 
supported and can be used to avoid ambiguity but is not required.

- **User:** These endpoints require a user token. You can get this 
from your profile under the User Token section. If you are using this 
for voting, make sure to allow users to opt out! A prefix of `User` 
before the user token such as `User abcdef` is supported and can be 
used to avoid ambiguity but is not required outside of endpoints that 
have both a user and a bot authentication option such as Get Votes. 
In such endpoints, the default will always be a bot auth unless 
you prefix the token with `User`

## Base Response

A default API Response will be of the below format:

```json
{
    "done": true,
    "reason": "Reason for success of failure, can be null",
    "context": "Any extra context"
}
```

## Core

### Index
#### GET /index

Returns the index for bots and servers

**API v2 analogue:** (no longer working) [Get Index](https://legacy.fateslist.xyz/docs/redoc#operation/get_index)

**Query parameters**

- **target_type** [String? | default = bot (type info may be incomplete, see example)]


**Example**

```json
{
    "target_type": "bot"
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "new": [
        {
            "guild_count": 0,
            "description": "",
            "banner": "",
            "nsfw": false,
            "votes": 0,
            "state": 0,
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "top_voted": [
        {
            "guild_count": 0,
            "description": "",
            "banner": "",
            "nsfw": false,
            "votes": 0,
            "state": 0,
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "certified": [
        {
            "guild_count": 0,
            "description": "",
            "banner": "",
            "nsfw": false,
            "votes": 0,
            "state": 0,
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "tags": [
        {
            "name": "",
            "iconify_data": "",
            "id": "",
            "owner_guild": null
        }
    ],
    "features": [
        {
            "id": "",
            "name": "",
            "viewed_as": "",
            "description": ""
        }
    ]
}
```


### Resolve Vanity
#### GET /code/{code}

Resolves the vanity for a bot/server in the list

**API v2 analogue:** (no longer working) [Get Vanity](https://legacy.fateslist.xyz/docs/redoc#operation/get_vanity)

**Path parameters**

- **code** [String (type info may be incomplete, see example)]


**Example**

```json
{
    "code": "my-vanity"
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "target_type": "bot | server",
    "target_id": "0000000000"
}
```


### Get Policies
#### GET /policies

Get policies (rules, privacy policy, terms of service)

**API v2 analogue:** (no longer working) [All Policies](https://legacy.fateslist.xyz/api/docs/redoc#operation/all_policies)

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "rules": {},
    "privacy_policy": {}
}
```


### Get Bot
#### GET /bots/{id}


Fetches bot information given a bot ID. If not found, 404 will be returned. 

This endpoint handles both bot IDs and client IDs

Differences from API v2:

- Unlike API v2, this does not support compact or no_cache. Owner order is also guaranteed
- *``long_description/css`` is sanitized with ammonia by default, use `long_description_raw` if you want the unsanitized version*
- All responses are cached for a short period of time. There is *no* way to opt out unlike API v2
- Some fields have been renamed or removed (such as ``promos`` which may be readded at a later date)

This API returns some empty fields such as ``webhook``, ``webhook_secret``, `api_token`` and more. 
This is to allow reuse of the Bot struct in Get Bot Settings which does contain this sensitive data. 

**Set the Frostpaw header if you are a custom client**


**API v2 analogue:** [Fetch Bot](https://legacy.fateslist.xyz/docs/redoc#operation/fetch_bot)

**Path parameters**

- **id** [i64 (type info may be incomplete, see example)]


**Example**

```json
{
    "id": 0
}
```

**Query parameters**

- **lang** [Optional <String> (type info may be incomplete, see example)]


**Example**

```json
{
    "lang": null
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    },
    "description": "",
    "tags": [],
    "created_at": "1970-01-01T00:00:00Z",
    "last_stats_post": "1970-01-01T00:00:00Z",
    "long_description": "blah blah blah",
    "long_description_raw": "blah blah blah unsanitized",
    "long_description_type": 2,
    "guild_count": 0,
    "shard_count": 493,
    "user_count": 0,
    "shards": [],
    "prefix": null,
    "library": "",
    "invite": null,
    "invite_link": "https://discord.com/api/oauth2/authorize....",
    "invite_amount": 48,
    "owners": [
        {
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            },
            "main": false
        }
    ],
    "owners_html": "",
    "features": [
        {
            "id": "",
            "name": "",
            "viewed_as": "",
            "description": ""
        }
    ],
    "state": 0,
    "page_style": 1,
    "website": null,
    "support": "",
    "github": null,
    "css": "<style></style>",
    "votes": 0,
    "total_votes": 0,
    "vanity": "",
    "donate": null,
    "privacy_policy": null,
    "nsfw": false,
    "banner_card": null,
    "banner_page": null,
    "keep_banner_decor": false,
    "client_id": "",
    "flags": [],
    "action_logs": [
        {
            "user_id": "",
            "action": 0,
            "action_time": "1970-01-01T00:00:00Z",
            "context": null
        }
    ],
    "uptime_checks_total": 30,
    "uptime_checks_failed": 19,
    "commands": {
        "default": [
            {
                "cmd_type": 0,
                "cmd_groups": [],
                "cmd_name": "",
                "vote_locked": false,
                "description": "",
                "args": [],
                "examples": [],
                "premium_only": false,
                "notes": [],
                "doc_link": "",
                "id": ""
            }
        ]
    },
    "resources": [
        {
            "id": "",
            "resource_title": "",
            "resource_link": "",
            "resource_description": ""
        }
    ],
    "webhook": "This will be redacted for Get Bot endpoint",
    "webhook_secret": "This will be redacted for Get Bot endpoint",
    "webhook_type": null,
    "api_token": "This will be redacted for Get Bot endpoint"
}
```


### Search List
#### GET /search?q={query}

Searches the list based on a query named ``q``

**API v2 analogue:** (no longer working) [Fetch Bot](https://legacy.fateslist.xyz/docs/redoc#operation/search_list)

**Query parameters**

- **q** [String? | default = mew (type info may be incomplete, see example)]


**Example**

```json
{
    "q": "mew"
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "bots": [
        {
            "guild_count": 0,
            "description": "",
            "banner": "",
            "nsfw": false,
            "votes": 0,
            "state": 0,
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "servers": [
        {
            "guild_count": 0,
            "description": "",
            "banner": "",
            "nsfw": false,
            "votes": 0,
            "state": 0,
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "profiles": [
        {
            "banner": "",
            "description": "",
            "user": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            }
        }
    ],
    "packs": [
        {
            "id": "0",
            "name": "",
            "description": "",
            "icon": "",
            "banner": "",
            "resolved_bots": [
                {
                    "user": {
                        "id": "",
                        "username": "",
                        "disc": "",
                        "avatar": "",
                        "bot": false
                    },
                    "description": ""
                }
            ],
            "owner": {
                "id": "",
                "username": "",
                "disc": "",
                "avatar": "",
                "bot": false
            },
            "created_at": "1970-01-01T00:00:00Z"
        }
    ],
    "tags": {
        "bots": [
            {
                "name": "",
                "iconify_data": "",
                "id": "",
                "owner_guild": null
            }
        ],
        "servers": [
            {
                "name": "",
                "iconify_data": "",
                "id": "",
                "owner_guild": null
            }
        ]
    }
}
```


### Random Bot
#### GET /random-bot


Fetches a random bot on the list

Example:
```py
import requests

def random_bot():
    res = requests.get(api_url"/random-bot")
    json = res.json()
    if res.status != 200:
        # Handle an error in the api
        ...
    return json
```


**API v2 analogue:** (no longer working) [Fetch Random Bot](https://legacy.fateslist.xyz/api/docs/redoc#operation/fetch_random_bot)

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "guild_count": 0,
    "description": "",
    "banner": "",
    "nsfw": false,
    "votes": 0,
    "state": 0,
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    }
}
```


### Random Server
#### GET /random-server


Fetches a random server on the list

Example:
```py
import requests

def random_server():
    res = requests.get(api_url"/random-server")
    json = res.json()
    if res.status != 200:
        # Handle an error in the api
        ...
    return json
```


**API v2 analogue:** (no longer working) [Fetch Random Server](https://legacy.fateslist.xyz/api/docs/redoc#operation/fetch_random_server)

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "guild_count": 0,
    "description": "",
    "banner": "",
    "nsfw": false,
    "votes": 0,
    "state": 0,
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    }
}
```


### Get Server
#### GET /servers/{id}


Fetches server information given a server/guild ID. If not found, 404 will be returned. 

Differences from API v2:

- Unlike API v2, this does not support compact or no_cache.
- *``long_description/css`` is sanitized with ammonia by default, use `long_description_raw` if you want the unsanitized version*
- All responses are cached for a short period of time. There is *no* way to opt out unlike API v2
- Some fields have been renamed or removed

**Set the Frostpaw header if you are a custom client**


**API v2 analogue:** (no longer working) [Fetch Server](https://legacy.fateslist.xyz/docs/redoc#operation/fetch_server)

**Path parameters**

- **id** [i64 (type info may be incomplete, see example)]


**Example**

```json
{
    "id": 0
}
```

**Query parameters**

- **lang** [Optional <String> (type info may be incomplete, see example)]


**Example**

```json
{
    "lang": null
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    },
    "description": "",
    "tags": [],
    "long_description_type": 0,
    "long_description": "",
    "long_description_raw": "",
    "vanity": null,
    "guild_count": 0,
    "invite_amount": 0,
    "created_at": "1970-01-01T00:00:00Z",
    "state": 0,
    "flags": [],
    "css": "",
    "website": null,
    "banner_card": null,
    "banner_page": null,
    "keep_banner_decor": false,
    "nsfw": false,
    "votes": 0,
    "total_votes": 0
}
```


### Get User Votes
#### GET /users/{user_id}/bots/{bot_id}/votes


Endpoint to check amount of votes a user has.

- votes | The amount of votes the bot has.
- voted | Whether or not the user has *ever* voted for the bot.
- vote_epoch | The redis TTL of the users vote lock. This is not time_to_vote which is the
elapsed time the user has waited since their last vote.
- timestamps | A list of timestamps that the user has voted for the bot on that has been recorded.
- time_to_vote | The time the user has waited since they last voted.
- vote_right_now | Whether a user can vote right now. Currently equivalent to `vote_epoch < 0`.

Differences from API v2:

- Unlike API v2, this does not require authorization to use. This is to speed up responses and 
because the last thing people want to scrape are Fates List user votes anyways. **You should not rely on
this however, it is prone to change *anytime* in the future**.
- ``vts`` has been renamed to ``timestamps``


**API v2 analogue:** (no longer working) [Get User Votes](https://legacy.fateslist.xyz/api/docs/redoc#operation/get_user_votes)

**Path parameters**

- **user_id** [i64 (type info may be incomplete, see example)]
- **bot_id** [i64 (type info may be incomplete, see example)]


**Example**

```json
{
    "user_id": 0,
    "bot_id": 0
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "votes": 10,
    "voted": true,
    "vote_right_now": false,
    "vote_epoch": 101,
    "time_to_vote": 0,
    "timestamps": [
        "1970-01-01T00:00:00Z"
    ]
}
```


### Post Stats
#### GET /bots/{bot_id}/stats


Post stats to the list

Example:
```py
import requests

# On dpy, guild_count is usually the below
guild_count = len(client.guilds)

# If you are using sharding
shard_count = len(client.shards)
shards = client.shards.keys()

# Optional: User count (this is not accurate for larger bots)
user_count = len(client.users) 

def post_stats(bot_id: int, guild_count: int):
    res = requests.post(f"{api_url}/bots/{bot_id}/stats", json={"guild_count": guild_count})
    json = res.json()
    if res.status != 200:
        # Handle an error in the api
        ...
    return json
```


**API v2 analogue:** (no longer working) [Post Stats](https://legacy.fateslist.xyz/api/docs/redoc#operation/set_stats)

**Request Body**

```json
{
    "guild_count": 3939,
    "shard_count": 48484,
    "shards": [
        149,
        22020
    ],
    "user_count": 39393
}
```

**Response Body**

```json
{
    "guild_count": 0,
    "description": "",
    "banner": "",
    "nsfw": false,
    "votes": 0,
    "state": 0,
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    }
}
```


### Mini Index
#### GET /mini-index


Returns a mini-index which is basically a Index but with only ``tags``
and ``features`` having any data. Other fields are empty arrays/vectors.

This is used internally by sunbeam for the add bot system where a full bot
index is too costly and making a new struct is unnecessary.


**API v2 analogue:** None

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "new": [],
    "top_voted": [],
    "certified": [],
    "tags": [
        {
            "name": "",
            "iconify_data": "",
            "id": "",
            "owner_guild": null
        }
    ],
    "features": [
        {
            "id": "",
            "name": "",
            "viewed_as": "",
            "description": ""
        }
    ]
}
```


### Gets Bot Settings
#### GET /users/{user_id}/bots/{bot_id}/settings


Returns the bot settings.

The ``bot`` key here is equivalent to a Get Bot response with the following
differences:

- Sensitive fields (see examples) like ``webhook``, ``api_token``, 
``webhook_secret`` and others are filled out here
- This API only allows bot owners to use it, otherwise it will 400!

Staff members *should* instead use Lynx.

Due to massive changes, this API cannot be mapped onto any v2 API


**API v2 analogue:** None

**Path parameters**

- **user_id** [i64 (type info may be incomplete, see example)]
- **bot_id** [i64 (type info may be incomplete, see example)]


**Example**

```json
{
    "user_id": 0,
    "bot_id": 0
}
```

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "new": [],
    "top_voted": [],
    "certified": [],
    "tags": [
        {
            "name": "",
            "iconify_data": "",
            "id": "",
            "owner_guild": null
        }
    ],
    "features": [
        {
            "id": "",
            "name": "",
            "viewed_as": "",
            "description": ""
        }
    ]
}
```


## Auth

### Get OAuth2 Link
#### GET /oauth2

Returns the oauth2 link used to login with

**API v2 analogue:** (no longer working) [Get OAuth2 Link](https://legacy.fateslist.xyz/docs/redoc#operation/get_oauth2_link)

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "done": true,
    "reason": null,
    "context": "https://discord.com/........."
}
```


### Create OAuth2 Login
#### POST /oauth2

Creates a oauth2 login given a code

**API v2 analogue:** (no longer working) [Login User](https://legacy.fateslist.xyz/api/docs/redoc#operation/login_user)

**Request Body**

```json
{
    "code": "code from discord oauth",
    "state": "Random UUID right now"
}
```

**Response Body**

```json
{
    "state": 0,
    "token": "",
    "user": {
        "id": "",
        "username": "",
        "disc": "",
        "avatar": "",
        "bot": false
    },
    "site_lang": "",
    "css": null
}
```


### Delete OAuth2 Login
#### DELETE /oauth2


'Deletes' (logs out) a oauth2 login. Always call this when logging out 
even if you do not use cookies as it may perform other logout tasks in future

This API is essentially a logout


**API v2 analogue:** (no longer working) [Logout Sunbeam](https://legacy.fateslist.xyz/docs/redoc#operation/logout_sunbeam)

**Request Body**

```json
{}
```

**Response Body**

```json
{
    "done": true,
    "reason": null,
    "context": null
}
```

