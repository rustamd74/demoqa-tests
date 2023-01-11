from demoqa_tests.model.pages import practice_form


def test_student_registration():
    practice_form.open_page()
    practice_form.submit_data('John', 'Doe', 'johndoe@gmail.com', '2223331110', '221b, Baker street')
    practice_form.select_gender('Male')
    practice_form.date_birthday(day='4', month='2', year='2004')
    practice_form.subject('Computer Science')
    practice_form.set_hobbies('Sports')
    practice_form.insert_picture("resources/python_label.png")
    practice_form.select_state('Uttar Pradesh')
    practice_form.select_city('Lucknow')
    practice_form.submit()

    practice_form.assert_registration_student('John Doe', 'johndoe@gmail.com', 'Male', '2223331110', '04 March,2004',
                                               'Computer Science', 'Sports', 'python_label.png', '221b, Baker street',
                                               'Uttar Pradesh Lucknow')
