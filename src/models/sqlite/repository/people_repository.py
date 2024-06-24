from dataclasses import astuple
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.entities.people import PeopleTable, PersonWithoutId
from src.models.sqlite.interfaces.people_repository_interface import PeopleRepositoryInterface

class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(self, person: PersonWithoutId) -> None:
        with self.__db_connection as database:
            try:
                person_data = PeopleTable(**person)
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get_person(self, person_id: int) ->  PeopleTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session.
                        query(PeopleTable).
                        outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id).
                        filter(PeopleTable.id == person_id).
                        with_entities(
                            PeopleTable.last_name,
                            PeopleTable.first_name,

                            PetsTable.type,
                            PetsTable.name.label("pet_name"),
                            PetsTable.name.label("pet_type"),
                        ).
                        one()
                )
                return person
            except NoResultFound:
                return None