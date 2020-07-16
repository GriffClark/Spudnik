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

# TODO steps to problem definition:
# 1. take screenshots of ads
# 2. crop screenshots
# 3. scrape ads for category/content
# 4. build dashboard to see what ads are being seen relative to time and location
# 5. create more natural web presence
# deal with pop-up windows
# 6. create more natural social media presense
# 7. create bot that interacts with a browser exactly like a person would - with a mouse that moves around and clicks on elements
# 8. figure out how to create multiple google accounts
# 9. let the beasts loose upon the internet, and make sure they're getting ads for laptops
# 10. figure out how to buy laptops without spending money, in bulk
# 11. see if ads change after purchase


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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class AdWebsite:
    def __init__(self, url):
        self.url = url

    # Love Python variable declarations...
    xpath = ""
    y_location = ""
    id = ""

    def intelligent_screenshot_ad(self):
        # TODO finish method. Ads might be able to be identified by capturing web traffic with Wireshark and loading
        #  just the ad URL
        driver.get(self.url)
        wait_for_webpage_to_load()
        if len(self.xpath) > 0:
            # this means an xpath was set
            driver.executeScript("arguments[0].scrollIntoView(true);", self.xpath)
            print("pretend like we took a screenshot")

    def dumb_screenshot_ad(self):
        driver.get(self.url)
        wait_for_webpage_to_load()
        take_screenshot(self.url)


def smooth_scroll():
    # this method is designed to confuse any detection software looking for continuous scroll patterns
    default_scroll_distance = 800
    # this system of scrolling is meant to simulate how people scroll. We go down towards a specific element,

    if location_history.size() <= 0:
        location_history.push(0)

    target_location = random.randint(int(location_history.peek()),
                                     int(location_history.peek()) + default_scroll_distance)  # this
    # is where we want to end up

    counter = 0
    steps = 150
    while counter < steps:  # don't care if we get stuck here or not
        time_sleep_max = 115
        time_sleep_now = random.randint(int(time_sleep_max / 2), time_sleep_max)
        time.sleep(time_sleep_now / 1000)
        if target_location <= get_y_offset():
            break
        else:
            driver.execute_script(
                "window.scrollBy(" + str(location_history.pop()) + "," + str(target_location / steps) + ")", "")
            location_history.push(get_y_offset())
            # print(str(location_history.peek()) + "px" + "/" + str(get_document_height()) + "px " + str(datetime.now()))
        counter += 1
        if check_if_stuck():
            break;


def get_y_offset():
    return int(driver.execute_script("return window.pageYOffset;"))


def send_modulated_input(data, path, selectorType):
    max_attempts = 5
    for i in range(max_attempts):
        try:
            for x in data:
                if selectorType == "xpath":
                    driver.find_element_by_xpath(path).send_keys(x)
                elif selectorType == "id":
                    driver.find_element_by_id(path).send_keys(x)
                time.sleep((random.randint(60, 175)) / 1000)
            time.sleep(3)
            break
        except:
            print("failed a login attempt. Sleeping for 5 seconds then trying again")
            time.sleep(5)


def wait_for_webpage_to_load():
    # TODO make this not be a brute force guess
    time.sleep(8)


