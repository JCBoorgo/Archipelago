import enum


class ZorkGrandInquisitorCraftableSpellBehaviors(enum.Enum):
    VANILLA = 0
    ANY_SPELL = 1
    ANYTHING = 2


class ZorkGrandInquisitorDeathsanity(enum.Enum):
    OFF = 0
    ON = 1


class ZorkGrandInquisitorEvents(enum.Enum):
    CHARON_CALLED = "Event: Charon Called"
    DALBOZ_LOCKER_OPENABLE = "Event: Dalboz Locker Openable"
    DAM_DESTROYED = "Event: Dam Destroyed"
    DOOR_DRANK_MEAD = "Event: Door Drank Mead"
    DOOR_SMOKED_CIGAR = "Event: Door Smoked Cigar"
    DUNCE_LOCKER_OPENABLE = "Event: Dunce Locker Openable"
    HAS_REPAIRABLE_OBIDIL = "Event: Has Repairable OBIDIL"
    HAS_REPAIRABLE_SNAVIG = "Event: Has Repairable SNAVIG"
    ROPE_GLORFABLE = "Event: Rope GLORFable"
    VICTORY = "Victory"
    WHITE_HOUSE_LETTER_MAILABLE = "Event: White House Letter Mailable"
    ZORKMID_BILL_ACCESSIBLE = "Event: 500 Zorkmid Bill Accessible"
    ZORK_ROCKS_ACTIVATED = "Event: Zork Rocks Activated"


class ZorkGrandInquisitorGoals(enum.Enum):
    THREE_ARTIFACTS = 0
    ARTIFACT_OF_MAGIC_HUNT = 1
    SPELL_HEIST = 2
    ZORK_TOUR = 3
    GRIM_JOURNEY = 4


class ZorkGrandInquisitorHotspots(enum.Enum):
    ENABLED = 0
    REQUIRE_ITEM_PER_REGION = 1
    REQUIRE_ITEM_PER_HOTSPOT = 2


