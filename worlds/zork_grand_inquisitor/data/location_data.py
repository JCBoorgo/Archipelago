from typing import Dict, NamedTuple, Optional, Tuple, Union

from ..enums import (
    ZorkGrandInquisitorEvents,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorLocations,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorTags,
)


class ZorkGrandInquisitorLocationData(NamedTuple):
    game_state_trigger: Optional[
        Tuple[
            Union[
                Tuple[str, str],
                Tuple[int, int],
                Tuple[int, Tuple[int, ...]],
                Tuple[Tuple[int, ...], int],
            ],
            ...,
        ]
    ]
    archipelago_id: Optional[int]
    region: ZorkGrandInquisitorRegions
    tags: Optional[Tuple[ZorkGrandInquisitorTags, ...]] = None
    requirements: Optional[
        Tuple[
            Union[
                Union[
                    ZorkGrandInquisitorItems,
                    ZorkGrandInquisitorEvents,
                ],
                Tuple[
                    Union[
                        ZorkGrandInquisitorItems,
                        ZorkGrandInquisitorEvents,
                    ],
                    ...,
                ],
            ],
            ...,
        ]
    ] = None
    event_item_name: Optional[str] = None


LOCATION_OFFSET = 9758067000

location_data: Dict[
    Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents], ZorkGrandInquisitorLocationData
] = {
    ZorkGrandInquisitorLocations.ALARM_SYSTEM_IS_DOWN: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tr2m"),),
        archipelago_id=LOCATION_OFFSET + 0,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.AN_EXCELLENT_POPPING_UTENSIL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2196, 84),),
        archipelago_id=LOCATION_OFFSET + 1,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            ZorkGrandInquisitorItems.GRIFFS_DRAGON_TOOTH,
        ),
    ),
    ZorkGrandInquisitorLocations.ARREST_THE_VANDAL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10789, 1),),
        archipelago_id=LOCATION_OFFSET + 2,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
            ZorkGrandInquisitorItems.CIGAR,
        ),
    ),
    ZorkGrandInquisitorLocations.ARTIFACTS_EXPLAINED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11787, 1), (11788, 1), (11789, 1)),
        archipelago_id=LOCATION_OFFSET + 3,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.A_BIG_FAT_SASSY_2_HEADED_MONSTER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((8929, 1),),
        archipelago_id=LOCATION_OFFSET + 4,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_OBIDIL,),
    ),
    ZorkGrandInquisitorLocations.A_LETTER_FROM_THE_WHITE_HOUSE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9124, 1),),
        archipelago_id=LOCATION_OFFSET + 5,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.WHITE_HOUSE_LETTER_MAILABLE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_666_MAILBOX,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.A_SMALLWAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11777, 1),),
        archipelago_id=LOCATION_OFFSET + 6,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            ZorkGrandInquisitorItems.SPELL_IGRAM,
        ),
    ),
    ZorkGrandInquisitorLocations.BEAUTIFUL_THATS_PLENTY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13278, 1),),
        archipelago_id=LOCATION_OFFSET + 7,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_MOSSY_GRATE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
            ZorkGrandInquisitorItems.SPELL_THROCK,
        ),
    ),
    ZorkGrandInquisitorLocations.BEBURTT_DEMYSTIFIED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16315, 1),),
        archipelago_id=LOCATION_OFFSET + 8,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE,
            ZorkGrandInquisitorItems.SPELL_KENDALL,
        ),
    ),
    ZorkGrandInquisitorLocations.BETTER_SPELL_MANUFACTURING_IN_UNDER_10_MINUTES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "th3x"),),
        archipelago_id=LOCATION_OFFSET + 9,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE,),
    ),
    ZorkGrandInquisitorLocations.BOING_BOING_BOING: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4220, 1),),
        archipelago_id=LOCATION_OFFSET + 10,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.HAMMER,
            ZorkGrandInquisitorItems.SNAPDRAGON,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.BONK: ZorkGrandInquisitorLocationData(
        game_state_trigger=((19491, 1),),
        archipelago_id=LOCATION_OFFSET + 11,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.HAMMER,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.BRAVE_SOULS_WANTED: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "us2g"),),
        archipelago_id=LOCATION_OFFSET + 12,
        region=ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.BROG_DO_GOOD: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2644, 1),),
        archipelago_id=LOCATION_OFFSET + 13,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.BROGS_GRUE_EGG,
            (
                ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.BROG_EAT_ROCKS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2629, 1),),
        archipelago_id=LOCATION_OFFSET + 14,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.BROG_KNOW_DUMB_THAT_DUMB: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2650, 1),),
        archipelago_id=LOCATION_OFFSET + 15,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.BROGS_GRUE_EGG,),
    ),
    ZorkGrandInquisitorLocations.BROG_MUCH_BETTER_AT_THIS_GAME: ZorkGrandInquisitorLocationData(
        game_state_trigger=((15715, 1),),
        archipelago_id=LOCATION_OFFSET + 16,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.BROGS_GRUE_EGG,
            (
                ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
            ZorkGrandInquisitorItems.BROGS_PLANK,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SKULL_CAGE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.CASTLE_WATCHING_A_FIELD_GUIDE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dv1t"),),
        archipelago_id=LOCATION_OFFSET + 17,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.CAVES_NOTES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "th3y"),),
        archipelago_id=LOCATION_OFFSET + 18,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE,),
    ),
    ZorkGrandInquisitorLocations.CLOSING_THE_TIME_TUNNELS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9543, 1),),
        archipelago_id=LOCATION_OFFSET + 19,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.COME_TO_PAPA_YOU_NUT: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "cd6k"), (1673, 1), (1660, 1), (1312, 1)),
        archipelago_id=LOCATION_OFFSET + 20,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.GRIFFS_AIR_PUMP,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_RAFT,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_SEA_CAPTAIN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO,
            ),
            ZorkGrandInquisitorItems.GRIFFS_DRAGON_TOOTH,
        ),
    ),
    ZorkGrandInquisitorLocations.CRISIS_AVERTED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11769, 1),),
        archipelago_id=LOCATION_OFFSET + 21,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.ZORK_ROCKS_ACTIVATED,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_DENTED_LOCKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.CUT_THAT_OUT_YOU_LITTLE_CREEP: ZorkGrandInquisitorLocationData(
        game_state_trigger=((19350, 1),),
        archipelago_id=LOCATION_OFFSET + 22,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.DENIED_BY_THE_LAKE_MONSTER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((17632, 1),),
        archipelago_id=LOCATION_OFFSET + 23,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_BLINDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
        ),
    ),
    ZorkGrandInquisitorLocations.DINGWHACKER_DELUXE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2417, 1),),
        archipelago_id=LOCATION_OFFSET + 24,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.DONT_EVEN_START_WITH_US_SPARKY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "hp5e"), (8919, 2), (9, 100)),
        archipelago_id=LOCATION_OFFSET + 25,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SWORD,),
    ),
    ZorkGrandInquisitorLocations.DONT_GO_SPENDING_IT_ALL_IN_ONE_PLACE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4512, 87),),
        archipelago_id=LOCATION_OFFSET + 26,
        region=ZorkGrandInquisitorRegions.ANYWHERE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
    ),
    ZorkGrandInquisitorLocations.DOOOOOOWN: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3619, 3600),),
        archipelago_id=LOCATION_OFFSET + 27,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DOWN: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3619, 5300),),
        archipelago_id=LOCATION_OFFSET + 28,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_LUCY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DRAGON_ARCHIPELAGO_TIME_TUNNEL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9216, 1),),
        archipelago_id=LOCATION_OFFSET + 29,
        region=ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_NARWILE,),
    ),
    ZorkGrandInquisitorLocations.DUNCE_LOCKER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11851, 1),),
        archipelago_id=LOCATION_OFFSET + 30,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.EGGPLANTS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3816, 11000),),
        archipelago_id=LOCATION_OFFSET + 31,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.ELSEWHERE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pc1e"),),
        archipelago_id=LOCATION_OFFSET + 32,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.EMERGENCY_MAGICATRONIC_MESSAGE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11784, 1),),
        archipelago_id=LOCATION_OFFSET + 33,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
    ),
    ZorkGrandInquisitorLocations.ENJOY_YOUR_TRIP: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13743, 1),),
        archipelago_id=LOCATION_OFFSET + 34,
        region=ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_KENDALL,),
    ),
    ZorkGrandInquisitorLocations.FAT_LOT_OF_GOOD_THATLL_DO_YA: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16368, 1),),
        archipelago_id=LOCATION_OFFSET + 35,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorItems.SPELL_IGRAM,),
    ),
    ZorkGrandInquisitorLocations.FIRE_FIRE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10277, (1, 2)),),
        archipelago_id=LOCATION_OFFSET + 36,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
            ZorkGrandInquisitorItems.CIGAR,
        ),
    ),
    ZorkGrandInquisitorLocations.FLOOD_CONTROL_DAM_3_THE_NOT_REMOTELY_BORING_TALE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13259, 1),),
        archipelago_id=LOCATION_OFFSET + 37,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.FLYING_SNAPDRAGON: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4222, 1),),
        archipelago_id=LOCATION_OFFSET + 38,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_THROCK,
            ZorkGrandInquisitorItems.SNAPDRAGON,
            ZorkGrandInquisitorItems.HAMMER,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.FROBUARY_3_UNDERGROUNDHOG_DAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dw2g"),),
        archipelago_id=LOCATION_OFFSET + 39,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.GETTING_SOME_CHANGE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12892, 1),),
        archipelago_id=LOCATION_OFFSET + 40,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.ZORKMID_BILL_ACCESSIBLE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CHANGE_MACHINE_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.GO_AWAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10654, 1),),
        archipelago_id=LOCATION_OFFSET + 41,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.GOOD_PUZZLE_SMART_BROG: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "sg6e"), (17103, 1), (15715, 1), (15707, 1)),
        archipelago_id=LOCATION_OFFSET + 42,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.BROGS_GRUE_EGG,
            (
                ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
            ZorkGrandInquisitorItems.BROGS_PLANK,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SKULL_CAGE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.GUE_TECH_ENTRANCE_EXAM: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11082, 1), (11307, 1), (11536, 1)),
        archipelago_id=LOCATION_OFFSET + 43,
        region=ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.HAVE_A_HELL_OF_A_DAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((8443, 1),),
        archipelago_id=LOCATION_OFFSET + 44,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.HELLO_THIS_IS_SHONA_FROM_GURTH_PUBLISHING: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4698, 1),),
        archipelago_id=LOCATION_OFFSET + 45,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10421, 1),),
        archipelago_id=LOCATION_OFFSET + 46,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
            ZorkGrandInquisitorItems.PLASTIC_SIX_PACK_HOLDER,
        ),
    ),
    ZorkGrandInquisitorLocations.HEY_FREE_DIRT: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11747, 1),),
        archipelago_id=LOCATION_OFFSET + 47,
        region=ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            ZorkGrandInquisitorItems.SHOVEL,
        ),
    ),
    ZorkGrandInquisitorLocations.HMMM_BIG_TOOTHPICK: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2194, 69),),
        archipelago_id=LOCATION_OFFSET + 48,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.BROGS_PLANK,),
    ),
    ZorkGrandInquisitorLocations.HMMM_INFORMATIVE_YET_DEEPLY_DISTURBING: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "mt2h"),),
        archipelago_id=LOCATION_OFFSET + 49,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.HOW_TO_HYPNOTIZE_YOURSELF: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "uh1e"),),
        archipelago_id=LOCATION_OFFSET + 50,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.HOW_TO_WIN_AT_DOUBLE_FANUCCI: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "th3s"),),
        archipelago_id=LOCATION_OFFSET + 51,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorEvents.DALBOZ_LOCKER_OPENABLE,),
    ),
    ZorkGrandInquisitorLocations.IMBUE_BEBURTT: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12166, 1),),
        archipelago_id=LOCATION_OFFSET + 52,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.IM_COMPLETELY_NUDE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((19344, 1),),
        archipelago_id=LOCATION_OFFSET + 53,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.INFLATUS_THE_ETERNAL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "cd4h"),),
        archipelago_id=LOCATION_OFFSET + 54,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.INTO_THE_FOLIAGE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13060, 1),),
        archipelago_id=LOCATION_OFFSET + 55,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.INVISIBLE_FLOWERS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12967, 1),),
        archipelago_id=LOCATION_OFFSET + 56,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_IGRAM,),
    ),
    ZorkGrandInquisitorLocations.IN_CASE_OF_ADVENTURE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12931, 1),),
        archipelago_id=LOCATION_OFFSET + 57,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.HAMMER,
            (
                ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.IN_MAGIC_WE_TRUST: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13062, 1),),
        archipelago_id=LOCATION_OFFSET + 58,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_REZROV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.ITS_ALMOST_AS_IF_IT_WERE_INFINITE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((11005, 15),),
        archipelago_id=LOCATION_OFFSET + 59,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
    ),
    ZorkGrandInquisitorLocations.ITS_ONE_OF_THOSE_ADVENTURERS_AGAIN: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pe3j"),),
        archipelago_id=LOCATION_OFFSET + 60,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.ITS_PLAYING_A_LITTLE_HARD_TO_GET: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3816, 1006),),
        archipelago_id=LOCATION_OFFSET + 61,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_OBIDIL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.IT_DOESNT_APPEAR_TO_BE_FOOLED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3816, 1009),),
        archipelago_id=LOCATION_OFFSET + 62,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_BEBURTT,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.I_AM_NOT_IMPRESSED: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "hp4f"), (8419, 1)),
        archipelago_id=LOCATION_OFFSET + 63,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_SNAVIG,),
    ),
    ZorkGrandInquisitorLocations.I_DONT_THINK_YOU_WOULDVE_WANTED_THAT_TO_WORK_ANYWAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3816, 1008),),
        archipelago_id=LOCATION_OFFSET + 64,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_THROCK,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.I_DONT_WANT_NO_TROUBLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10694, 1),),
        archipelago_id=LOCATION_OFFSET + 65,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.I_LIKE_YOUR_STYLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16374, 1),),
        archipelago_id=LOCATION_OFFSET + 66,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
            ZorkGrandInquisitorEvents.DAM_DESTROYED,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_CHASM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.I_SPIT_ON_YOUR_FILTHY_COINAGE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tp1e"), (9, 87), (1011, 1)),
        archipelago_id=LOCATION_OFFSET + 67,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
    ),
    ZorkGrandInquisitorLocations.LIT_SUNFLOWERS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4129, 1),),
        archipelago_id=LOCATION_OFFSET + 68,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_THROCK,),
    ),
    ZorkGrandInquisitorLocations.LOOK_AN_ICE_CREAM_BAR: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12517, 1),),
        archipelago_id=LOCATION_OFFSET + 69,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.MAILED_IT_TO_HELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2498, (1, 2)),),
        archipelago_id=LOCATION_OFFSET + 70,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (ZorkGrandInquisitorItems.TOTEM_GRIFF, ZorkGrandInquisitorItems.TOTEM_LUCY),
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.MAKE_LOVE_NOT_WAR: ZorkGrandInquisitorLocationData(
        game_state_trigger=(((8623, 8734), 21),),
        archipelago_id=LOCATION_OFFSET + 71,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.CHARON_CALLED,
            ZorkGrandInquisitorItems.SWORD,
        ),
    ),
    ZorkGrandInquisitorLocations.MEAD_LIGHT: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10485, 1),),
        archipelago_id=LOCATION_OFFSET + 72,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.MEAD_LIGHT,
            (
                ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.ME_I_AM_THE_BOSS_OF_YOU: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "px1k"),),
        archipelago_id=LOCATION_OFFSET + 73,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.MIKES_PANTS: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tr2p"),),
        archipelago_id=LOCATION_OFFSET + 74,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.MUSHROOM_HAMMERED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4217, 1),),
        archipelago_id=LOCATION_OFFSET + 75,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.HAMMER,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.NATIONAL_TREASURE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((14318, 1),),
        archipelago_id=LOCATION_OFFSET + 76,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_REZROV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.NATURAL_AND_SUPERNATURAL_CREATURES_OF_QUENDOR: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dv1p"),),
        archipelago_id=LOCATION_OFFSET + 77,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.NOOOOOOOOOOOOO: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12706, 1),),
        archipelago_id=LOCATION_OFFSET + 78,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.NOTHIN_LIKE_A_GOOD_STOGIE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4237, 1),),
        archipelago_id=LOCATION_OFFSET + 79,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.CIGAR,
        ),
    ),
    ZorkGrandInquisitorLocations.NOW_YOU_LOOK_LIKE_US_WHICH_IS_AN_IMPROVEMENT: ZorkGrandInquisitorLocationData(
        game_state_trigger=((8935, 1),),
        archipelago_id=LOCATION_OFFSET + 80,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_SNAVIG,),
    ),
    ZorkGrandInquisitorLocations.NO_AUTOGRAPHS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10476, 1),),
        archipelago_id=LOCATION_OFFSET + 81,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.NO_BONDAGE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pe2e"), (10262, 2), (15150, 83)),
        archipelago_id=LOCATION_OFFSET + 82,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorEvents.ROPE_GLORFABLE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.NO_ONE_RETURNS_FROM_HADES: ZorkGrandInquisitorLocationData(
        game_state_trigger=((15204, 1),),
        archipelago_id=LOCATION_OFFSET + 83,
        region=ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.OBIDIL_DRIED_UP: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12164, 1),),
        archipelago_id=LOCATION_OFFSET + 84,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
            ZorkGrandInquisitorItems.SANDWITCH_WRAPPER,
        ),
    ),
    ZorkGrandInquisitorLocations.OH_DEAR_GOD_ITS_A_DRAGON: ZorkGrandInquisitorLocationData(
        game_state_trigger=((1300, 1),),
        archipelago_id=LOCATION_OFFSET + 85,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.GRIFFS_AIR_PUMP,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_RAFT,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_SEA_CAPTAIN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.OH_VERY_FUNNY_GUYS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2448, 1),),
        archipelago_id=LOCATION_OFFSET + 86,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_BROG,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.OH_WOW_TALK_ABOUT_DEJA_VU: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4869, 1),),
        archipelago_id=LOCATION_OFFSET + 87,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.COCOA_INGREDIENTS,
            ZorkGrandInquisitorItems.HUNGUS_LARD,
        ),
    ),
    ZorkGrandInquisitorLocations.OLD_SCRATCH_WINNER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4512, 32),),
        archipelago_id=LOCATION_OFFSET + 88,
        region=ZorkGrandInquisitorRegions.ANYWHERE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,),
    ),
    ZorkGrandInquisitorLocations.ONLY_YOU_CAN_PREVENT_FOOZLE_FIRES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pe5n"),),
        archipelago_id=LOCATION_OFFSET + 89,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.OPEN_THE_GATES_OF_HELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((8730, 1),),
        archipelago_id=LOCATION_OFFSET + 90,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_SNAVIG,
            ZorkGrandInquisitorItems.TOTEM_BROG,  # Visually hiding this totem is tied to owning it; no choice
        ),
    ),
    ZorkGrandInquisitorLocations.OUTSMART_THE_QUELBEES: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4241, 1),),
        archipelago_id=LOCATION_OFFSET + 91,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.HUNGUS_LARD,
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.PERMASEAL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "mt1g"),),
        archipelago_id=LOCATION_OFFSET + 92,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.PLANETFALL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pp1j"),),
        archipelago_id=LOCATION_OFFSET + 93,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.PLEASE_DONT_THROCK_THE_GRASS: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "te1g"),),
        archipelago_id=LOCATION_OFFSET + 94,
        region=ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.PORT_FOOZLE_TIME_TUNNEL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9404, 1),),
        archipelago_id=LOCATION_OFFSET + 95,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
        ),
    ),
    ZorkGrandInquisitorLocations.PROZORKED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4115, 1),),
        archipelago_id=LOCATION_OFFSET + 96,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.PROZORK_TABLET,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.PURPLE_BEAST_ALARM_SYSTEM: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tp1f"),),
        archipelago_id=LOCATION_OFFSET + 97,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.REASSEMBLE_SNAVIG: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4512, 98),),
        archipelago_id=LOCATION_OFFSET + 98,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_ANS,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_GIV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.RESTOCKED_ON_GRUESDAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tr2h"),),
        archipelago_id=LOCATION_OFFSET + 99,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.RIGHT_HELLO_YES_UH_THIS_IS_SNEFFLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4698, 3),),
        archipelago_id=LOCATION_OFFSET + 100,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.RIGHT_UH_SORRY_ITS_ME_AGAIN_SNEFFLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4698, 4),),
        archipelago_id=LOCATION_OFFSET + 101,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.SNAVIG_REPAIRED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12161, 1),),
        archipelago_id=LOCATION_OFFSET + 102,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.HAS_REPAIRABLE_SNAVIG,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.SOUVENIR: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13408, 1),),
        archipelago_id=LOCATION_OFFSET + 103,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.SPELL_CHECK_COMPLETE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12168, 1),),
        archipelago_id=LOCATION_OFFSET + 104,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        )
    ),
    ZorkGrandInquisitorLocations.STRAIGHT_TO_HELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9719, 1),),
        archipelago_id=LOCATION_OFFSET + 105,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.STRIP_GRUE_FIRE_WATER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((14511, 1), (14524, 5)),
        archipelago_id=LOCATION_OFFSET + 106,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_1,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_2,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_3,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_4,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.SUCKING_ROCKS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12859, 1),),
        archipelago_id=LOCATION_OFFSET + 107,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            ZorkGrandInquisitorItems.PERMA_SUCK_MACHINE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_VACUUM_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.TALK_TO_ME_GRAND_INQUISITOR: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10299, 1),),
        archipelago_id=LOCATION_OFFSET + 108,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.TAMING_YOUR_SNAPDRAGON: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dv1h"),),
        archipelago_id=LOCATION_OFFSET + 109,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.THAR_SHE_BLOWS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((1311, 1), (1312, 1)),
        archipelago_id=LOCATION_OFFSET + 110,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.GRIFFS_AIR_PUMP,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_RAFT,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_SEA_CAPTAIN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO,
            ),
            ZorkGrandInquisitorItems.GRIFFS_DRAGON_TOOTH,
        ),
    ),
    ZorkGrandInquisitorLocations.THATS_A_ROPE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10486, 1),),
        archipelago_id=LOCATION_OFFSET + 111,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorEvents.ROPE_GLORFABLE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.THATS_IT_JUST_KEEP_HITTING_THOSE_BUTTONS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13805, 1),),
        archipelago_id=LOCATION_OFFSET + 112,
        region=ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
    ),
    ZorkGrandInquisitorLocations.THATS_STILL_A_ROPE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tp1e"), (9, 83), (1011, 1)),
        archipelago_id=LOCATION_OFFSET + 113,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorEvents.ROPE_GLORFABLE,),
    ),
    ZorkGrandInquisitorLocations.THATS_THE_SPIRIT: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10341, 95),),
        archipelago_id=LOCATION_OFFSET + 114,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.THE_ALCHEMICAL_DEBACLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9459, 1),),
        archipelago_id=LOCATION_OFFSET + 115,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.THE_ENDLESS_FIRE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9473, 1),),
        archipelago_id=LOCATION_OFFSET + 116,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.THE_FLATHEADIAN_FUDGE_FIASCO: ZorkGrandInquisitorLocationData(
        game_state_trigger=((9520, 1),),
        archipelago_id=LOCATION_OFFSET + 117,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.THE_ONLY_WAY_TO_WIN_IS_NOT_TO_PLAY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16286, 1),),
        archipelago_id=LOCATION_OFFSET + 118,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.DALBOZ_LOCKER_OPENABLE,
            ZorkGrandInquisitorItems.SPELL_KENDALL,
        ),
    ),
    ZorkGrandInquisitorLocations.THE_PERILS_OF_MAGIC: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "me1j"),),
        archipelago_id=LOCATION_OFFSET + 119,
        region=ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.THE_UNDERGROUND_UNDERGROUND: ZorkGrandInquisitorLocationData(
        game_state_trigger=((13167, 1),),
        archipelago_id=LOCATION_OFFSET + 120,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SUBWAY_TOKEN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.THIS_DOESNT_LOOK_ANYTHING_LIKE_THE_BROCHURE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "cd60"), (1524, 1)),
        archipelago_id=LOCATION_OFFSET + 121,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.TOTEM_LUCY,),
    ),
    ZorkGrandInquisitorLocations.THROCKED_MUSHROOM_HAMMERED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4219, 1),),
        archipelago_id=LOCATION_OFFSET + 122,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.HAMMER,
            ZorkGrandInquisitorItems.SPELL_THROCK,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.TIME_TRAVEL_FOR_DUMMIES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "th3z"),),
        archipelago_id=LOCATION_OFFSET + 123,
        region=ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE,),
    ),
    ZorkGrandInquisitorLocations.TOTEMIZED_DAILY_BILLBOARD: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "px1h"),),
        archipelago_id=LOCATION_OFFSET + 124,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.UH_OH_BROG_CANT_SWIM: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "cd60"), (1520, 1)),
        archipelago_id=LOCATION_OFFSET + 125,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.TOTEM_BROG,),
    ),
    ZorkGrandInquisitorLocations.UM_AH_UM_AH_UM_AH: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16997, 4),),
        archipelago_id=LOCATION_OFFSET + 126,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.UMBRELLA_FLOWERS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12926, 1),),
        archipelago_id=LOCATION_OFFSET + 127,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_BEBURTT,),
    ),
    ZorkGrandInquisitorLocations.UP: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3619, 5200),),
        archipelago_id=LOCATION_OFFSET + 128,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_LUCY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.USELESS_BUT_FUN: ZorkGrandInquisitorLocationData(
        game_state_trigger=((14321, 1),),
        archipelago_id=LOCATION_OFFSET + 129,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.SPELL_GOLGATEM,),
    ),
    ZorkGrandInquisitorLocations.UUUUUP: ZorkGrandInquisitorLocationData(
        game_state_trigger=((3619, 3500),),
        archipelago_id=LOCATION_OFFSET + 130,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.VOYAGE_OF_CAPTAIN_ZAHAB: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "uh1h"),),
        archipelago_id=LOCATION_OFFSET + 131,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.WANT_SOME_RYE_COURSE_YA_DO: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4034, 1),),
        archipelago_id=LOCATION_OFFSET + 132,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR,
            ZorkGrandInquisitorItems.MEAD_LIGHT,
            ZorkGrandInquisitorItems.ZIMDOR_SCROLL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.WANT_SOME_RYE_COURSE_YA_DO_PAST: ZorkGrandInquisitorLocationData(
        game_state_trigger=((17006, 5001),),
        archipelago_id=LOCATION_OFFSET + 133,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.WE_DONT_SERVE_YOUR_KIND_HERE: ZorkGrandInquisitorLocationData(
        game_state_trigger=((2461, 1),),
        archipelago_id=LOCATION_OFFSET + 134,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.WE_GOT_A_HIGH_ROLLER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((15472, 1),),
        archipelago_id=LOCATION_OFFSET + 135,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_1,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_2,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_3,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_4,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.WHAT_ARE_YOU_STUPID: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10484, 1),),
        archipelago_id=LOCATION_OFFSET + 136,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.PLASTIC_SIX_PACK_HOLDER,
            (
                ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.WHITE_HOUSE_TIME_TUNNEL: ZorkGrandInquisitorLocationData(
        game_state_trigger=((4983, 1),),
        archipelago_id=LOCATION_OFFSET + 137,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.SPELL_NARWILE,
        ),
    ),
    ZorkGrandInquisitorLocations.WHOOPS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((15959, (1, 2)),),
        archipelago_id=LOCATION_OFFSET + 138,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(ZorkGrandInquisitorItems.BROGS_GRUE_EGG,)
    ),
    ZorkGrandInquisitorLocations.WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dc10"), (1596, 1)),
        archipelago_id=LOCATION_OFFSET + 139,
        region=ZorkGrandInquisitorRegions.WALKING_CASTLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.YAD_GOHDNUORGREDNU_3_YRAUBORF: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dm2g"),),
        archipelago_id=LOCATION_OFFSET + 140,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.YOUR_PUNY_WEAPONS_DONT_PHASE_ME_BABY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dg4e"), (4266, 1), (9, 21), (4035, 1)),
        archipelago_id=LOCATION_OFFSET + 141,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_HARRY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.YOU_DONT_GO_MESSING_WITH_A_MANS_ZIPPER: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16405, 1),),
        archipelago_id=LOCATION_OFFSET + 142,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorItems.SPELL_REZROV,),
    ),
    ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS: ZorkGrandInquisitorLocationData(
        game_state_trigger=((16342, 1),),
        archipelago_id=LOCATION_OFFSET + 143,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.YOU_LOSE_MUFFET_ANTE_UP: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "qs1e"), (14511, 1), (14524, 5)),
        archipelago_id=LOCATION_OFFSET + 144,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.CORE,),
        requirements=(
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_1,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_2,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_3,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_4,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.YOU_ONE_OF_THEM_AGITATORS_AINT_YA: ZorkGrandInquisitorLocationData(
        game_state_trigger=((10586, 1),),
        archipelago_id=LOCATION_OFFSET + 145,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE,),
    ),
    ZorkGrandInquisitorLocations.YOU_WANT_A_PIECE_OF_ME_DOCK_BOY: ZorkGrandInquisitorLocationData(
        game_state_trigger=((15151, 1),),
        archipelago_id=LOCATION_OFFSET + 146,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.ZIMDOR_IS_UNDAMAGED: ZorkGrandInquisitorLocationData(
        game_state_trigger=((12167, 1),),
        archipelago_id=LOCATION_OFFSET + 147,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.CORE, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.ZIMDOR_SCROLL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        )
    ),
    # Deathsanity
    ZorkGrandInquisitorLocations.DEATH_ARRESTED_WITH_JACK: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 1)),
        archipelago_id=LOCATION_OFFSET + 200 + 0,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
            ZorkGrandInquisitorItems.CIGAR,
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_ATTACKED_THE_QUELBEES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 20)),
        archipelago_id=LOCATION_OFFSET + 200 + 1,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_CLIMBED_OUT_OF_THE_WELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 21)),
        archipelago_id=LOCATION_OFFSET + 200 + 2,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(ZorkGrandInquisitorItems.WELL_ROPE,),
    ),
    ZorkGrandInquisitorLocations.DEATH_EATEN_BY_A_GRUE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 18)),
        archipelago_id=LOCATION_OFFSET + 200 + 3,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            (
                ZorkGrandInquisitorItems.TOTEM_GRIFF,
                ZorkGrandInquisitorItems.TOTEM_LUCY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_JUMPED_IN_BOTTOMLESS_PIT: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 3)),
        archipelago_id=LOCATION_OFFSET + 200 + 4,
        region=ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
    ),
    ZorkGrandInquisitorLocations.DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 37)),
        archipelago_id=LOCATION_OFFSET + 200 + 5,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_1,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_2,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_3,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_4,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_LOST_SOUL_TO_OLD_SCRATCH: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 23)),
        archipelago_id=LOCATION_OFFSET + 200 + 6,
        region=ZorkGrandInquisitorRegions.ANYWHERE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,),
    ),
    ZorkGrandInquisitorLocations.DEATH_OUTSMARTED_BY_THE_QUELBEES: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 29)),
        archipelago_id=LOCATION_OFFSET + 200 + 7,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.HUNGUS_LARD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 30)),
        archipelago_id=LOCATION_OFFSET + 200 + 8,
        region=ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
    ),
    ZorkGrandInquisitorLocations.DEATH_STEPPED_INTO_THE_INFINITE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 4)),
        archipelago_id=LOCATION_OFFSET + 200 + 9,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_SWALLOWED_BY_A_DRAGON: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 11)),
        archipelago_id=LOCATION_OFFSET + 200 + 10,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(
            ZorkGrandInquisitorItems.GRIFFS_AIR_PUMP,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_RAFT,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_SEA_CAPTAIN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO,
            ),
            ZorkGrandInquisitorItems.GRIFFS_DRAGON_TOOTH,
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_THROCKED_THE_GRASS: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 34)),
        archipelago_id=LOCATION_OFFSET + 200 + 11,
        region=ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.SPELL_THROCK,
            (
                ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_GRASS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_INFINITY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 9)),
        archipelago_id=LOCATION_OFFSET + 200 + 12,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_INFINITY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_NEWARK_NEW_JERSEY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 33)),
        archipelago_id=LOCATION_OFFSET + 200 + 13,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_NEWARK_NEW_JERSEY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_PERMANENTLY_HALLS_OF_INQUISITION: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 8)),
        archipelago_id=LOCATION_OFFSET + 200 + 14,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_HALL_OF_INQUISITION,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_PERMANENTLY_INFINITY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 7)),
        archipelago_id=LOCATION_OFFSET + 200 + 15,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_INFINITY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_PERMANENTLY_NEWARK_NEW_JERSEY: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 6)),
        archipelago_id=LOCATION_OFFSET + 200 + 16,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_NEWARK_NEW_JERSEY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_PERMANENTLY_STRAIGHT_TO_HELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 5)),
        archipelago_id=LOCATION_OFFSET + 200 + 17,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_PERMANENTLY_SURFACE_OF_MERZ: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 13)),
        archipelago_id=LOCATION_OFFSET + 200 + 18,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_SURFACE_OF_MERZ,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_TOTEMIZED_SURFACE_OF_MERZ: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 32)),
        archipelago_id=LOCATION_OFFSET + 200 + 19,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY,),
        requirements=(
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_SURFACE_OF_MERZ,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.DEATH_YOURE_NOT_CHARON: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 10)),
        archipelago_id=LOCATION_OFFSET + 200 + 20,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorItems.SPELL_SNAVIG,),
    ),
    ZorkGrandInquisitorLocations.DEATH_ZORK_ROCKS_EXPLODED: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "gjde"), (2201, 19)),
        archipelago_id=LOCATION_OFFSET + 200 + 21,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.DEATHSANITY, ZorkGrandInquisitorTags.MISSABLE),
        requirements=(ZorkGrandInquisitorEvents.ZORK_ROCKS_ACTIVATED,),
    ),
    # Landmarksanity
    ZorkGrandInquisitorLocations.LANDMARK_DRAGON_ARCHIPELAGO: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "cd60"),),
        archipelago_id=LOCATION_OFFSET + 300 + 0,
        region=ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
        requirements=(
            (
                ZorkGrandInquisitorItems.TOTEM_BROG,
                ZorkGrandInquisitorItems.TOTEM_GRIFF,
                ZorkGrandInquisitorItems.TOTEM_LUCY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_DUNGEON_MASTERS_HOUSE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dg40"),),
        archipelago_id=LOCATION_OFFSET + 300 + 1,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_FLOOD_CONTROL_DAM_3: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "ue1e"),),
        archipelago_id=LOCATION_OFFSET + 300 + 2,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_GATES_OF_HELL: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "hp50"),),
        archipelago_id=LOCATION_OFFSET + 300 + 3,
        region=ZorkGrandInquisitorRegions.HADES,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_GREAT_UNDERGROUND_EMPIRE_ENTRANCE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "uw10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 4,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_GUE_TECH_FOUNTAIN_INSIDE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tr10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 5,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_GUE_TECH_FOUNTAIN_OUTSIDE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "te50"),),
        archipelago_id=LOCATION_OFFSET + 300 + 6,
        region=ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_HADES_SHORE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "hp10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 7,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_INFINITE_CORRIDOR: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "th10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 8,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_INQUISITION_HEADQUARTERS: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "px10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 9,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_JACKS_SHOP: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pp10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 10,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_MIRROR_ROOM: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dm10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 11,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_PAST_PORT_FOOZLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "qe10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 12,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
        requirements=(
            (
                ZorkGrandInquisitorItems.TOTEM_BROG,
                ZorkGrandInquisitorItems.TOTEM_GRIFF,
                ZorkGrandInquisitorItems.TOTEM_LUCY,
            ),
        ),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_PORT_FOOZLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "pe10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 13,
        region=ZorkGrandInquisitorRegions.PORT_FOOZLE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_SPELL_CHECKER: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "tp40"),),
        archipelago_id=LOCATION_OFFSET + 300 + 14,
        region=ZorkGrandInquisitorRegions.SPELL_LAB,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_TOTEMIZER: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "mt10"),),
        archipelago_id=LOCATION_OFFSET + 300 + 15,
        region=ZorkGrandInquisitorRegions.MONASTERY,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_UMBRELLA_TREE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "uc1e"),),
        archipelago_id=LOCATION_OFFSET + 300 + 16,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_UNDERGROUND_UNDERGROUND_ENTRANCE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "uc60"),),
        archipelago_id=LOCATION_OFFSET + 300 + 17,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_WALKING_CASTLES_HEART: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "dc1h"), (1596, 1)),
        archipelago_id=LOCATION_OFFSET + 300 + 18,
        region=ZorkGrandInquisitorRegions.WALKING_CASTLE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
    ),
    ZorkGrandInquisitorLocations.LANDMARK_WHITE_HOUSE: ZorkGrandInquisitorLocationData(
        game_state_trigger=(("location", "sw40"),),
        archipelago_id=LOCATION_OFFSET + 300 + 19,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        tags=(ZorkGrandInquisitorTags.LANDMARKSANITY,),
        requirements=(
            (
                ZorkGrandInquisitorItems.TOTEM_BROG,
                ZorkGrandInquisitorItems.TOTEM_GRIFF,
                ZorkGrandInquisitorItems.TOTEM_LUCY,
            ),
        ),
    ),
    # Events
    ZorkGrandInquisitorEvents.CHARON_CALLED: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.HADES_SHORE,
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.CHARON_CALLED.value,
    ),
    ZorkGrandInquisitorEvents.DALBOZ_LOCKER_OPENABLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.DALBOZ_LOCKER_OPENABLE.value,
    ),
    ZorkGrandInquisitorEvents.DAM_DESTROYED: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        requirements=(
            ZorkGrandInquisitorItems.SPELL_REZROV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.DAM_DESTROYED.value,
    ),
    ZorkGrandInquisitorEvents.DOOR_DRANK_MEAD: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        requirements=(
            ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR,
            ZorkGrandInquisitorItems.MEAD_LIGHT,
            ZorkGrandInquisitorItems.ZIMDOR_SCROLL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.DOOR_DRANK_MEAD.value,
    ),
    ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.DM_LAIR,
        requirements=(
            (
                ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.CIGAR,
        ),
        event_item_name=ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR.value,
    ),
    ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.DUNCE_LOCKER_OPENABLE.value,
    ),
    ZorkGrandInquisitorEvents.HAS_REPAIRABLE_OBIDIL: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.HAS_REPAIRABLE_OBIDIL.value,
    ),
    ZorkGrandInquisitorEvents.HAS_REPAIRABLE_SNAVIG: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        requirements=(
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_ANS,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_GIV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.HAS_REPAIRABLE_SNAVIG.value,
    ),
    ZorkGrandInquisitorEvents.ROPE_GLORFABLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.CROSSROADS,
        requirements=(
            ZorkGrandInquisitorItems.WELL_ROPE,
            ZorkGrandInquisitorItems.SPELL_GLORF,
        ),
        event_item_name=ZorkGrandInquisitorEvents.ROPE_GLORFABLE.value,
    ),
    ZorkGrandInquisitorEvents.VICTORY: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.ENDGAME,
        event_item_name=ZorkGrandInquisitorEvents.VICTORY.value,
    ),
    ZorkGrandInquisitorEvents.WHITE_HOUSE_LETTER_MAILABLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.WHITE_HOUSE,
        requirements=(
            (ZorkGrandInquisitorItems.TOTEM_GRIFF, ZorkGrandInquisitorItems.TOTEM_LUCY),
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.WHITE_HOUSE_LETTER_MAILABLE.value,
    ),
    ZorkGrandInquisitorEvents.ZORKMID_BILL_ACCESSIBLE: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.ANYWHERE,
        requirements=(ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,),
        event_item_name=ZorkGrandInquisitorEvents.ZORKMID_BILL_ACCESSIBLE.value,
    ),
    ZorkGrandInquisitorEvents.ZORK_ROCKS_ACTIVATED: ZorkGrandInquisitorLocationData(
        game_state_trigger=None,
        archipelago_id=None,
        region=ZorkGrandInquisitorRegions.GUE_TECH,
        requirements=(
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
            ZorkGrandInquisitorItems.ZORK_ROCKS,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
        event_item_name=ZorkGrandInquisitorEvents.ZORK_ROCKS_ACTIVATED.value,
    ),
}