def log_into_amazon():
    # every login attempt gets flagged as suspicious activity, so we're going to have to get creative...
    # this has to be run on a box with a custom chrome profile
    driver.get("https://www.amazon.com")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/div/span").click()
    wait_for_webpage_to_load()
    send_modulated_input(default_email, "//*[@id=\"ap_email\"]", "xpath")
    driver.find_element_by_xpath("//*[@id=\"ap_email\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    send_modulated_input(default_password, "//*[@id=\"ap_password\"]", "xpath")
    driver.find_element_by_xpath("//*[@id=\"ap_password\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    print("logged into amazon")


def log_into_google():
    driver.get("https://www.google.com/")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath("//*[@id=\"gb_70\"]").click()
    send_modulated_input(default_email, "//*[@id=\"identifierId\"]", "xpath")
    driver.find_element_by_xpath("//*[@id=\"identifierId\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    try:
        send_modulated_input("ea;oiu*&0293%", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                                              "1]/div/form/span/section/div/div/div[""1]/div[1]/div/div/div/div/div[""1]/div/div[1]/input",
                             "xpath")
    except:
        print("failed finding pwd field 1")
        try:
            send_modulated_input("ea;oiu*&0293%", "//*[@id=\"password\"]/div[1]/div/div[1]/input", "xpath")
        except:
            print("failed finding pwd field 2")
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div["
        "1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(
        Keys.ENTER)
    time.sleep(5)
    global logged_into_google
    logged_into_google = True
    print("logged into Google")


def log_into_reddit():
    driver.get("https://www.reddit.com/")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a[1]").click()
    wait_for_webpage_to_load()
    frame = driver.find_element_by_xpath("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[3]/div[2]/div/iframe")
    driver.switch_to.frame(frame)
    send_modulated_input(default_username, "loginUsername", "id")
    send_modulated_input(default_password, "loginPassword", "id")
    driver.find_element_by_id("loginPassword").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    print("logged into Reddit")


def log_into_facebook_and_instagram():
    driver.get("https://www.instagram.com/")
    wait_for_webpage_to_load()
    driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]").click()
    wait_for_webpage_to_load()
    send_modulated_input(default_email, "//*[@id=\"email\"]", "xpath")
    send_modulated_input(default_password, "//*[@id=\"pass\"]", "xpath")
    driver.find_element_by_xpath("//*[@id=\"pass\"]").send_keys(Keys.ENTER)
    wait_for_webpage_to_load()
    print("logged into Instagram, and Facebook by extension")


def check_if_stuck():
    if location_history.size() > 3 and location_history.items[0] == location_history.items[1]:
        # first part is there because first few values will often be 0 as the webpage loads
        print("we're stuck :/ This probably means we reached the end of the page")
        return True
    else:
        return False


def get_location_history():
    return location_history


def open_new_window():
    # print("DEBUG: dumping old location history...")
    # print(get_location_history().items)
    website_selection = random.choice(website_list)
    driver.get(website_selection)
    print("Going to " + website_selection)
    global location_history
    location_history = Stack()
    location_history.push(0)


def scroll_through_social_media(stop_time_input):
    """
    TODO Need to interact with social media sites more organically. This will entail...
    1) clicking on posts and
    following links
    2) chatting with other social media accounts
    3) following and unfollowing new pages (can probably
    use suggested)
    4) making posts. Need to have posts include pictures of the same person, but be unique. Maybe
    scrape other people's posts but change some elements to make them unique? Find/build a face generator and
    super-impose the faces onto other photos?
    5) organically commenting on other people's posts
    """
    current_social_media_page = social_media_list[random.randint(0, int(len(social_media_list) - 1))]
    driver.get(current_social_media_page)
    print("Going to spend " + str(stop_time_input) + "s scrolling through " + str(current_social_media_page))
    wait_for_webpage_to_load()
    stop_time_sm = get_elapsed_time() + timedelta(
        seconds=stop_time_input
    )
    while get_elapsed_time() <= stop_time_sm:
        if check_if_stuck() is True:
            break
        else:
            smooth_scroll()
            take_screenshot(current_social_media_page)
            look_at_post_time = random.randint(3, 15)
            print("looking at a post for " + str(look_at_post_time) + "s")
            time.sleep(look_at_post_time)


def get_document_height():
    try:
        return driver.execute_script(
            "return document.body.scrollHeight")  # this has to be recalculated as the webpage loads
    except:
        print("couldn't get document height. Defaulting to 500")
        return 500


default_file_location = "C:\\Users\\gclar\\PycharmProjects\\Spudnik\\Screenshots\\"  # TODO this is a bad


def build_ad_websites():
    # manually compiled list of personalized ads and where to find them
    global ad_website_list
    cafe_mom = AdWebsite("https://thestir.cafemom.com/parenting_news/226166/target-black-owned-badge")
    cafe_mom.xpath = "//*[@id=\"adContainer\"]"
    ad_website_list.append(cafe_mom)


def take_screenshot(current_web_url):
    split_url = current_web_url.split('/')
    raw_datetime_array = str(datetime.now()).split()
    raw_datetime = raw_datetime_array[1] + "_" + raw_datetime_array[0]
    sanitized_datetime_array = raw_datetime.split(':')
    sanitized_seconds = sanitized_datetime_array[2].split('.')[0]
    sanitized_datetime = sanitized_datetime_array[0] + sanitized_datetime_array[1] + sanitized_seconds

    # files are named *website@hhmmss.png*
    sanitized_url = split_url[2] + "@" + str(sanitized_datetime)  # this line ultimately dictates file naming format

    print("screenshot saved to " + str(sanitized_url) + ".png")
    driver.save_screenshot(default_file_location + str(sanitized_url) + ".png")


def gather_ad_data():
    # go to a few pre-defined webpages, takes pictures of ads in know locations
    return -1


# INIT

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

ad_website_list = []

location_history = Stack()
location_history.push(0)
logged_into_reddit = False
logged_into_google = False
num_webpages_visited = 0  # this will be used to track how many webpages we've seen
default_password = "ea;oiu*&0293%"
default_email = "isaacMcCafferty081081@gmail.com"
default_username = "isaacMcCafferty081"

# set up the bot
build_ad_websites()
log_into_google()
# log_into_amazon() # this needs its own machine to work. Amazon's good
log_into_facebook_and_instagram()
log_into_reddit()


def get_elapsed_time():
    return (datetime.now() - startTime)


last_visit_time = datetime.now()
while True:
    open_new_window()  # need to open a webpage to get started
    # see if we should go to Reddit to view an ad, or if we should go to the interwebs to keep building our user profile
    print("T+: " + str(get_elapsed_time().seconds) + "s")
    if num_webpages_visited > 0 and num_webpages_visited % 7 == 0:
        scroll_through_social_media(random.randint(10, 50))
        last_visit_time = datetime.now()
    else:
        num_scrolls_to_complete = random.randint(50, 500)  # maximum number of scrolls until we get bored and leave the
        if int(random.randint(0, 9)) == 4:  # 10% chance of opening new webpage
            print("opening new webpage")
            open_new_window()
        elif get_y_offset() >= get_document_height():
            # if you're most of the way through a document that can be far enough
            print("hit the bottom. Restarting this whole kerfluffle again... *sigh*")
            break
        else:
            i = 0
            while i < num_scrolls_to_complete:
                smooth_scroll()
                print("scrolled down a bit " + str(datetime.now()))
                if check_if_stuck():
                    # if we're stuck, break out of the loop and restart
                    print("Stuck?: " + str(check_if_stuck()))
                    break
                i += 1
    # after every iteration, see where we're at with ads
    for element in ad_website_list:
        element.dumb_screenshot_ad()
    # at this point, we have made a scroll action
    # Now, see if we should click a link on this webpage
    all_links = links = driver.find_elements_by_partial_link_text(
        '')  # many of the things this finds won't be clickable, hence the try/catch block. This is intentional,
    # as it can be used as a way to add randomness to how often we click
    l = links[(random.randint(0, len(links) - 1))]  # this is the link we will try to click
    try:
        l.click()
        time.sleep(3)  # allows time for the webpage to load
        driver.switch_to.window(driver.window_handles[random.randint(0, len(driver.window_handles) - 1)])
        if len(driver.window_handles) > 7:
            driver.close()
    except:
        print("error clicking element " + str(l.tag_name))

    # sometimes it should switch between tabs TODO this isn't working
    if int(random.randint(0,
                          9)) == 4:  # TODO turn this and the other identical line into chance_to_perform_operation(probability)
        # it may be beneficial to have this hit more often, but not sure how much it affects anything
        num_open_windows = len(driver.window_handles)
        try:
            driver.switch_to.window(driver.window_handles[random.randint(num_open_windows)])
        except:
            print("window switcheroo failed")