class ZorkGrandInquisitorItems(enum.Enum):
    ARTIFACT_OF_MAGIC = "Artifact of Magic"
    BROGS_BICKERING_TORCH = "Brog's Bickering Torch"
    BROGS_FLICKERING_TORCH = "Brog's Flickering Torch"
    BROGS_GRUE_EGG = "Brog's Grue Egg"
    BROGS_PLANK = "Brog's Plank"
    CIGAR = "Cigar"
    COCOA_INGREDIENTS = "Cocoa Ingredients"
    COCONUT_OF_QUENDOR = "Coconut of Quendor"
    CUBE_OF_FOUNDATION = "Cube of Foundation"
    DEATH = "Grim Journey Death"
    FILLER_AIMFIZ_SCROLL = "AIMFIZ Scroll: Transport Caster to Someone Else's Location"
    FILLER_BAYALA_SCROLL = "BAYALA Scroll: Deform Body"
    FILLER_BITTYJOO_SCROLL = "BITTYJOO Scroll: Make Lies Undetectable"
    FILLER_BLORB_SCROLL = "BLORB Scroll: Safely Protext a Small Object"
    FILLER_BLORPLE_SCROLL = "BLORPLE Scroll: Explore an Object's Mystic Connections"
    FILLER_BOOZNIK_SCROLL = "BOOZNIK Scroll: Reverse Spells in Spellbook"
    FILLER_BORCH_SCROLL = "BORCH Scroll: Put Insects to Sleep"
    FILLER_CASKLY_SCROLL = "CASKLY Scroll: Cause Perfection"
    FILLER_CLEESH_SCROLL = "CLEESH Scroll: Change a Creature Into a Small Amphibian"
    FILLER_CONBAK_SCROLL = "CONBAK Scroll: Build Strong Bodies 12 Different Ways"
    FILLER_DABHHU_SCROLL = "DABHHU Scroll: Ensure Complete Obedience"
    FILLER_DRILBO_SCROLL = "DRILBO Scroll: Strip a Floor of Yellowed Wax"
    FILLER_ESPNIS_SCROLL = "ESPNIS Scroll: Sleep"
    FILLER_EXEX_SCROLL = "EXEX Scroll: Make Things Move With Greater Speed"
    FILLER_FAIFT_SCROLL = "FAIFT Scroll: Change Appearance to Look Younger"
    FILLER_FILFRE_SCROLL = "FILFRE Scroll: Create Gratuitous Fireworks"
    FILLER_FIZMO_SCROLL = "FIZMO Scroll: Cause Stopped-Up Pipes to Unclog"
    FILLER_FOBLUB_SCROLL = "FOBLUB Scroll: Glue Audience to Seats"
    FILLER_FRIPPLE_SCROLL = "FRIPPLE Scroll: Erect a Magical Barrier"
    FILLER_FROTZ_SCROLL = "FROTZ Scroll: Cause Something to Give Off Light"
    FILLER_FWEEP_SCROLL = "FWEEP Scroll: Turn Caster Into a Bat"
    FILLER_GASPAR_SCROLL = "GASPAR Scroll: Provide for Your Own Resurrection"
    FILLER_GILCH_SCROLL = "GILCH Scroll: Astral Travel"
    FILLER_GIRGOL_SCROLL = "GIRGOL Scroll: Stop Time"
    FILLER_GHELOOH_SCROLL = "GHEL-OOH Scroll: Suspend Subject in a Gelatinous Substance"
    FILLER_GIZGUM_SCROLL = "GIZGUM Scroll: Predict Visits From Relatives"
    FILLER_GLOTH_SCROLL = "GLOTH Scroll: Fold Dough 83 Times"
    FILLER_GNUSTO_SCROLL = "GNUSTO Scroll: Write a Magic Spell Into a Spellbook"
    FILLER_GOLMAC_SCROLL = "GOLMAC Scroll: Travel Temporally"
    FILLER_GONDAR_SCROLL = "GONDAR Scroll: Extinguish Fire"
    FILLER_GORCH_SCROLL = "GORCH Scroll: Create Ladder"
    FILLER_GUNCHO_SCROLL = "GUNCHO Scroll: Banish Victim to Another Plane of Existence"
    FILLER_IMALI_SCROLL = "IMALI Scroll: Worsen Eyesight"
    FILLER_IZYUK_SCROLL = "IZYUK Scroll: Fly Like a Bird"
    FILLER_JINDAK_SCROLL = "JINDAK Scroll: Detect Magic"
    FILLER_KEPMKOMN_SCROLL = "KEPMKOMN Scroll: Cause Massive Destruction to Edifices"
    FILLER_KOAASST_SCROLL = "KOAASST Scroll: Play Soothing Ambient Music"
    FILLER_KRAK_SCROLL = "KRAK Scroll: Slow Time Drastically"
    FILLER_KREBF_SCROLL = "KREBF Scroll: Repair Willful Damage"
    FILLER_KULCAD_SCROLL = "KULCAD Scroll: Dispel a Magic Spell"
    FILLER_LESOCH_SCROLL = "LESOCH Scroll: Gust of Wind"
    FILLER_LEXDOM_SCROLL = "LEXDOM Scroll: Create Lock and Key"
    FILLER_LIDIBO_SCROLL = "LIDIBO Scroll: Make a Creature Think You Are Really Ugly"
    FILLER_LISKON_SCROLL = "LISKON Scroll: Shrink a Living Thing"
    FILLER_LOBAL_SCROLL = "LOBAL Scroll: Sharpen Hearing"
    FILLER_LOKTAR_SCROLL = "LOKTAR Scroll: Cause Temporal Distension"
    FILLER_MALYON_SCROLL = "MALYON Scroll: Animate Inanimate Objects"
    FILLER_MEEF_SCROLL = "MEEF Scroll: Cause Plants to Wilt"
    FILLER_MELBOR_SCROLL = "MELBOR Scroll: Protect From Harm by Evil Beings"
    FILLER_MUSDEX_SCROLL = "MUSDEX Scroll: Improve Muscle Tone"
    FILLER_NERZO_SCROLL = "NERZO Scroll: Balance Checkbook"
    FILLER_NIKMO_SCROLL = "NIKMO Scroll: Cause Urge to Initiate a Temporary Relationship"
    FILLER_NITFOL_SCROLL = "NITFOL Scroll: Converse With Beasts in Their Own Tongue"
    FILLER_OTSUNG_SCROLL = "OTSUNG Scroll: Erase Spell Written in Spellbook"
    FILLER_OZMOO_SCROLL = "OZMOO Scroll: Survive Unnatural Death"
    FILLER_PAXTEN_SCROLL = "PAX-TEN Scroll: Slow Productivity Through Confusion"
    FILLER_PULVER_SCROLL = "PULVER Scroll: Dry Liquids"
    FILLER_QUELBO_SCROLL = "QUELBO Scroll: Transmute Coconuts Into Gold"
    FILLER_STEGAW_SCROLL = "STEGAW Scroll: Turn Eggs Into Ripe Guano"
    FILLER_SWANZO_SCROLL = "SWANZO Scroll: Exorcise an Inhabiting Presence"
    FILLER_TINSOT_SCROLL = "TINSOT Scroll: Freeze Into Place"
    FILLER_TOSSIO_SCROLL = "TOSSIO Scroll: Turn Granite Into Fettuccini"
    FILLER_UMBOZ_SCROLL = "UMBOZ Scroll: Obviate Need for Dusting"
    FILLER_VARDIK_SCROLL = "VARDIK Scroll: Shield a Mind From an Evil Spirit"
    FILLER_VAXUM_SCROLL = "VAXUM Scroll: Make a Hostile Creature Your Friend"
    FILLER_VEZZA_SCROLL = "VEZZA Scroll: View the Future"
    FILLER_YOMIN_SCROLL = "YOMIN Scroll: Mind Probe"
    FILLER_YONK_SCROLL = "YONK Scroll: Augment the Power of Certain Spells"
    FILLER_YOZOZZO_SCROLL = "YOZOZZO Scroll: Turn Person Into a Mallard"
    FILLER_ZIMBOR_SCROLL = "ZIMBOR Scroll: Turn One Really Big City Into Lots of Tiny, Little Ashes"
    FILLER_ZOOKA_SCROLL = "ZOOKA Scroll: Turn Eggs Into Overripe Cabbage"
    FILLER_ZUGTHUG_SCROLL = "ZUGTHUG Scroll: Automatically Correct Speling Errors"
    GRIFFS_AIR_PUMP = "Griff's Air Pump"
    GRIFFS_DRAGON_TOOTH = "Griff's Dragon Tooth"
    GRIFFS_INFLATABLE_RAFT = "Griff's Inflatable Raft"
    GRIFFS_INFLATABLE_SEA_CAPTAIN = "Griff's Inflatable Sea Captain"
    HAMMER = "Hammer"
    HOTSPOT_666_MAILBOX = "Hotspot: 666 Mailbox"
    HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS = "Hotspot: Alpine's Quandry Card Slots"
    HOTSPOT_BLANK_SCROLL_BOX = "Hotspot: Blank Scroll Box"
    HOTSPOT_BLINDS = "Hotspot: Blinds"
    HOTSPOT_BUCKET = "Hotspot: Bucket"
    HOTSPOT_CANDY_MACHINE_BUTTONS = "Hotspot: Candy Machine Buttons"
    HOTSPOT_CANDY_MACHINE_COIN_SLOT = "Hotspot: Candy Machine Coin Slot"
    HOTSPOT_CANDY_MACHINE_VACUUM_SLOT = "Hotspot: Candy Machine Vacuum Slot"
    HOTSPOT_CHANGE_MACHINE_SLOT = "Hotspot: Change Machine Slot"
    HOTSPOT_CLOSET_DOOR = "Hotspot: Closet Door"
    HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT = "Hotspot: Closing the Time Tunnels Hammer Slot"
    HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER = "Hotspot: Closing the Time Tunnels Lever"
    HOTSPOT_COOKING_POT = "Hotspot: Cooking Pot"
    HOTSPOT_DENTED_LOCKER = "Hotspot: Dented Locker"
    HOTSPOT_DIRT_MOUND = "Hotspot: Dirt Mound"
    HOTSPOT_DOCK_WINCH = "Hotspot: Dock Winch"
    HOTSPOT_DRAGON_CLAW = "Hotspot: Dragon Claw"
    HOTSPOT_DRAGON_NOSTRILS = "Hotspot: Dragon Nostrils"
    HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE = "Hotspot: Dungeon Master's Lair Entrance"
    HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT = "Hotspot: Dungeon Master's House Exit"
    HOTSPOT_FLOOD_CONTROL_BUTTONS = "Hotspot: Flood Control Buttons"
    HOTSPOT_FLOOD_CONTROL_DOORS = "Hotspot: Flood Control Doors"
    HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT = "Hotspot: Frozen Treat Machine Coin Slot"
    HOTSPOT_FROZEN_TREAT_MACHINE_DOORS = "Hotspot: Frozen Treat Machine Doors"
    HOTSPOT_GLASS_CASE = "Hotspot: Glass Case"
    HOTSPOT_GRAND_INQUISITOR_DOLL = "Hotspot: Grand Inquisitor Doll"
    HOTSPOT_GUE_TECH_DOOR = "Hotspot: GUE Tech Door"
    HOTSPOT_GUE_TECH_GRASS = "Hotspot: GUE Tech Grass"
    HOTSPOT_GUE_TECH_WINDOWS = "Hotspot: GUE Tech Windows"
    HOTSPOT_HADES_PHONE_BUTTONS = "Hotspot: Hades Phone Buttons"
    HOTSPOT_HADES_PHONE_RECEIVER = "Hotspot: Hades Phone Receiver"
    HOTSPOT_HARRY = "Hotspot: Harry"
    HOTSPOT_HARRYS_ASHTRAY = "Hotspot: Harry's Ashtray"
    HOTSPOT_HARRYS_BIRD_BATH = "Hotspot: Harry's Bird Bath"
    HOTSPOT_IN_MAGIC_WE_TRUST_DOOR = "Hotspot: In Magic We Trust Door"
    HOTSPOT_JACKS_DOOR = "Hotspot: Jack's Door"
    HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS = "Hotspot: Loudspeaker Volume Buttons"
    HOTSPOT_MAILBOX_DOOR = "Hotspot: Mailbox Door"
    HOTSPOT_MAILBOX_FLAG = "Hotspot: Mailbox Flag"
    HOTSPOT_MIRROR = "Hotspot: Mirror"
    HOTSPOT_MOSSY_GRATE = "Hotspot: Mossy Grate"
    HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR = "Hotspot: Port Foozle Past Tavern Door"
    HOTSPOT_PURPLE_WORDS = "Hotspot: Purple Words"
    HOTSPOT_QUELBEE_HIVE = "Hotspot: Quelbee Hive"
    HOTSPOT_REGIONAL_CROSSROADS = "Hotspots: Crossroads"
    HOTSPOT_REGIONAL_DM_LAIR = "Hotspots: Dungeon Master's Lair"
    HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO = "Hotspots: Dragon Archipelago"
    HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM = "Hotspots: Flood Control Dam #3"
    HOTSPOT_REGIONAL_GUE_TECH = "Hotspots: GUE Tech"
    HOTSPOT_REGIONAL_HADES = "Hotspots: Hades"
    HOTSPOT_REGIONAL_MONASTERY = "Hotspots: Monastery"
    HOTSPOT_REGIONAL_PORT_FOOZLE = "Hotspots: Port Foozle"
    HOTSPOT_REGIONAL_PORT_FOOZLE_PAST = "Hotspots: Past Port Foozle"
    HOTSPOT_REGIONAL_SPELL_LAB = "Hotspots: Spell Lab"
    HOTSPOT_REGIONAL_WHITE_HOUSE = "Hotspots: White House"
    HOTSPOT_ROPE_BRIDGE = "Hotspot: Rope Bridge"
    HOTSPOT_SKULL_CAGE = "Hotspot: Skull Cage"
    HOTSPOT_SNAPDRAGON = "Hotspot: Snapdragon"
    HOTSPOT_SODA_MACHINE_BUTTONS = "Hotspot: Soda Machine Buttons"
    HOTSPOT_SODA_MACHINE_COIN_SLOT = "Hotspot: Soda Machine Coin Slot"
    HOTSPOT_SOUVENIR_COIN_SLOT = "Hotspot: Souvenir Coin Slot"
    HOTSPOT_SPELL_CHECKER = "Hotspot: Spell Checker"
    HOTSPOT_SPELL_LAB_BRIDGE_EXIT = "Hotspot: Spell Lab Bridge Exit"
    HOTSPOT_SPELL_LAB_CHASM = "Hotspot: Spell Lab Chasm"
    HOTSPOT_SPRING_MUSHROOM = "Hotspot: Spring Mushroom"
    HOTSPOT_STUDENT_ID_MACHINE = "Hotspot: Student ID Machine"
    HOTSPOT_SUBWAY_TOKEN_SLOT = "Hotspot: Subway Token Slot"
    HOTSPOT_TAVERN_FLY = "Hotspot: Tavern Fly"
    HOTSPOT_TOTEMIZER_SWITCH = "Hotspot: Totemizer Switch"
    HOTSPOT_TOTEMIZER_WHEELS = "Hotspot: Totemizer Wheels"
    HUNGUS_LARD = "Hungus Lard"
    LANDMARK = "Zork Tour Landmark"
    LARGE_TELEGRAPH_HAMMER = "Large Telegraph Hammer"
    LUCYS_PLAYING_CARD_1 = "Lucy's Playing Card: 1 Pip"
    LUCYS_PLAYING_CARD_2 = "Lucy's Playing Card: 2 Pips"
    LUCYS_PLAYING_CARD_3 = "Lucy's Playing Card: 3 Pips"
    LUCYS_PLAYING_CARD_4 = "Lucy's Playing Card: 4 Pips"
    MAP = "Map"
    MEAD_LIGHT = "Mead Light"
    MONASTERY_ROPE = "Monastery Rope"
    OLD_SCRATCH_CARD = "Old Scratch Card"
    PERMA_SUCK_MACHINE = "Perma-Suck Machine"
    PLASTIC_SIX_PACK_HOLDER = "Plastic Six-Pack Holder"
    POUCH_OF_ZORKMIDS = "Pouch of Zorkmids"
    PROZORK_TABLET = "Prozork Tablet"
    SANDWITCH_WRAPPER = "Sandwitch Wrapper"
    SCROLL_FRAGMENT_ANS = "Scroll Fragment: ANS"
    SCROLL_FRAGMENT_GIV = "Scroll Fragment: GIV"
    SHOVEL = "Shovel"
    SKULL_OF_YORUK = "Skull of Yoruk"
    SNAPDRAGON = "Snapdragon"
    SPELL_BEBURTT = "Spell: BEBURTT"
    SPELL_GLORF = "Spell: GLORF"
    SPELL_GOLGATEM = "Spell: GOLGATEM"
    SPELL_IGRAM = "Spell: IGRAM"
    SPELL_KENDALL = "Spell: KENDALL"
    SPELL_OBIDIL = "Spell: OBIDIL"
    SPELL_NARWILE = "Spell: NARWILE"
    SPELL_REZROV = "Spell: REZROV"
    SPELL_SNAVIG = "Spell: SNAVIG"
    SPELL_THROCK = "Spell: THROCK"
    SPELL_YASTARD = "Spell: YASTARD"
    STUDENT_ID = "Student ID"
    SUBWAY_DESTINATION_CROSSROADS = "Subway Destination: Crossroads"
    SUBWAY_DESTINATION_FLOOD_CONTROL_DAM = "Subway Destination: Flood Control Dam #3"
    SUBWAY_DESTINATION_HADES = "Subway Destination: Hades"
    SUBWAY_DESTINATION_MONASTERY = "Subway Destination: Monastery"
    SUBWAY_TOKEN = "Subway Token"
    SWORD = "Sword"
    TELEPORTER_DESTINATION_CROSSROADS = "Teleporter Destination: Crossroads"
    TELEPORTER_DESTINATION_DM_LAIR = "Teleporter Destination: Dungeon Master's Lair"
    TELEPORTER_DESTINATION_GUE_TECH = "Teleporter Destination: GUE Tech"
    TELEPORTER_DESTINATION_HADES = "Teleporter Destination: Hades"
    TELEPORTER_DESTINATION_MONASTERY = "Teleporter Destination: Monastery Station"
    TELEPORTER_DESTINATION_SPELL_LAB = "Teleporter Destination: Spell Lab"
    TOTEM_BROG = "Totem: Brog"
    TOTEM_GRIFF = "Totem: Griff"
    TOTEM_LUCY = "Totem: Lucy"
    TOTEMIZER_DESTINATION_HALL_OF_INQUISITION = "Totemizer Destination: Hall of Inquisition"
    TOTEMIZER_DESTINATION_INFINITY = "Totemizer Destination: Infinity"
    TOTEMIZER_DESTINATION_NEWARK_NEW_JERSEY = "Totemizer Destination: Newark, New Jersey"
    TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL = "Totemizer Destination: Straight to Hell"
    TOTEMIZER_DESTINATION_SURFACE_OF_MERZ = "Totemizer Destination: Surface of Merz"
    WELL_ROPE = "Well Rope"
    ZIMDOR_SCROLL = "ZIMDOR Scroll"
    ZORK_ROCKS = "Zork Rocks"


