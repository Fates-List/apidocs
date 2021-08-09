# Enum Reference

Below is a reference of all the enums used in Fates List, It is automatically generated

## APIEventTypes

| Name | Value | Description |
| :--- | :--- | :--- |
| ws_invalid | 0 | Websocket Invalid Response |
| ws_no_auth | 1 | Websocket No Authentication |
| ws_ready | 3 | Websocket Ready |
| ws_event_single | 4 | Single Websocket Event |
| ws_event_multi | 5 | Mutliple Websocket Events |
| auth_token | 20 | Token Auth |
| auth_manager_key | 21 | Manager Auth |
| vote_webhook | 40 | Vote Webhook Event |

## APIEvents

May or may not be in numeric order

| Name | Value | Description |
| :--- | :--- | :--- |
| bot_vote | 0 | Vote Bot Event |
| bot_add | 1 | Bot Add Event |
| bot_edit | 2 | Bot Edit Event |
| bot_delete | 3 | Bot Delete Event |
| bot_claim | 4 | Bot Claim Event |
| bot_approve | 5 | Bot Approve Event |
| bot_deny | 6 | Bot Deny Event |
| bot_ban | 7 | Bot Ban Event |
| bot_unban | 8 | Bot Unban Event |
| bot_requeue | 9 | Bot Requeue Event |
| bot_certify | 10 | Bot Certify Event |
| bot_uncertify | 11 | Bot Uncertify Event |
| bot_transfer | 12 | Bot Ownership Transfer Event |
| bot_hide | 13 | Bot Hide Event |
| bot_archive | 14 | Bot Archive Event |
| bot_unverify | 15 | Bot Unverify Event |
| bot_view | 16 | Bot View Event (Websocket only) |
| bot_invite | 17 | Bot Invite Event (Websocket only) |
| bot_unclaim | 18 | Bot Unclaim Event |
| bot_root_update | 19 | Bot Root State Update Event |
| bot_vote_reset | 20 | Bot Votes Reset Event |
| bot_vote_reset_all | 21 | Bot Votes Reset All Event |
| bot_lock | 22 | Bot Lock Event |
| bot_unlock | 23 | Bot Unlock Event |
| review_vote | 30 | Review Vote Event |
| review_add | 31 | Bot Review Add Event |
| review_edit | 32 | Bot Review Edit Event |
| review_delete | 33 | Bot Review Delete Event |
| command_vote | 50 | Bot Command Vote Event |
| command_add | 51 | Bot Command Add Event |
| command_edit | 52 | Bot Command Edit Event |
| command_delete | 53 | Bot Command Delete Event |
| server_vote | 70 | Server Vote Event |
| server_add | 71 | Server Add Event |
| server_edit | 72 | Server Edit Event |
| server_delete | 73 | Server Delete Event |
| server_ban | 74 | Server Ban Event |
| server_hide | 75 | Server Hide Event |
| server_archive | 76 | Server Archive Event |
| ws_identity | 90 | Websocket Identity Event |
| ws_identity_res | 91 | Websocket Identity Response Event |
| ws_kill | 92 | Websocket Kill Event |
| ws_status | 93 | Websocket Status Event |
| ws_event | 94 | Websocket Event |
| vote_reminder | 110 | Vote Reminder |

## BotAdminOp

Handles bot admin operations

| Name | Value | Description |
| :--- | :--- | :--- |
| requeue | 0 | Requeue Bot |
| claim | 1 | Claim Bot |
| unclaim | 2 | Unclaim Bot |
| ban | 3 | Ban Bot |
| unban | 4 | Unban Bot |
| certify | 5 | Certify Bot |
| uncertify | 6 | Uncertify Bot |
| approve | 7 | Approve Bot |
| deny | 8 | Deny Bot |
| unverify | 9 | Unverify Bot |
| transfer | 10 | Transfer Bot Ownership |
| root_update | 11 | Root State Update |
| reset_votes | 12 | Reset All Votes |
| dummy_recursive | 13 | Dummy Resursive |
| dummy_nrecursive | 14 | Dummy Nonrecursive |
| staff_lock | 15 | Staff Lock Bot |
| staff_unlock | 16 | Staff Unlock Bot |
| bot_lock | 17 | Bot Lock |
| bot_unlock | 18 | Bot Unlock |
| bot_delete | 19 | Bot Delete |

## BotLock

