from selene.support.conditions import have


def select_value(elements, text):
    elements.element_by(have.value(text)).element('..').click()