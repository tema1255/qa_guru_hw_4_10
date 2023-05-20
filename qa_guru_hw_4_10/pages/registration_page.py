from selene import browser, have, command
from qa_guru_hw_4_10 import resource
from qa_guru_hw_4_10.data.user import User


class RegistrtionPage:

    def open(self):
        browser.open("/automation-practice-form")

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[for^=gender-radio]').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(user.birth_year)
        browser.element('.react-datepicker__month-select').type(user.birth_month)
        browser.element('option[value="3"]').click()
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.driver.execute_script('window.scrollTo(0,300)')
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

        browser.element("#uploadPicture").set_value(resource.path(user.picture))

        browser.element('#currentAddress').perform(
            command.js.set_value(user.current_address)
        )
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, user):
        full_name = user.first_name + ' ' + user.last_name
        date_of_birth = user.birth_day + ' ' + user.birth_month + ',' + user.birth_year
        state_and_city = user.state + ' ' + user.city
        browser.element(".table").all("td").even.should(
            have.texts(
                full_name,
                user.email,
                user.gender,
                user.mobile,
                date_of_birth,
                user.subjects,
                user.hobbies,
                user.picture,
                user.current_address,
                state_and_city,
            )
        )
        return self
