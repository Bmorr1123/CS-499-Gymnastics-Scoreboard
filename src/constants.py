
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
