from selene import browser, have, command
from qa_guru_hw_4_10 import resource


class RegistrtionPage:

    def open(self):
        browser.config.window_width = 1280
        browser.config.window_height = 768
        browser.config.hold_browser_open = True
        browser.open("https://demoqa.com/automation-practice-form")
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(".react-datepicker__month-select").type(month)
        browser.element('option[value="3"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_gender(self, value):
        browser.all("[for^=gender-radio]").element_by(have.text(value)).click()
        return self

    def fill_mobile(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_subjects(self, math_value, eng_value):
        browser.element("#subjectsInput").type(math_value).press_enter().type(
            eng_value
        ).press_enter()
        return self

    def scroll_to(self, value):
        browser.driver.execute_script(value)
        return self

    def fill_hobbies(self):
        browser.element("[for=hobbies-checkbox-1]").click()
        browser.element("[for=hobbies-checkbox-3]").click()
        return self

    def upload_picture(self):
        browser.element("#uploadPicture").set_value(resource.path('0.jpeg'))
        return self

    def fill_current_address(self, value):
        browser.element("#currentAddress").perform(
            command.js.set_value(value)
        )
        return self

    def fill_state(self, value):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    def fill_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        browser.element("#submit").perform(command.js.click)
        return self

    def should_have_registered_user_with(
            self,
            full_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_and_city,
    ):
        browser.element(".table").all("td").even.should(
            have.texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city,
            )
        )
        return self
