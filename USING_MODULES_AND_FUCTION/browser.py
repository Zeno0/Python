import webbrowser

# webbrowser.open("https://myanimelist.com.net")
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"),1)
chrome = webbrowser.get(using="chrome")
chrome.open_new_tab("https://myanimelist.com.net")