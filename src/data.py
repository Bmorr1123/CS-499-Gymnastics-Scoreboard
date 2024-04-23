import constants
import db.models


class DisplaySettings:
    def __init__(
            self,
            display_logo: bool = True,
            display_start_value: bool = True,
            display_judges: bool = True,
            display_order: bool = True
    ):
        self.display_logo: bool = display_logo
        self.display_start_value: bool = display_start_value
        self.display_judges: bool = display_judges
        self.display_order: bool = display_order

    def __str__(self):
        return f"DisplaySettings<display_logo={self.display_logo} , display_start_value={self.display_start_value} , display_judges={self.display_judges} , display_order={self.display_order}>"


class EventLineupManager:
    def __init__(
            self,
            lineup_objects: list[db.models.Lineup],
            lineup_entry_objects: [db.models.LineupEntry],
    ):
        self.lineup_objects: list[db.models.Lineup] = lineup_objects
        self.lineup_entry_objects: list[db.models.LineupEntry] = lineup_entry_objects

        self.current_apparatus_index: int | None = None
        self.current_gymnast_index: int | None = None

        self.apparatus_order: list[str] | None = None

        self._current_lineup: db.models.Lineup | None = None
        self._current_lineup_entries: list[db.models.LineupEntry] | None = None

    def start_event(self, apparatus_order: list[str]):
        assert len(apparatus_order) == 4, "Incorrect apparatus count."
        apparatus_names = [app.short_name for app in constants.APPARATUS_TYPES]
        for apparatus in apparatus_order:
            assert apparatus in apparatus_names, f"Apparatus with name \"{apparatus}\" could not be found."

        self.apparatus_order = apparatus_order
        self.current_gymnast_index = -1
        self.current_apparatus_index = -1

        self.next_apparatus()
        self.next_gymnast()

        self.get_current_lineup()
        self.get_current_lineup_entries()

    def _find_current_lineup(self) -> db.models.Lineup | None:
        if self.current_apparatus_index is None or not self.apparatus_order:
            return None
        for lineup in self.lineup_objects:
            if lineup.apparatus_name == self.apparatus_order[self.current_apparatus_index]:
                return lineup

        return None

    def _find_current_lineup_entries(self) -> list[db.models.LineupEntry] | None:
        current_lineup = self.get_current_lineup()
        if current_lineup is None:
            return None

        current_lineup_entries: list[db.models.LineupEntry] = []
        for lineup_entry in self.lineup_entry_objects:
            if lineup_entry.lineup_id == current_lineup.lineup_id:
                current_lineup_entries.append(lineup_entry)

        current_lineup_entries.sort(key=lambda lineup_entry: lineup_entry.order, reverse=True)
        return current_lineup_entries

    def get_current_lineup(self) -> db.models.Lineup | None:
        if not self._current_lineup:
            self._current_lineup = self._find_current_lineup()

        return self._current_lineup

    def get_current_lineup_entries(self) -> list[db.models.LineupEntry] | None:
        if not self._current_lineup_entries:
            self._current_lineup_entries = self._find_current_lineup_entries()

        return self._current_lineup_entries

    def get_current_gymnast_id(self) -> int | None:
        if self.current_gymnast_index is None or self.current_apparatus_index is None:
            return None
        entries = self.get_current_lineup_entries()
        if not entries:
            return None

        return entries[self.current_gymnast_index].gymnast_id

    def get_current_apparatus_name(self) -> str | None:
        if self.current_apparatus_index is None or not self.apparatus_order:
            return None

        return self.apparatus_order[self.current_apparatus_index]

    def next_gymnast(self) -> bool:
        if self.current_gymnast_index is None or self.current_apparatus_index is None:
            return False
        entries = self.get_current_lineup_entries()
        if not entries:
            return False

        if len(entries) <= self.current_gymnast_index + 1:
            return False
        self.current_gymnast_index += 1
        return True

    def next_apparatus(self) -> bool:
        if self.current_apparatus_index is None or not self.apparatus_order:
            return False

        if len(self.apparatus_order) <= self.current_apparatus_index + 1:
            return False
        self.current_apparatus_index += 1
        return True


class MeetData:
    singleton = None

    @classmethod
    def get_data(cls):
        if MeetData.singleton:
            return MeetData.singleton
        else:
            MeetData.singleton = MeetData()
            return MeetData.singleton

    def __init__(self):
        self.meet_format: constants.MeetType | None = None
        self.event_id: int | None = None
        self.schools: list[str | None] = [None for i in range(4)]
        self.event_lineup_managers: list[EventLineupManager | None] = [None for i in range(4)]
        self.gymnasts: [db.models.Gymnast] = []
        self.display_settings: DisplaySettings = DisplaySettings()

