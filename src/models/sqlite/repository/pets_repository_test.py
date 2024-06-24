from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock 

from .pets_repository import PetsRepository
from src.models.sqlite.entities.pets import PetsTable


class MockConnection():
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)], # Query
                    [
                        PetsTable(name="cat", type="gato"),
                        PetsTable(name="dog", type="cachorro"),
                        PetsTable(name="horse", type="cavalo"),
                    ]  # Resultado

                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult():
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_so_result_found

    def __raise_so_result_found(self, *args, **kwargs):
        raise NoResultFound('No result found')

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    # mock_connection.session.filter.assert_not_called()

    assert response[0].name == "cat"

def test_list_pets_no_results():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable) # Quando da erro ele para na query
    mock_connection.session.all.assert_not_called()

    assert response == []

def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("dog")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "dog")
    mock_connection.session.delete.assert_called_once()

def test_delete_pets_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("petName")

    mock_connection.session.rollback.assert_called_once()

    