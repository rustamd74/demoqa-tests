from selene.support.conditions import have


def select_hobbies(elements, *by_texts):
    for value in by_texts:
        elements.element_by(have.text(value)).click()