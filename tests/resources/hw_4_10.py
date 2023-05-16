from qa_guru_hw_4_10.data.user import User
from qa_guru_hw_4_10.pages.registration_page import RegistrtionPage


def test_student_registration_form():
    registration_page = RegistrtionPage()

    artem = User(
        first_name="Artem",
        last_name="Chekanov",
        email="tema-42@mail.ru",
        gender="Male",
        mobile="9876543210",
        birth_year="1987",
        birth_month="April",
        birth_day="02",
        subjects="Math",
        hobbies='Sports, Music',
        picture="0.jpeg",
        current_address="До востребования!",
        state="Haryana",
        city="Karnal",
    )
    registration_page.open()
    registration_page.register(artem)
    registration_page.should_have_registered(artem)

