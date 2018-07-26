from selenium import webdriver

Instance = None

def Initialize():
    global Instance
    options = webdriver.FirefoxOptions()
    # set headless mode on
    options.set_headless(True)
    Instance = webdriver.Firefox(options = options)
    #Instance.implicitly_wait(5)
    return Instance

def CloseDriver():
    global Instance
    Instance.quit()