| Name | Value | Description |
| :--- | :--- | :--- |
| unlocked | 0 | Bot unlocked for editing |
| locked | 1 | Bot locked for editing |
| locked_staff | 2 | Bot locked by staff |
| locked_staff_spam | 3 | Bot locked by staff due to spamming edits |

## BotRequeue

| Name | Value | Description |
| :--- | :--- | :--- |
| claim | 0 | Claim Bot |
| requeue | 1 | Requeue Bot |
| unclaim | 2 | Unclaim Bot |

## BotState

| Name | Value | Description |
| :--- | :--- | :--- |
| approved | 0 | Verified |
| pending | 1 | Pending Verification |
| denied | 2 | Denied |
| hidden | 3 | Hidden |
| banned | 4 | Banned |
| under_review | 5 | Under Review |
| certified | 6 | Certified |
| archived | 7 | Archived |

## CommandType


    0 - Regular (Prefix) Command

    1 - Slash Command (Guild)
    
    2 - Slash Command (Global)
    

| Name | Value | Description |
| :--- | :--- | :--- |
| regular | 0 | Regular Command |
| guild_slash | 1 | Slash Command (guild) |
| global_slash | 2 | Slash Command (global) |

## CooldownBucket

| Name | Value | Description |
| :--- | :--- | :--- |
| requeue | 12.0 | An enumeration. |
| ban | 18.0 | An enumeration. |
| transfer | 30.0 | An enumeration. |
| reset | 60 | An enumeration. |
| lock | 120 | An enumeration. |
| delete | 210.0 | An enumeration. |

## LongDescType

| Name | Value | Description |
| :--- | :--- | :--- |
| html | 0 | HTML/Raw Description |
| markdown_pymarkdown | 1 | Markdown using Python Markdown |
| markdown_marked | 2 | Markdown using JavaScript Marked |

## PartnerAdType

| Name | Value | Description |
| :--- | :--- | :--- |
| server | server | Server Ad |
| site | site | Site Ad |

## PartnerType

| Name | Value | Description |
| :--- | :--- | :--- |
| bot | 0 | Bot |
| guild | 1 | Guild |

## PromotionType

| Name | Value | Description |
| :--- | :--- | :--- |
| announcement | 0 | Announcement |
| promotion | 1 | Promotion |
| generic | 2 | Generic |

## Status

Status object (See https://docs.fateslist.xyz/basics/basic-structures#status for more information)

| Name | Value | Description |
| :--- | :--- | :--- |
| unknown | 0 | Unknown |
| online | 1 | Online |
| offline | 2 | Offline |
| idle | 3 | Idle |
| dnd | 4 | Do Not Disturb |

## ULAFeature

| Name | Value | Description |
| :--- | :--- | :--- |
| get_bot | 1 | Get Bot |
| post_stats | 2 | Post Stats |
| get_user_voted | 3 | Get User Voted |

## ULAMethod

| Name | Value | Description |
| :--- | :--- | :--- |
| get | 0 | GET method |
| post | 1 | POST method |
| put | 2 | PUT method |
| patch | 3 | PATCH method |
| delete | 4 | DELETE method |

## ULAState

| Name | Value | Description |
| :--- | :--- | :--- |
| pending | 0 | Pending Verification |
| approved | 1 | Approved |

## UserState

| Name | Value | Description |
| :--- | :--- | :--- |
| normal | 0 | Normal (No Ban) |
| global_ban | 1 | Global Ban |
| pedit_ban | 2 | Profile Edit Ban |
| ddr_ban | 3 | Data Deletion Request Ban |

## Vanity

| Name | Value | Description |
| :--- | :--- | :--- |
| server | 0 | Server |
| bot | 1 | Bot |
| profile | 2 | Profile |

## WebSocketCommand

| Name | Value | Description |
| :--- | :--- | :--- |
| dispatch_old | 0 | Dispatch Old Events |

## WebhookResolver

| Name | Value | Description |
| :--- | :--- | :--- |
| not_ack | 0 | Not Acknowledged |
| error | 1 | Post Error |
| posted | 2 | Posted |

## WebhookType

| Name | Value | Description |
| :--- | :--- | :--- |
| vote | 0 | Vote Webhook |
| discord | 1 | Discord Integration |
| fc | 2 | Fates Client |

## WidgetFormat

| Name | Value | Description |
| :--- | :--- | :--- |
| json | json | JSON Widget |
| html | html | HTML Widget |
| png | png | Widget (as png image) |
| webp | webp | Widget (as webp image) |