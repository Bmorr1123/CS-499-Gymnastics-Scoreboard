
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
