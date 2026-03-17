class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

    MAIN_PAGE = BASE_URL + '/'
    LOGIN_PAGE = BASE_URL + '/login'
    REGISTER_USER = BASE_URL + '/api/auth/register'
    DELETE_USER = BASE_URL + '/api/auth/user'
    PROFILE_PAGE = BASE_URL + '/account/profile'
    FORGOT_PASSWORD_PAGE = BASE_URL + '/forgot-password'
    RESET_PASSWORD_PAGE = BASE_URL + '/reset-password'
    ORDERS_HISTORY = BASE_URL + '/account/order-history'
    FEED = BASE_URL + '/feed'


class Text:
    POPUP_TEXT = "Детали ингредиента"
    BUTTON_TEXT = "Войти"