class ZorkGrandInquisitorItemTransforms(enum.Enum):
    MAKE_FILLER = "Make Filler"


class ZorkGrandInquisitorLandmarksanity(enum.Enum):
    OFF = 0
    ON = 1


class ZorkGrandInquisitorLocations(enum.Enum):
    ALARM_SYSTEM_IS_DOWN = "Alarm System is Down"
    AN_EXCELLENT_POPPING_UTENSIL = "An Excellent Popping Utensil"
    ARREST_THE_VANDAL = "Arrest the Vandal!"
    ARTIFACTS_EXPLAINED = "Artifacts, Explained"
    A_BIG_FAT_SASSY_2_HEADED_MONSTER = "A Big, Fat, SASSY 2-Headed Monster"
    A_LETTER_FROM_THE_WHITE_HOUSE = "A Letter from the White House"
    A_SMALLWAY = "A Smallway"
    BEAUTIFUL_THATS_PLENTY = "Beautiful, That's Plenty!"
    BEBURTT_DEMYSTIFIED = "BEBURTT, Demystified"
    BETTER_SPELL_MANUFACTURING_IN_UNDER_10_MINUTES = "Better Spell Manufacturing in Under 10 Minutes"
    BOING_BOING_BOING = "Boing, Boing, Boing"
    BONK = "Bonk!"
    BRAVE_SOULS_WANTED = "Brave Souls Wanted"
    BROG_DO_GOOD = "Brog Do Good!"
    BROG_EAT_ROCKS = "Brog Eat Rocks"
    BROG_KNOW_DUMB_THAT_DUMB = "Brog Know Dumb. That Dumb"
    BROG_MUCH_BETTER_AT_THIS_GAME = "Brog Much Better at This Game"
    CASTLE_WATCHING_A_FIELD_GUIDE = "Castle Watching: A Field Guide"
    CAVES_NOTES = "Cave's Notes"
    CLOSING_THE_TIME_TUNNELS = "Closing the Time Tunnels"
    COME_TO_PAPA_YOU_NUT = "Come to Papa. You Nut"
    CRISIS_AVERTED = "Crisis Averted"
    CUT_THAT_OUT_YOU_LITTLE_CREEP = "Cut That Out You Little Creep!"
    DEATH_ARRESTED_WITH_JACK = "Death: Interesting Philosophical Thought"
    DEATH_ATTACKED_THE_QUELBEES = "Death: Just Under Half a Second"
    DEATH_CLIMBED_OUT_OF_THE_WELL = "Death: Breaking Curfew"
    DEATH_EATEN_BY_A_GRUE = "Death: Pitch Black Cave in a Zork Game"
    DEATH_JUMPED_IN_BOTTOMLESS_PIT = "Death: Old Age"
    DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER = "Death: Mind-Boggling Unlucky Streak"
    DEATH_LOST_SOUL_TO_OLD_SCRATCH = "Death: Contractually Obligated"
    DEATH_OUTSMARTED_BY_THE_QUELBEES = "Death: Antennae Nose Plugs"
    DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD = "Death: Chop, Slice, Puree"
    DEATH_STEPPED_INTO_THE_INFINITE = "Death: Tiny Step for Mankind"
    DEATH_SWALLOWED_BY_A_DRAGON = "Death: Spare Loft Behind Uvula"
    DEATH_THROCKED_THE_GRASS = "Death: Expressly Forbidden"
    DEATH_TOTEMIZED_INFINITY = "Death: Airless Expanse of the Cosmos"
    DEATH_TOTEMIZED_NEWARK_NEW_JERSEY = "Death: Arteriosclerosis"
    DEATH_TOTEMIZED_PERMANENTLY_HALLS_OF_INQUISITION = "Death: Ms. Peeper's Paperweight"
    DEATH_TOTEMIZED_PERMANENTLY_INFINITY = "Death: S.S. Feinstein's Tractor Beam"
    DEATH_TOTEMIZED_PERMANENTLY_NEWARK_NEW_JERSEY = "Death: Manhole Cover in New Jersey"
    DEATH_TOTEMIZED_PERMANENTLY_STRAIGHT_TO_HELL = "Death: Evil Spawn's Plaything"
    DEATH_TOTEMIZED_PERMANENTLY_SURFACE_OF_MERZ = "Death: Eternity Gazing at the Scenic Vista"
    DEATH_TOTEMIZED_SURFACE_OF_MERZ = "Death: Very, Very Pretty"
    DEATH_YOURE_NOT_CHARON = "Death: Not Charon"
    DEATH_ZORK_ROCKS_EXPLODED = "Death: Pretty Painless"
    DENIED_BY_THE_LAKE_MONSTER = "Denied by the Lake Monster"
    DINGWHACKER_DELUXE = "Dingwhacker Deluxe"
    DONT_EVEN_START_WITH_US_SPARKY = "Don't Even Start With Us, Sparky"
    DONT_GO_SPENDING_IT_ALL_IN_ONE_PLACE = "Don't Go Spending it All in One Place"
    DOOOOOOWN = "Doooooown"
    DOWN = "Down"
    DRAGON_ARCHIPELAGO_TIME_TUNNEL = "Dragon Archipelago Time Tunnel"
    DUNCE_LOCKER = "Dunce Locker"
    EGGPLANTS = "Eggplants"
    ELSEWHERE = "Elsewhere"
    EMERGENCY_MAGICATRONIC_MESSAGE = "Emergency Magicatronic Message"
    ENJOY_YOUR_TRIP = "Enjoy Your Trip!"
    FAT_LOT_OF_GOOD_THATLL_DO_YA = "Fat Lot of Good That'll Do Ya"
    FIRE_FIRE = "Fire! Fire!"
    FLOOD_CONTROL_DAM_3_THE_NOT_REMOTELY_BORING_TALE = "Flood Control Dam #3: The Not Remotely Boring Tale"
    FLYING_SNAPDRAGON = "Flying Snapdragon"
    FROBUARY_3_UNDERGROUNDHOG_DAY = "Frobruary 3 - Undergroundhog Day"
    GETTING_SOME_CHANGE = "Getting Some Change"
    GOOD_PUZZLE_SMART_BROG = "Good Puzzle. Smart Brog"
    GO_AWAY = "GO AWAY!"
    GUE_TECH_ENTRANCE_EXAM = "GUE Tech Entrance Exam"
    HAVE_A_HELL_OF_A_DAY = "Have a Hell of a Day!"
    HELLO_THIS_IS_SHONA_FROM_GURTH_PUBLISHING = "Hello, This is Shona from Gurth Publishing"
    HELP_ME_CANT_BREATHE = "Help... Me. Can't... Breathe"
    HEY_FREE_DIRT = "Hey, Free Dirt!"
    HMMM_BIG_TOOTHPICK = "Hmmm. Big Toothpick"
    HMMM_INFORMATIVE_YET_DEEPLY_DISTURBING = "Hmmm. Informative. Yet Deeply Disturbing"
    HOW_TO_HYPNOTIZE_YOURSELF = "How to Hypnotize Yourself"
    HOW_TO_WIN_AT_DOUBLE_FANUCCI = "How to Win at Double Fanucci"
    IMBUE_BEBURTT = "Imbue BEBURTT"
    IM_COMPLETELY_NUDE = "I'm Completely Nude"
    INFLATUS_THE_ETERNAL = "Inflatus the Eternal"
    INTO_THE_FOLIAGE = "Into the Foliage"
    INVISIBLE_FLOWERS = "Invisible Flowers"
    IN_CASE_OF_ADVENTURE = "In Case of Adventure, Break Glass!"
    IN_MAGIC_WE_TRUST = "In Magic We Trust"
    ITS_ALMOST_AS_IF_IT_WERE_INFINITE = "It's Almost as if it Were... Infinite"
    ITS_ONE_OF_THOSE_ADVENTURERS_AGAIN = "It's One of Those Adventurers Again..."
    ITS_PLAYING_A_LITTLE_HARD_TO_GET = "It's Playing a Little Hard to Get"
    IT_DOESNT_APPEAR_TO_BE_FOOLED = "It Doesn't Appear to be Fooled"
    I_AM_NOT_IMPRESSED = "I Am Not Impressed"
    I_DONT_THINK_YOU_WOULDVE_WANTED_THAT_TO_WORK_ANYWAY = "I Don't Think You Would've Wanted That to Work Anyway"
    I_DONT_WANT_NO_TROUBLE = "I Don't Want No Trouble!"
    I_LIKE_YOUR_STYLE = "I Like Your Style!"
    I_SPIT_ON_YOUR_FILTHY_COINAGE = "I Spit on Your Filthy Coinage"
    LANDMARK_DRAGON_ARCHIPELAGO = "Landmark Visited: Dragon Archipelago"
    LANDMARK_DUNGEON_MASTERS_HOUSE = "Landmark Visited: Dungeon Master's House"
    LANDMARK_FLOOD_CONTROL_DAM_3 = "Landmark Visited: Flood Control Dam #3"
    LANDMARK_GATES_OF_HELL = "Landmark Visited: Gates of Hell"
    LANDMARK_GREAT_UNDERGROUND_EMPIRE_ENTRANCE = "Landmark Visited: Great Underground Empire Entrance"
    LANDMARK_GUE_TECH_FOUNTAIN_INSIDE = "Landmark Visited: GUE Tech Fountain (Inside)"
    LANDMARK_GUE_TECH_FOUNTAIN_OUTSIDE = "Landmark Visited: GUE Tech Fountain (Outside)"
    LANDMARK_HADES_SHORE = "Landmark Visited: Hades Shore"
    LANDMARK_INFINITE_CORRIDOR = "Landmark Visited: Infinite Corridor"
    LANDMARK_INQUISITION_HEADQUARTERS = "Landmark Visited: Inquisition Headquarters"
    LANDMARK_JACKS_SHOP = "Landmark Visited: Jack's Shop"
    LANDMARK_MIRROR_ROOM = "Landmark Visited: Mirror Room"
    LANDMARK_PAST_PORT_FOOZLE = "Landmark Visited: Past Port Foozle"
    LANDMARK_PORT_FOOZLE = "Landmark Visited: Port Foozle"
    LANDMARK_SPELL_CHECKER = "Landmark Visited: Spell Checker"
    LANDMARK_TOTEMIZER = "Landmark Visited: Totemizer"
    LANDMARK_UMBRELLA_TREE = "Landmark Visited: Umbrella Tree"
    LANDMARK_UNDERGROUND_UNDERGROUND_ENTRANCE = "Landmark Visited: Underground Underground Entrance"
    LANDMARK_WALKING_CASTLES_HEART = "Landmark Visited: Walking Castle's Heart"
    LANDMARK_WHITE_HOUSE = "Landmark Visited: White House"
    LIT_SUNFLOWERS = "Lit Sunflowers"
    LOOK_AN_ICE_CREAM_BAR = "Look! An Ice Cream Bar"
    MAILED_IT_TO_HELL = "Mailed it to Hell"
    MAKE_LOVE_NOT_WAR = "Make Love, Not War"
    MEAD_LIGHT = "Mead Light?"
    ME_I_AM_THE_BOSS_OF_YOU = "Me! I am the Boss of You!"
    MIKES_PANTS = "Mike's Pants"
    MUSHROOM_HAMMERED = "Mushroom, Hammered"
    NATIONAL_TREASURE = "300 Year Old National Treasure"
    NATURAL_AND_SUPERNATURAL_CREATURES_OF_QUENDOR = "Natural and Supernatural Creatures of Quendor"
    NOOOOOOOOOOOOO = "NOOOOOOOOOOOOO!"
    NOTHIN_LIKE_A_GOOD_STOGIE = "Nothin' Like a Good Stogie"
    NOW_YOU_LOOK_LIKE_US_WHICH_IS_AN_IMPROVEMENT = "Now You Look Like Us, Which is an Improvement"
    NO_AUTOGRAPHS = "No Autographs"
    NO_BONDAGE = "No Bondage"
    NO_ONE_RETURNS_FROM_HADES = "NO ONE Returns from Hades"
    OBIDIL_DRIED_UP = "OBIDIL, Dried Up"
    OH_DEAR_GOD_ITS_A_DRAGON = "Oh Dear God, It's a Dragon!"
    OH_VERY_FUNNY_GUYS = "Oh, Very Funny Guys"
    OH_WOW_TALK_ABOUT_DEJA_VU = "Oh, Wow! Talk About Deja Vu"
    OLD_SCRATCH_WINNER = "Old Scratch Winner!"
    ONLY_YOU_CAN_PREVENT_FOOZLE_FIRES = "Only You Can Prevent Foozle Fires"
    OPEN_THE_GATES_OF_HELL = "Open the Gates of Hell"
    OUTSMART_THE_QUELBEES = "Outsmart the Quelbees"
    PERMASEAL = "PermaSeal"
    PLANETFALL = "Planetfall"
    PLEASE_DONT_THROCK_THE_GRASS = "Please Don't THROCK the Grass"
    PORT_FOOZLE_TIME_TUNNEL = "Port Foozle Time Tunnel"
    PROZORKED = "Prozorked"
    PURPLE_BEAST_ALARM_SYSTEM = "Purple Beast Alarm System"
    REASSEMBLE_SNAVIG = "Reassemble SNAVIG"
    RESTOCKED_ON_GRUESDAY = "Restocked on Gruesday"
    RIGHT_HELLO_YES_UH_THIS_IS_SNEFFLE = "Right. Hello. Yes. Uh, This is Sneffle"
    RIGHT_UH_SORRY_ITS_ME_AGAIN_SNEFFLE = "Right. Uh, Sorry. It's Me Again. Sneffle"
    SNAVIG_REPAIRED = "SNAVIG, Repaired"
    SOUVENIR = "Souvenir"
    SPELL_CHECK_COMPLETE = "Spell Check Complete"
    STRAIGHT_TO_HELL = "Straight to Hell"
    STRIP_GRUE_FIRE_WATER = "Strip Grue, Fire, Water"
    SUCKING_ROCKS = "Sucking Rocks"
    TALK_TO_ME_GRAND_INQUISITOR = "Talk to Me Grand Inquisitor"
    TAMING_YOUR_SNAPDRAGON = "Taming Your Snapdragon"
    THAR_SHE_BLOWS = "Thar She Blows!"
    THATS_A_ROPE = "That's a Rope"
    THATS_IT_JUST_KEEP_HITTING_THOSE_BUTTONS = "That's it! Just Keep Hitting Those Buttons"
    THATS_STILL_A_ROPE = "That's Still a Rope"
    THATS_THE_SPIRIT = "That's the Spirit!"
    THE_ALCHEMICAL_DEBACLE = "The Alchemical Debacle"
    THE_ENDLESS_FIRE = "The Endless Fire"
    THE_FLATHEADIAN_FUDGE_FIASCO = "The Flatheadian Fudge Fiasco"
    THE_ONLY_WAY_TO_WIN_IS_NOT_TO_PLAY = "The Only Way to Win is Not to Play"
    THE_PERILS_OF_MAGIC = "The Perils of Magic"
    THE_UNDERGROUND_UNDERGROUND = "The Underground Underground"
    THIS_DOESNT_LOOK_ANYTHING_LIKE_THE_BROCHURE = "This Doesn't Look Anything Like the Brochure"
    THROCKED_MUSHROOM_HAMMERED = "THROCKed Mushroom, Hammered"
    TIME_TRAVEL_FOR_DUMMIES = "Time Travel for Dummies"
    TOTEMIZED_DAILY_BILLBOARD = "Totemized Daily Billboard Functioning Correctly"
    UH_OH_BROG_CANT_SWIM = "Uh-Oh. Brog Can't Swim"
    UMBRELLA_FLOWERS = "Umbrella Flowers"
    UM_AH_UM_AH_UM_AH = "Um. Ah. Um. Ah. Um. Ah."
    UP = "Up"
    USELESS_BUT_FUN = "Useless, But Fun"
    UUUUUP = "Uuuuup"
    VOYAGE_OF_CAPTAIN_ZAHAB = "Voyage of Captain Zahab"
    WANT_SOME_RYE_COURSE_YA_DO = "Want Some Rye? Course Ya Do!"
    WANT_SOME_RYE_COURSE_YA_DO_PAST = "Want Some Rye? ... Course Ya Do!"
    WE_DONT_SERVE_YOUR_KIND_HERE = "We Don't Serve Your Kind Here"
    WE_GOT_A_HIGH_ROLLER = "We Got a High Roller!"
    WHAT_ARE_YOU_STUPID = "What Are You, Stupid?"
    WHITE_HOUSE_TIME_TUNNEL = "White House Time Tunnel"
    WHOOPS = "Whoops!"
    WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE = "Wow! I've Never Gone Inside Him Before!"
    YAD_GOHDNUORGREDNU_3_YRAUBORF = "yaD gohdnuorgrednU - 3 yrauborF"
    YOUR_PUNY_WEAPONS_DONT_PHASE_ME_BABY = "Your Puny Weapons Don't Phase Me, Baby!"
    YOU_DONT_GO_MESSING_WITH_A_MANS_ZIPPER = "You Don't Go Messing With a Man's Zipper"
    YOU_GAINED_86_EXPERIENCE_POINTS = "You Gained 86 Experience Points"
    YOU_LOSE_MUFFET_ANTE_UP = "You Lose, Muffet. Ante Up"
    YOU_ONE_OF_THEM_AGITATORS_AINT_YA = "You One of Them Agitators, Ain't Ya?"
    YOU_WANT_A_PIECE_OF_ME_DOCK_BOY = "You Want a Piece of Me, Dock Boy? or Girl"
    ZIMDOR_IS_UNDAMAGED = "ZIMDOR is Undamaged"


