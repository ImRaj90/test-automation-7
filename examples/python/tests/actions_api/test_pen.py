import math

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_PEN
from selenium.webdriver.common.by import By


def test_use_pen(driver):
    driver.get('https://www.selenium.dev/selenium/web/pointerActionsPage.html')

    pointer_area = driver.find_element(By.ID, "pointerArea")
    action = ActionBuilder(driver)
    action.add_pointer_input(POINTER_PEN, "default pen")
    action.pointer_action\
        .move_to(pointer_area)\
        .pointer_down(0)
    action.pointer_action\
        .move_by(2, 2)\
        .pointer_up(0)
    action.perform()

    moves = driver.find_elements(By.CLASS_NAME, "pointermove")
    move_to = properties(moves[0])
    down = properties(driver.find_element(By.CLASS_NAME, "pointerdown"))
    move_by = properties(moves[1])
    up = properties(driver.find_element(By.CLASS_NAME, "pointerup"))

    rect = pointer_area.rect
    center_x = rect["x"] + rect["width"] / 2
    center_y = rect["y"] + rect["height"] / 2

    assert move_to["button"] == "-1"
    assert move_to["pageX"] == str(math.floor(center_x))
    assert move_to["pageY"] == str(math.floor(center_y))
    assert down["button"] == "0"
    assert down["pageX"] == str(math.floor(center_x))
    assert down["pageY"] == str(math.floor(center_y))
    assert move_by["button"] == "-1"
    assert move_by["pageX"] == str(math.floor(center_x + 2))
    assert move_by["pageY"] == str(math.floor(center_y + 2))
    assert up["button"] == "0"
    assert up["pageX"] == str(math.floor(center_x + 2))
    assert up["pageY"] == str(math.floor(center_y + 2))


def properties(element):
    kv = element.text.split(' ', 1)[1].split(', ')
    return {x[0]:x[1] for x in list(map(lambda item: item.split(': '), kv))}


