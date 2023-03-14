from selenium.webdriver.common.by import By

driverPathChrome = 'chromedriver.exe'
# url страницы формы авторизации
baseUrl = 'https://b2c.passport.rt.ru'
# название страницы (возможные варианты: Авторизация, Регистрация)
page_title = 'card-container__title'
# страница регистрации
page_reg = 'kc-register'
# страница восстановления пароля
page_forgotPassword = 'h1.card-container__title'
# страница авторизации через социальные сети
page_vk = "oidc_vk"
page_ok = "oidc_ok"
page_mail = "oidc_mail"
page_google = "oidc_google"
page_ya = "oidc_ya"


# таб выбора: телефон, почта, логин, лицевой счет
tabButtonsId = ['t-btn-tab-phone', 't-btn-tab-mail', 't-btn-tab-login', 't-btn-tab-ls']
placeholderInputsId = '.rt-input__placeholder'
placeholderInputsValue = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']
placeholderInputs_pass = 'Пароль'
placeholderInputs_registr = ['Имя', 'Фамилия', 'Регион', 'E-mail или мобильный телефон', 'Пароль', 'Подтверждение пароля']
tabTitles = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
activeTab = 'rt-tab--active'
# поле ввода логина на странице авторизации
login_locator = (By.ID, 'username')
# поле ввода пароля на странице авторизации
pass_locator = (By.ID, 'password')
# кнопка "Войти" на странице авторизации
tab_authoriz = (By.ID, 'kc-login')
# кнопка "Забыл пароль" на странице авторизации
tab_forgotPassword = 'forgot_password'
# картинка капчи на странице восстановления пароля
image_captcha_locator = 'rt-captcha__image'
# кнопка обновления капчи на странице восстановления пароля
tab_refresh_capcha = 'rt-captcha__reload'
# кнопка "Вернуться назад" на странице восстановления пароля
tab_return_back = 'reset-back'
# ссылка на пользовательское соглашение под кнопкой "Войти" на странице авторизации
link_user_locator1 = 'a.rt-link.rt-link--orange[target="_blank"]'
# ссылка на пользовательское соглашение в футере на странице авторизации
link_user_locator2 = 'span.rt-footer-left__item-accent'

# поле ввода имени на странице регистрации
firstName_locator = (By.NAME, 'firstName')
# поле ввода фамилии на странице регистрации
lastName_locator = (By.NAME, 'lastName')
# поле ввода пароля на странице регистрации
pass_locator_reg = (By.CSS_SELECTOR, 'input#password')
# глаз в поле пароля на странице регистрации
password_visibility = 'div.new-password-container>div.rt-input-container.new-password-container__password div.rt-input__action>svg'

registerFormKeysFirstName = ['Ш', 'Пр', '123', '№;"?@%!@#$',
                              '1fM7VWiKLd9ПЙЦAf9DySd91йф1zZenува',
                              'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                               '的一是不了人我在有他这为之大来以个中上们',
                               '|\\/!@#$%^&*()-_=+`~?"№;:[]{}',
                              'Александр']
registerFormKeysLastName = ['Ш', 'Пр', '123', '№;"?@%!@#$',
                            '1fM7VWiKLd9ПЙЦAf9DySd91йф1zZenува',
                            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                            '的一是不了人我在有他这为之大来以个中上们',
                            '|\\/!@#$%^&*()-_=+`~?"№;:[]{}',
                            'Сергеев']
registerFormKeysLogin = ['A', 'Пр', '123', '№;"?@%!@#$',
                           '1fM7VWiKLd9ПЙЦAf9DySd91йф1zZenува',
                           '的一是不了人我在有他这为之大来以个中上们',
                           '9099900015', 'testing@mail.ru']
registerFormPassword = ['Tests&1', 'testTests', 'test&Testы123', 'test&tests123', 'test&Tests123']


sendKeys = ['79998887776', 'test@test.ru', '899988776655', 'TextText']
placeValue = ['Мобильный телефон', 'Электронная почта', 'Лицевой счёт', 'Логин']
tabTitlesAuth = ['Телефон', 'Почта', 'Лицевой счёт', 'Логин']


# ошибки
authorizError = "Неверный логин или пароль"
authorizErrorID = (By.ID, 'form-error-message')
registerErrors_locator = (By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error')
registerErrorsName = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
registerErrorsAddress = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
registerErrorsPasswordConfirm = 'Пароли не совпадают'
registerErrorsPass = 'Длина пароля должна быть не менее 8 символов'



