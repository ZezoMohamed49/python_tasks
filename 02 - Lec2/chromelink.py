
import webbrowser

links = [r'facebook.com',r'google.com',r'linkedin.com']

def open_link(link):
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open(link)
    
