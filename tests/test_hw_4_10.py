from qa_guru_hw_4_10.pages.registration_page import RegistrtionPage


def test_student_registration_form(browser_setup):
    registration_page = RegistrtionPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name("Artem")\
        .fill_last_name("Chekanov")\
        .fill_email("tema-42@mail.ru")\
        .fill_gender("Male")\
        .fill_mobile("9876543210")\
        .fill_date_of_birth("1987", "April", "02")\
        .fill_subjects("math", "eng")\
        .scroll_to("window.scrollTo(0,300)")\
        .fill_hobbies()\
        .upload_picture()\
        .fill_current_address("До востребования!")\
        .fill_state("Haryana")\
        .fill_city("Karnal")\
        .submit()

    # THEN
    registration_page.should_have_registered_user_with(
        "Artem Chekanov",
        "tema-42@mail.ru",
        "Male",
        "9876543210",
        "02 April,1987",
        "Maths, English",
        "Sports, Music",
        "0.jpeg",
        "До востребования!",
        "Haryana Karnal",
    )


