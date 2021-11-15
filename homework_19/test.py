def test_return_saved_cookies(dashboard):
    print(dashboard.cookies.return_webdriver_cookies())


def test_return_local_storage(dashboard):
    print(dashboard.local_storage.return_webdriver_local_storage())
