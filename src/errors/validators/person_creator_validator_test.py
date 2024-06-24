from src.errors.validators.person_creator_validator import person_creator_validator 

class MockRequest:
    def __init__(self,body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "age": 88,
        "pet_id": 7,
        "last_name":"deTal4",
        "first_name":"Fulano",
    })
    
    person_creator_validator(request)