from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import  Options
import csv
from bs4 import  BeautifulSoup
import pickle


def formatDate(date):
    months = dict(JAN = "01", FEB="02", MAR="03", APR="04", MAY="05", JUN="06", JUL="07", AUG="08", SEP="09", OCT="10", NOV="11", DEC="12")
    s = date[:3] + months[date[3:6]] + date[6:]
    return s

def authenticateLogin():
    url = "https://secure.housing.ubc.ca/cas/sgw/cwl_auth.home"
    newUrl = ""
    browser = webdriver.Chrome()
    browser.get(url)
    while (newUrl != "https://secure.housing.ubc.ca/cas/sgw/cwl_auth.home"):
        newUrl = browser.current_url;
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
    browser.close()
    start()
def parseTransactions(html):
    soup = BeautifulSoup(html, "html.parser")
    fieldnames = ['date', 'loc', 'lat', 'long', 'amt', 'card']
    date = ""
    amt = ""
    loc = ""
    with open("data.csv", mode='w') as csv_file:
        c = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for foo in soup.find_all('div', attrs={'class': ['row-highlight', '']}):
            fooD = foo.descendants
            # print("foo")
            for d in fooD:
                # print("d")
                if d.name == 'div' and d.get('class', '') == ['item-left']:
                    print(d.text)
                    date = formatDate(d.text)

                if d.name == 'div' and d.get("class", '') == ['item-right']:
                    print(d.text)
                    if d.text[1] == '-':
                        print(d.text[2:])
                        amt = d.text[2:]
                    else:
                        amt = d.text[1:]
                if d.name == 'div' and d.get("class", '') == ['item-comments']:
                    print(d.text)
                    loc = d.text.split("Location: ", 1)[1]
            c.writerow({'date': date, 'amt': amt, 'loc': loc, 'lat': 0,'long' : 0, 'card': "UBC Card"})
def start():
    chromeOP = Options()
    chromeOP.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chromeOP)
    browser.get("https://secure.housing.ubc.ca/cas/sgw/ws_mpvan_plans.accounts?p_action=VIEW_ACCT")

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://secure.housing.ubc.ca/cas/sgw/ws_mpvan_plans.accounts?p_action=VIEW_ACCT")

    browser.find_element_by_xpath(
        "/html/body/div[@class='container']/div[6]/div[@class='content expand']/div[@class='row-fluid expand']/p[5]/a[1]").click()
    dropDown = Select(browser.find_element_by_id("p_start_date"))
    dropDown.select_by_index(11)
    browser.find_element_by_name("SUBMIT").click()
    html = browser.page_source
    parseTransactions(html)

def main():
    authenticateLogin()



main()

