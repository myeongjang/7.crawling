def hover(browser, xpath):
    element_to_hover_over = browser.find_element_by_xpath(xpath)
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()

hover(driver,'//*[@id="webNavi"]/li[4]/a') #목차1