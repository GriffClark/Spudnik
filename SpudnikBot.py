import selenium
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime, timedelta
from enum import Enum
from selenium.webdriver.common.keys import Keys

# driver downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads

startTime = datetime.now()
print(str(startTime))

"""
TODO
Have bot be able to click links on eCommerce sites
Have bot be able to screenshot all ads it sees
"""
# # INTERNET EXPLORER
# PATH = "C:\Program Files (x86)\IEDriverServer.exe"
# driver = webdriver.Ie(PATH) #hoping that using IE will evade bot detection because... you know... its IE


options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {  # TODO why isn't this getting rid of infobar
    "profile.default_content_setting_values.notifications": 1
})
# CHROME
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)
frame = ""


def smooth_scroll():
    default_scroll_value = 800
    # this system of scrolling is meant to simulate how people scroll. We go down towards a specific element,
    target_location = random.randint(get_current_location() + default_scroll_value - 100,
                                     get_current_location() + default_scroll_value + 100) #this is where we want to end up
    scroll_breakup_value = random.randint(10, 50)
    scroll_distance = (target_location - get_current_location()) / scroll_breakup_value
    i = 0
    while i < scroll_breakup_value:
        print(f"\naction " + str(i) + "/" + str(scroll_breakup_value) + " (max)")
        time_sleep_now = random.randint(time_sleep_max / 2, time_sleep_max)
        time.sleep(time_sleep_now / 1000)
        if target_location <= get_current_location():
            break
        else:
            location_history.append(get_current_location())
            driver.execute_script("window.scrollBy(" + str(get_current_location()) + "," + str(
                get_current_location() + scroll_distance) + ")", "")
            print(str(int((get_current_location() / get_document_height()) * 100)) + "% done")
            if check_if_stuck():
                # if we're stuck, break out of the loop and restart
                print("smooth scroll claims to be stuck, but it's notorious for lying")
                break
            else:
                print(f"DEBUG: location history: \n" + str(location_history))
        i += 1


def get_current_location():
    return driver.execute_script("return window.pageYOffset;");


def send_modulated_input(data, path, selectorType):
    # TODO selectorType should be enum
    max_attempts = 5
    for i in range(max_attempts):
        try:
            for x in data:
                if selectorType == 0:
                    driver.find_element_by_xpath(path).send_keys(x)
                elif selectorType == 1:
                    driver.find_element_by_id(path).send_keys(x)
                time.sleep((random.randint(65, 85)) / 1000)
            time.sleep(3)
            break
        except:
            print("failed a login attempt. Sleeping for 5 seconds then trying again")
            time.sleep(5)


def wait_for_webpage_to_load():
    # TODO make this not be a brute force guess
    time.sleep(8)