class ZorkGrandInquisitorLocationTransforms(enum.Enum):
    REMOVE = "Remove"


class ZorkGrandInquisitorRegions(enum.Enum):
    ANYWHERE = "Anywhere"
    CROSSROADS = "Crossroads"
    DM_LAIR = "Dungeon Master's Lair"
    DM_LAIR_INTERIOR = "Dungeon Master's Lair - Interior"
    DRAGON_ARCHIPELAGO = "Dragon Archipelago"
    DRAGON_ARCHIPELAGO_DRAGON = "Dragon Archipelago - Dragon"
    ENDGAME = "Endgame"
    GUE_TECH = "GUE Tech"
    GUE_TECH_ENTRANCE = "GUE Tech - Entrance"
    GUE_TECH_HALLWAY = "GUE Tech - Hallway"
    GUE_TECH_OUTSIDE = "GUE Tech - Outside"
    HADES = "Hades"
    HADES_BEYOND_GATES = "Hades - Beyond Gates"
    HADES_SHORE = "Hades - Shore"
    MENU = "Menu"
    MONASTERY = "Monastery"
    MONASTERY_EXHIBIT = "Monastery - Exhibit"
    PORT_FOOZLE = "Port Foozle"
    PORT_FOOZLE_JACKS_SHOP = "Port Foozle - Jack's Shop"
    PORT_FOOZLE_PAST = "Port Foozle Past"
    PORT_FOOZLE_PAST_TAVERN = "Port Foozle Past - Tavern"
    SPELL_LAB = "Spell Lab"
    SPELL_LAB_BRIDGE = "Spell Lab - Bridge"
    SUBWAY_CROSSROADS = "Subway Platform - Crossroads"
    SUBWAY_FLOOD_CONTROL_DAM = "Subway Platform - Flood Control Dam #3"
    SUBWAY_MONASTERY = "Subway Platform - Monastery"
    WALKING_CASTLE = "Walking Castle"
    WHITE_HOUSE = "White House"
    WHITE_HOUSE_INTERIOR = "White House - Interior"


