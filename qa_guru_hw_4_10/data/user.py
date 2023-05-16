import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birth_year: str
    birth_month: str
    birth_day: str
    subjects: str
    hobbies: str
    current_address: str
    picture: str
    state: str
    city: str


