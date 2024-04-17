from sqlalchemy import create_engine, URL, select, union_all, Select
from sqlalchemy.orm import Session
from os import getenv
from dotenv import load_dotenv
from models import Models, School, Event, Gymnast, Lineup, LineupEntry, Judge


def get_environment_variable(env_var_name: str) -> str:
    env_var = getenv(env_var_name)
    # print(f"{env_var_name} = {env_var}")  # Debug statement to check if .env is found
    if not env_var:
        raise EnvironmentError(f"Could not find environment variable '{env_var_name}'.")
    return env_var


class DBInterface:
    interface = None

    @classmethod
    def get_interface(cls, path_to_dot_env: str):
        if DBInterface.interface:
            return DBInterface.interface
        else:
            return DBInterface(path_to_dot_env)

    def __init__(self, path_to_dotenv: str | None = None):
        load_dotenv(path_to_dotenv)  # This loads our .env file so that os can use it.
        try:
            self.engine = create_engine(
                URL.create(
                    drivername="mysql",
                    username=get_environment_variable("MYSQL_USER"),
                    password=get_environment_variable("MYSQL_PASSWORD"),
                    host=get_environment_variable("DATABASE_HOST"),
                    database=get_environment_variable("MYSQL_DATABASE"),
                ),
                pool_recycle=3600  # Refresh the connection every hour.
            )
        except EnvironmentError:
            raise EnvironmentError("Could not find the required environment variables. Required Variables:\n\tMYSQL_USER\n\tMYSQL_PASSWORD\n\tDATABASE_HOST\n\tMYSQL_DATABASE")

        self.session = None

        Models.metadata.create_all(self.engine)  # Create the tables in the DB

    def get_session(self) -> Session:
        if self.session is None:
            self.session = Session(self.engine)

        return self.session

    # ----------------------------------------------------------------------------------------------- School Queries ---
    def get_schools(self) -> [School]:
        session = self.get_session()

        select_statement = select(School)

        return list(session.scalars(select_statement))

    def get_school_by_id(self, school_id: int) -> [School]:
        session = self.get_session()
        select_statement = select().where(School.school_id == school_id)
        return list(session.scalars(select_statement))

    def get_school_by_name(self, school_name: str) -> [School]:
        session = self.get_session()
        select_statement = select(School).where(School.school_name == school_name)
        return list(session.scalars(select_statement))

    def get_schools_by_names(self, school_names: [str]) -> [School]:
        session = self.get_session()
        select_statements = session.query(School).filter(School.school_name.in_(school_names))
        return list(session.scalars(select_statements))

    # ------------------------------------------------------------------------------------------------ Event Queries ---
    def get_events(self) -> [Event]:
        session = self.get_session()
        select_statement = select(Event)
        return list(session.scalars(select_statement))

    def get_event_by_id(self, event_id: int) -> [Event]:
        session = self.get_session()
        select_statement = select(Event).where(Event.event_id == event_id)
        return list(session.scalars(select_statement))

    # ---------------------------------------------------------------------------------------------- Gymnast Queries ---
    def get_gymnasts_from_school(self, school: School) -> [Gymnast]:
        session = self.get_session()
        select_statement = select(Gymnast).where(Gymnast.school_id == school.school_id)
        return list(session.scalars(select_statement))

    def get_gymnasts_from_school_id(self, school_id: int) -> [Gymnast]:
        session = self.get_session()
        select_statement = select(Gymnast).where(Gymnast.school_id == school_id)
        return list(session.scalars(select_statement))

    def get_gymnast_by_id(self, gymnast_id: int) -> [Gymnast]:
        session = self.get_session()
        select_statement = select(Gymnast).where(Gymnast.gymnast_id == gymnast_id)
        return list(session.scalars(select_statement))

    def get_gymnast_by_name(self, first_name: str, last_name: str) -> [Gymnast]:
        session = self.get_session()
        select_statement = select(Gymnast).where(Gymnast.first_name == first_name, Gymnast.last_name == last_name)
        return list(session.scalars(select_statement))

    def get_gymnasts_by_names(self, names: list[tuple[str, str]]) -> [Gymnast]:
        session = self.get_session()
        select_statements = union_all(*(
            select(Gymnast).where(Gymnast.first_name == first_name, Gymnast.last_name == last_name)
            for first_name, last_name in names
        ))
        gymnasts_ids = list(session.scalars(select_statements))  # For some reason union_all only returns IDs

        # This select statement will get all the gymnast information.
        select_statements = session.query(Gymnast).filter(Gymnast.gymnast_id.in_(gymnasts_ids))
        return list(session.scalars(select_statements))

    # ----------------------------------------------------------------------------------------------- Lineup Queries ---
    def get_lineups(self) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup)
        return list(session.scalars(select_statement))

    def get_lineup_by_id(self, lineup_id: int) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup).where(Lineup.lineup_id == lineup_id)
        return list(session.scalars(select_statement))

    def get_lineups_by_event_id(self, event_id: int) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup).where(Lineup.event_id == event_id)
        return list(session.scalars(select_statement))

    def get_lineups_by_event(self, event: Event) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup).where(Lineup.event_id == event.event_id)
        return list(session.scalars(select_statement))

    def get_lineups_by_event_and_apparatus(self, event: Event, apparatus_name: str) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup).where(
            Lineup.event_id == event.event_id
        ).where(
            Lineup.apparatus_name == apparatus_name
        )
        return list(session.scalars(select_statement))

    def get_lineups_by_event_and_apparatus_and_school(self, event_id: int, apparatus_name: str, school_id: int) -> [Lineup]:
        session = self.get_session()
        select_statement = select(Lineup).where(
            Lineup.event_id == event_id
        ).where(
            Lineup.apparatus_name == apparatus_name
        ).where(
            Lineup.school_id == school_id
        )
        return list(session.scalars(select_statement))

    # ------------------------------------------------------------------------------------------ LineupEntry Queries ---
    def get_lineup_entries(self) -> [LineupEntry]:
        session = self.get_session()
        select_statement = select(LineupEntry)
        return list(session.scalars(select_statement))

    def get_lineup_entries_from_lineup(self, lineup: Lineup) -> [LineupEntry]:
        session = self.get_session()
        select_statement = select(LineupEntry).where(LineupEntry.lineup_id == lineup.lineup_id)
        return list(session.scalars(select_statement))

    # ------------------------------------------------------------------------------------------------ Judge Queries ---
    def get_judges(self) -> [Judge]:
        session = self.get_session()
        select_statement = select(Judge)
        return list(session.scalars(select_statement))

    def get_judges_by_event(self, event: Event) -> [Judge]:
        session = self.get_session()
        select_statement = select(Judge).where(Judge.event_id == event.event_id)
        return list(session.scalars(select_statement))

    def get_judges_by_event_and_apparatus(self, event: Event, apparatus_name: str) -> [Judge]:
        session = self.get_session()
        select_statement = select(Judge).where(
            Judge.event_id == event.event_id,
            Judge.apparatus_name == apparatus_name
        )
        return list(session.scalars(select_statement))

    # --------------------------------------------------------------------------------------------- Helper Functions ---
    def insert(self, *objects: Models):
        session = self.get_session()
        session.add_all(objects)
        session.commit()

    def delete(self, *objects: Models):
        session = self.get_session()
        for obj in objects:
            session.delete(obj)
        session.commit()