class ZorkGrandInquisitorStartingLocations(enum.Enum):
    PORT_FOOZLE = 0
    CROSSROADS = 1
    DM_LAIR = 2
    DM_LAIR_INTERIOR = 3
    GUE_TECH = 4
    SPELL_LAB = 5
    HADES_SHORE = 6
    SUBWAY_FLOOD_CONTROL_DAM = 7
    MONASTERY = 8
    MONASTERY_EXHIBIT = 9


class ZorkGrandInquisitorTags(enum.Enum):
    CORE = "Core"
    DEATHSANITY = "Deathsanity"
    FILLER = "Filler"
    GOAL_ARTIFACT_OF_MAGIC_HUNT = "Goal: Artifact of Magic Hunt"
    GOAL_GRIM_JOURNEY = "Goal: Grim Journey"
    GOAL_SPELL_HEIST = "Goal: Spell Heist"
    GOAL_THREE_ARTIFACTS = "Goal: Three Artifacts"
    GOAL_ZORK_TOUR = "Goal: Zork Tour"
    HOTSPOT = "Hotspot"
    HOTSPOT_REGIONAL = "Regional Hotspot"
    INVENTORY_ITEM = "Inventory Item"
    LANDMARKSANITY = "Landmarksanity"
    MISSABLE = "Missable"
    SPELL = "Spell"
    SUBWAY_DESTINATION = "Subway Destination"
    TELEPORTER_DESTINATION = "Teleporter Destination"
    TOTEMIZER_DESTINATION = "Totemizer Destination"
    TOTEM = "Totem"
