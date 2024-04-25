
class MeetType:
    def __init__(
            self,
            short_name: str,
            long_name: str,
            team_count: int
    ):
        self.short_name: str = short_name
        self.long_name: str = long_name
        self.team_count: int = team_count


MEET_TYPES = [
    MeetType("Dual", "Dual", 2),
    MeetType("Tri", "Triangular", 3),
    MeetType("Quad", "Quadrangular", 4)
]


class ApparatusType:
    def __init__(
            self,
            abbreviation: str,
            short_name: str,
            full_names: str,
            sub_options: list[str] | None
    ):
        self.abbreviation = abbreviation
        self.short_name = short_name
        self.full_names = full_names
        self.sub_options = sub_options


APPARATUS_TYPES = [
    ApparatusType("Vt", "Vault", "Vault", None),
    ApparatusType("Bs", "Bars", "Uneven Parallel Bars", None),
    ApparatusType("Bm", "Beam", "Balance Beam", None),
    ApparatusType("Fr", "Floor", "Floor Exercise", None),
]
"""
Format:
    0 is Home Team
    1-3 is Visitor Team 1-3

Dual Meet:
    Home - Vault, Bar, HALFTIME, Beam, Floor
    Visitor - Bars, Vault, HALFTIME, Floor, Beam 

Tri Meet:
    Home - Vault, Bars, NOTHING, Beam, NOTHING, Floor
    Visitor 1 - Bars, NOTHING, Vaults, NOTHING, Floor, Beam
    Visitor 2 - NOTHING, Vault, Bars, Floor, Beam, NOTHING

Quad Meet:
    Home - Vault, Bars, Beam, Floor
    Visitor 1 - Floor, Vault, Bars, Beam
    Visitor 2 - Beam, Floor, Vault, Bars
    Visitor 3 -  Bars, Beam, Floor, Vault
"""
APPARATUS_ORDERING = {
    2: {
        0: ["Vault", "Bars", "Break", "Beam", "Floor"],
        1: ["Bars", "Vault", "Break", "Floor", "Beam"]
    },
    3: {
        0: ["Vault", "Bars", "Break", "Beam", "Break", "Floor"],
        1: ["Bars", "Break", "Vault", "Break", "Floor", "Beam"],
        2: ["Break", "Vault", "Bars", "Floor", "Beam", "Break"]
    },
    4: {
        0: ["Vault", "Bars", "Beam", "Floor"],
        1: ["Floor", "Vault", "Bars", "Beam"],
        2: ["Beam", "Floor", "Vault", "Bars"],
        3: ["Bars", "Beam", "Floor", "Vault"]
    }
}
