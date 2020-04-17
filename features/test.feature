Feature: Search in Yandex

Scenario: Test yandex search

  Given website "yandex.ru"
  Then check if search field element exist
  When type text in search field "тензор"
  Then check if suggestion table element exist
  When press ENTER to search field
  Then check if first result is "tensor.ru"

Scenario: Test yandex images

  Given site "yandex.ru"
  When check if images link exist
  Then click on images link
  When url is "https://yandex.ru/images/"
  Then click on the first image
  Then check image and right nav button
  Then click right nav button to switch img and check if imgs are different
  Then click left nav button to switch on the previous img and check if this is the previous img