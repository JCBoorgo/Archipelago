from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class Pikmin4ArchipelagoOptions:
    pass


class Pikmin4Game(Game):
    name = "Pikmin 4"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = Pikmin4ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="For treasure objectives, collect all instances of the required treasure",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Collect the following Treasure: TREASURE",
                data={
                    "TREASURE": (self.treasures, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Rescue CREWMATE",
                data={
                    "CREWMATE": (self.crewmates, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Max out the following Oatchi: OATCHI",
                data={
                    "OATCHI": (self.oatchi, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get a Gold Medal in the following Dandori Challenge: DANDORI",
                data={
                    "DANDORI": (self.dandori_challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="100% the following Cave: CAVE",
                data={
                    "CAVE": (self.caves, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ]

    @staticmethod
    def treasures() -> List[str]:
        return [
            "Universal Rubber Cutie",
            "Planetary Rubber Cutie",
            "Stately Rubber Cutie",
            "Dapper Rubber Cutie",
            "Sweet Stumble-Not",
            "Sweet Torrent",
            "Deceptive Snack",
            "Cookie of Nibbled Circles",
            "Cookie of Prosperity",
            "Vanishing Cookie",
            "Love's Fortune Cookie",
            "Hearty Container",
            "Jiggle-Jiggle",
            "S.S. Berry",
            "S.S. Peppermint",
            "S.S. Chocolate",
            "Unbreakable Promise",
            "Golden Vaulting Table",
            "Olfactory Sculpture",
            "Princess Pearl",
            "Sticky Jewel",
            "Hoop of Healing",
            "Hoop of Passion",
            "Hoop of Fortune",
            "Tandem Trainer",
            "Sphere of Fuzzy Feelings",
            "Orbital Communication Sphere",
            "Orb of Destruction",
            "Greed-inducement Device",
            "Disk of Joyous Wisdom",
            "Disk of Angry Wisdom",
            "Disk of Sorrowful Wisdom",
            "Disk of Amusing Wisdom",
            "Disk of Surprising Wisdom",
            "Secured Satchel",
            "Floral Instigator",
            "Fastening Item",
            "Trap Lid",
            "Perforated Raft",
            "Gift of Friendship",
            "Memory Fragment (Top Left)",
            "Memory Fragment (Top-ish)",
            "Memory Fragment (Top...Probably?)",
            "Memory Fragment (Top Right)",
            "Memory Fragment (Left Edge)",
            "Memory Fragment (Center Left)",
            "Memory Fragment (Center Right)",
            "Memory Fragment (Right Edge)",
            "Memory Fragment (Bottom Left)",
            "Memory Fragment (Bottom-ish)",
            "Memory Fragment (Bottom...Probably?)",
            "Memory Fragment (Bottom Right)",
            "Condensed Sunshine",
            "Flaky Temptation",
            "Cushion Cake",
            "Puzzle Snack",
            "Sphere of Desire",
            "Sphere of Family",
            "Sphere of Heart",
            "Sphere of Beginnings",
            "Sphere of Vitality",
            "Sphere of Calm",
            "Sphere of Good Fortune",
            "Sphere of Trust",
            "Sphere of Support",
            "Sphere of Truth",
            "Sunseed Berry",
            "Cupid's Grenade",
            "Searing Acidshock",
            "Velvety Dreamdrop",
            "Astringent Clump",
            "Wayward Moon",
            "Lesser Mock Bottom",
            "Mock Bottom",
            "Dawn Pustules",
            "Dusk Pustules",
            "Crimson Banquet",
            "Juicy Gaggle",
            "Zest Bomb",
            "Delectable Bouquet",
            "Portable Sunset",
            "Tremendous Sniffer",
            "Crunchy Deluge",
            "Disguised Delicacy",
            "Blonde Imposter",
            "Merciless Extractor",
            "Citrus Lump",
            "Face Wrinkler",
            "Pocked Airhead",
            "Insect Condo",
            "Dapper Blob",
            "Scaly Custard",
            "Seed Hive",
            "Stellar Extrusion",
            "Heroine's Tear",
            "Slapstick Crescent",
            "Fire-Breathing Feast",
            "Dusty Bed",
            "Doggy Bed",
            "Birdy Bed",
            "Fishy Bed",
            "Granddaughter Doll Head",
            "Gifting Vase",
            "Daughter Doll Head",
            "Mooching Vase",
            "Mama Doll Head",
            "Empty Vase",
            "King of Meats",
            "Maestro of Flavor",
            "Belted Delicacy",
            "Fish-Bed Snack",
            "The Four Grill Brothers",
            "Harmonic Synthesizer",
            "Spouse Alert",
            "Path Creator",
            "Time Marker",
            "Wind Detector",
            "Ambiguous Hostel",
            "Mega Horn",
            "Mechanical Harp (Memory Song)",
            "Mechanical Harp (Lullabies)",
            "Mechanical Harp (Windmills)",
            "Emperor Whistle",
            "Shake-a-Smile",
            "Amplified Amplifier",
            "Double Dragon-Eyed Scope",
            "Temporal Mechanism",
            "Director of Destiny",
            "Detective's Truth Seeker",
            "Unlimited Locomotive",
            "Middle-Management Tank Car",
            "Leisure Car",
            "Life Station",
            "Straight-and-Narrow Track",
            "Turn-of-Events Track",
            "Back-at-the-Beginning Track",
            "Thrill-Ride Track",
            "Mouth of Lies",
            "Monster Teeth",
            "Brush of Wisdom",
            "Brush of Foolishness",
            "False Lollipop",
            "Maternal Sculpture",
            "Bathing Pool",
            "Think-Tank Combobot",
            "Nexus Combobot",
            "Fist-Force Combobot",
            "Peacemaker Combobot",
            "Kick-Start Combobot",
            "Sure-Footed Combobot",
            "Uniquely You Goo",
            "Decorative Goo",
            "Illumination Goo",
            "Noble Goo",
            "True Goo",
            "Ambiguous Goo",
            "Captivation Goo",
            "Refreshing Goo",
            "Neon Goo",
            "Lamp of Inspiration",
            "Beckoning Mannequin",
            "Ancient Statue Head",
            "Contemplation Station",
            "Unfinished Statue",
            "Persistence Machine",
            "Giant's Fossil",
            "Expression Hider",
            "Buddy Display",
            "Heat Sensor",
            "Internal-Clock Measurer",
            "Solar-Powered Computing Machine",
            "Number Jumper",
            "Octoplus",
            "Mystery Squish Fish",
            "Newtolite Shell",
            "Slipper-Bug Fossil",
            "Relentless Spear",
            "Noble Bident",
            "Shattering Lance",
            "Micromanagement Station",
            "Glinty Circular Disc",
            "Life Controller",
            "Spinning Memories Plank",
            "Masterpiece Plank",
            "Telekinesis Detector",
            "Connection Detector",
            "Creativity Conduit",
            "Stone of Advancement",
            "Winged Freedom Sculpture",
            "Dimension Converter",
            "Soul Reverberator",
            "Personal-Injury Plank",
            "Don't-See-It Specs",
            "Love Nugget",
            "Crush Nugget",
            "Anxious Sprout",
            "Crew-Cut Gourd",
            "Child of the Earth",
            "Daughter of the Earth",
            "Mysterious Carriage",
            "Snack Bean",
            "Foolish Fruit",
            "Blast Shield",
            "Ring-of-Return Shield",
            "Satellite Shield",
            "Heroic Shield",
            "Shooting-Star Shield",
            "Heart Sword",
            "Spirit Sword",
            "Ice Sword",
            "Heroic Sword",
            "Bright Sword",
            "Unfloatable Boat",
            "Faux Fishy",
            "Space Spinner",
            "Sweet-Soaked Blue Bird",
            "Skin of the Phoenix",
            "Priceless Bird",
            "Aspiration-Ritual Ball",
            "Aspiration-Ritual Pole",
            "Divine Balloon",
            "Deity's Portrait",
            "Devil's Portrait",
            "Courage Emblem",
            "Power Emblem",
            "Wisdom Emblem",
            "Love Emblem",
            "Money Emblem",
            "Work Emblem",
            "Gold Nugget",
            "Long-Shot Totem",
            "Go-with-the-Flow Totem",
            "Chance Totem",
            "Difficult-Choice Totem",
            "Talisman of Life (Crane)",
            "Talisman of Life (Cherry Blossom)",
            "Talisman of Life (Moon)",
            "Talisman of Life (Rain)",
            "Talisman of Life (Phoenix)",

        ]

    @staticmethod
    def caves() -> List[str]:
        return [
            "Aquiferous Summit",
            "Crackling Cauldron",
            "Hectic Hollows",
            "Industrial Maze",
            "Last-Frost Cavern",
            "Drafty Gallery",
            "Kingdom of Beasts",
            "Secluded Courtyard",
            "Sightless Passage",
            "Below-Grade Discotheque",
            "Engulfed Castle",
            "Seafloor Resort",
            "Subzero Sauna",
            "Doppelganger's Den",
            "Frozen Inferno",
            "Plunder Palace",
            "Cradle of the Beast",
            "Dream Home",
            "Ultimate Testing Range",
            "Cavern for a King",
            "Subterranean Swarm",
            "The Mud Pit",
        ]

    @staticmethod
    def crewmates() -> List[str]:
        return [
            "Russ",
            "Dingo",
            "Yonny",
            "Bernard",
            "Olimar",
            "Louie",
            "Nelle",
            "Don Bergman",
            "Yorke",
            "Schnauz",
            "Dalmo",
            "Corgwin",
            "Jin",
            "Puddle",
            "Chet",
            "François",
            "Pitunia",
            "Sy",
            "Osa",
            "Kit",
            "Twyla",
            "Sammy",
            "Komo",
            "Ren",
            "Chewy",
            "Santi",
            "Sheeba",
            "Keesh",
            "Kaia",
            "Mika",
            "Molly",
            "Lapi",
            "Boris",
            "Horatio",
            "Wolfgang",
            "Muggs",
            "Vonda",
            "Frisé",
            "Chowder",
            "Kayz",
            "Alpin",
            "Fawks",
            "Kingsly",
            "Bernise",
            "Grace",
            "Dash",
            "Patch",
            "Beaux",
        ]

    @staticmethod
    def oatchi() -> List[str]:
        return [
            "Super Buff",
            "Big Chomp",
            "Mega Rush",
            "Doggy Paddle",
            "Pluck",
            "Dig",
            "Heal",
            "Command",
        ]

    @staticmethod
    def dandori_challenges() -> List[str]:
        return [
            "Dandori Day Care",
            "Hotshock Canyon",
            "Rockaway Cellars",
            "Test Tubs",
            "Ice-Cross Course",
            "Hefty Haulway",
            "Aerial Incinerator",
            "Strategic Freezeway",
            "Planning Pools",
            "Toggle Training",
            "Cliff-Hanger's Hold",
            "Oasis of Order",
        ]


# Archipelago Options
# ...