def log_into_google():
    driver.get("https://www.google.com/")
    driver.find_element_by_xpath("//*[@id=\"gb_70\"]").click()
    send_modulated_input(default_email, "//*[@id=\"identifierId\"]", 0)
    driver.find_element_by_xpath("//*[@id=\"identifierId\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    try:
        send_modulated_input("ea;oiu*&0293%", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                                              "1]/div/form/span/section/div/div/div[""1]/div[1]/div/div/div/div/div[""1]/div/div[1]/input",
                             0)
    except:
        print("failed finding pwd field 1")
        try:
            send_modulated_input("ea;oiu*&0293%", "//*[@id=\"password\"]/div[1]/div/div[1]/input", 0)
        except:
            print("failed finding pwd field 2")
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div["
        "1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(
        Keys.ENTER)
    time.sleep(5)
    global logged_into_google
    logged_into_google = True


def log_into_reddit():
    driver.get("https://www.reddit.com/")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a[1]").click()
    wait_for_webpage_to_load()
    frame = driver.find_element_by_xpath("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[3]/div[2]/div/iframe")
    driver.switch_to.frame(frame)
    send_modulated_input(default_username, "loginUsername", 1)
    send_modulated_input(default_password, "loginPassword", 1)
    driver.find_element_by_id("loginPassword").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()


def log_into_facebook():
    driver.get("https://www.facebook.com/")
    wait_for_webpage_to_load()
    send_modulated_input(default_email, "//*[@id=\"email\"]", 0)
    send_modulated_input(default_password, "//*[@id=\"pass\"]", 0)
    driver.find_element_by_xpath("//*[@id=\"pass\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()


def log_into_facebook_and_instagram():
    driver.get("https://www.instagram.com/")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]").click()
    wait_for_webpage_to_load()
    send_modulated_input(default_email, "//*[@id=\"email\"]", 0)
    send_modulated_input(default_password, "//*[@id=\"pass\"]", 0)
    driver.find_element_by_xpath("//*[@id=\"pass\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()


def check_if_stuck():
    if len(location_history) > 3 and location_history[-1] == location_history[
        -2]:  # first part is there because first few values will often be 0 as the webpage loads
        print("we're stuck :/ This probably means we reached the end of the page")
        return True
    else:
        return False


def get_location_history():
    return location_history


def open_new_window():
    print("DEBUG: dumping old location history...")
    print(get_location_history())
    print("loading in a new page...")
    website_selection = random.choice(website_list)
    driver.get(website_selection)
    print("clearing location history...")
    global location_history
    location_history = []


def scroll_through_social_media(stop_time_input):
    current_social_media_page = social_media_list[random.randint(0, int(len(social_media_list) - 1))]
    driver.get(current_social_media_page)
    wait_for_webpage_to_load()
    start_time_sm = datetime.now()
    stop_time_sm = timedelta(
        seconds=stop_time_input
    )
    elapsed_time = datetime.now() - start_time_sm
    while elapsed_time <= stop_time_sm:
        elapsed_time = datetime.now() - start_time_sm
        smooth_scroll()


def get_document_height():
    try:
        time.sleep(3)
        return driver.execute_script(
            "return document.body.scrollHeight")  # this has to be recalculated as the webpage loads
    except:
        print("couldn't get document height. Defaulting to 500")
        return 500


def screenshot_reddit_add():
    # FIXME finish
    try:
        element = driver.find_element_by_class_name("img_ad")
        eleWidth = element.get_attribute
        driver.get_screenshot_as_png()
    except:
        print("could not take picture of reddit ad")


# INIT

time_sleep_max = 350  # in ms
website_list = [
    "https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001&qp"
    "=parent_operatingsystem_facet%3DOperating%20System~Windows",
    "https://www.bestbuy.com/site/searchpage.jsp?st=macbook&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc"
    "=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys",
    "https://www.bestbuy.com/site/searchpage.jsp?st=chromebook&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page"
    "&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys",
    "https://www.apple.com/mac/?afid=p238%7CstIisv5mW-dc_mtid_1870765e38482_pcrid_434052220943_pgrid_19485452527_&cid"
    "=aos-us-kwgo-mac--slid---product-",
    "https://www.theverge.com/21250695/best-laptops", "https://www.laptopmag.com/reviews/best-laptops-1",
    "https://www.cnet.com/news/best-laptops-of-2020/",
    "https://www.pcmag.com/picks/the-best-laptops",
    "https://www.realclearenergy.org/",
    "http://bright-green.org/2020/06/28/is-bp-really-on-route-to-being-a-net-zero-firm/",
    "https://www.homedepot.com/b/Hardware-Chains-Ropes-Rope/N-5yc1vZc2gr",
    "https://www.homedepot.com/s/wire?NCNI-5",
    "https://www.google.com/chromebook/",
    "https://www.nytimes.com/",
    "https://www.tomsguide.com/best-picks/best-laptops"]

social_media_list = [
    "https://www.reddit.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/"
]

location_history = []
logged_into_reddit = False
logged_into_google = False
num_webpages_visited = 0  # this will be used to track how many webpages we've seen
default_password = "ea;oiu*&0293%"
default_email = "isaacMcCafferty081081@gmail.com"
default_username = "isaacMcCafferty081"

# set up the bot
# log_into_facebook_and_instagram()
# log_into_google()
# log_into_reddit()
scroll_through_social_media(100)

while True:
    # see if we should go to Reddit to view an ad, or if we should go to the interwebs to keep building our user profile
    if num_webpages_visited > 0 and num_webpages_visited % 2 == 0:
        driver.get("https://www.reddit.com/r/popular/")
        # if we aren't logged into reddit, we should do that
        # this assumes that we only have to log into reddit once per session
        time.sleep(10)
    # should go to reddit every ten webpages
    open_new_window()
    num_webpages_visited += 1
    num_scrolls = 0  # resets how many scrolls have been taken on this page
    num_scrolls_to_complete = random.randint(50, 500)  # maximum number of scrolls until we get bored and leave the
    # page, regardless of where we are
    scroll_range_max = get_document_height() / 8  # whats the furthest you can move in one scroll
    # then hang out for a sec
    while num_scrolls < num_scrolls_to_complete:  # until we've scrolled as far as we're going to on this page...
        if get_current_location() >= get_document_height():
            # if you're most of the way through a document that can be far enough
            print("hit the bottom. Restarting this whole kerfluffle over again...")
            break
        else:
            smooth_scroll()
            print("default: scrolled down a bit")
            if check_if_stuck():
                # if we're stuck, break out of the loop and restart
                break
        num_scrolls += 1
        # at this point, we have made a scroll action
        # Now, see if we should click a link on this webpage
        all_links = links = driver.find_elements_by_partial_link_text(
            '')  # many of the things this finds won't be clickable, hence the try/catch block. This is intentional, as it can be used as a way to add randomness to how often we click
        l = links[(random.randint(0, len(links) - 1))]  # this is the link we will try to click
        try:
            l.click()
            time.sleep(3)  # allows time for the webpage to load
            if len(driver.window_handles) > 7:
                driver.close()
        except:
            print("this element isn't clickable :(")

        # sometimes it should switch between tabs
        if num_scrolls % int((random.randint(1, 2)) * 1000) == 0:
            # TODO make this hit way more often
            num_open_windows = len(driver.window_handles)
            try:
                driver.switch_to.window(driver.window_handles[random.randint(num_open_windows)])
            except:
                print("window switcheroo failed")
