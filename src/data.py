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
        self.schools: [db.models.School] = [None for i in range(4)]
        self.gymnasts: [db.models.Gymnast] = []
        self.display_settings: DisplaySettings = DisplaySettings()