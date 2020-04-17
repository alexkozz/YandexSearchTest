from behave import *
from yapages import YaPages

yandexPage = YaPages()

@given('website "{url}"')
def step(context, url):
    yandexPage.open_site()

@then('check if search field element exist')
def step(context):
    context.search_field = yandexPage.get_search_field()

@when('type text in search field "{text}"')
def step(context, text):
    yandexPage.enter_word(context.search_field, text)

@then('check if suggestion table element exist')
def step(context):
    yandexPage.check_suggestion_table()

@when('press ENTER to search field')
def step(context):
    yandexPage.press_enter(context.search_field)

@then('check if first result is "{text}"')
def step(context, text):
    yandexPage.check_first_result(text)





@given('site "yandex.ru"')
def step(context):
    yandexPage.open_site()

@when('check if images link exist')
def step(context):
    context.images_btn = yandexPage.get_images_btn()

@then('click on images link')
def step(context):
    context.images_btn.click()
    yandexPage.close_tab()

@When('url is "{link}"')
def step(context, link):
    yandexPage.check_url(link)

@Then('click on the first image')
def step(context):
    yandexPage.click_first_image_min()

@Then('check image and right nav button')
def step(context):
    context.nav_right = yandexPage.get_nav_right()
    context.img_element = yandexPage.get_image()
    context.src1 = context.img_element.get_attribute('src')

@Then('click right nav button to switch img and check if imgs are different')
def step(context):
    context.nav_right.click()
    context.src2 = yandexPage.get_next_image_src(context.img_element, context.src1)
    yandexPage.img_not_equal(context.src1, context.src2)
    context.nav_left = yandexPage.get_nav_left()

@Then('click left nav button to switch on the previous img and check if this is the previous img')
def step(context):
    context.nav_left.click()
    context.src3 = yandexPage.get_next_image_src(context.img_element, context.src2)
    yandexPage.img_equal(context.src1, context.src3)
