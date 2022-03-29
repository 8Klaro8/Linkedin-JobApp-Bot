# general imports-------------------------------------------------------------------
import time
import random

# library imports-------------------------------------------------------------------

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from collections import OrderedDict

# start to apply func-------------------------------------------------------------------
def apply_job(input_list):
    for job in input_list:
        driver.get(job)
        driver.implicitly_wait(random_number)
        time.sleep(random_number)

        try:
            apply_button = driver.find_element_by_class_name('jobs-apply-button')
            driver.implicitly_wait(random_number)
            time.sleep(random_number)
            if driver.find_element_by_css_selector('.jobs-apply-button span').text == 'Easy Apply':
                title_of_job = driver.find_element_by_class_name('p5').text.split('\n')[0].lower()
                if 'python' in title_of_job:
                    print('python is in!')
                    apply_button.click()
                    driver.implicitly_wait(random_number)
                    time.sleep(random_number)
                    texT_input = driver.find_element_by_css_selector('.fb-single-line-text__input')
                    texT_input.send_keys('5455464367')
            else:

                driver.implicitly_wait(random_number)
                time.sleep(random_number)
                title_of_job = driver.find_element_by_class_name('p5').text.split('\n')[0].lower()
                print(title_of_job)
                if 'python' in title_of_job:
                    print('python is in!')
                    apply_button.click()
                    #Application is not complete as I dont wish to appy in a way that's not personal -
                    # may change in the future - for now just save.

        except:
            continue

# unsave saved jobs if necessary-------------------------------------------------------------------
def unsave_jobs():
    driver.implicitly_wait(random_number)
    time.sleep(random_number)
    jobs_button = driver.find_element_by_id('ember19')
    jobs_button.click()
    driver.implicitly_wait(random_number)
    time.sleep(random_number)

    my_jobs = driver.find_element_by_class_name('jobs-home-scalable-nav__nav-icon')
    my_jobs.click()
    driver.implicitly_wait(random_number)
    time.sleep(random_number)

    jobs_ul = driver.find_elements_by_class_name('reusable-search__result-container')
    print(len(jobs_ul))

    jobs_link = driver.find_elements_by_css_selector('.reusable-search__entity-result-list .reusable-search__result-'
                                                     'container .entity-result__title-text a')
    list_of_job_links = []
    for each in jobs_link:
        list_of_job_links.append(each.get_attribute('href'))

    for link in list_of_job_links:
        driver.get(link)
        driver.implicitly_wait(random_number)
        time.sleep(random_number)

        try:
            jobs_save_button_innerHTML = driver.find_element_by_css_selector('.jobs-save-button')\
                .get_attribute('innerHTML')
            jobs_save_button = driver.find_element_by_css_selector('.jobs-save-button')

            lines = jobs_save_button_innerHTML.split('\n')
            saved_label = lines[2].strip()
            if saved_label:
                jobs_save_button.click()
                driver.implicitly_wait(random_number)
                time.sleep(random_number)

        except:
            continue
    # False trials-------------------------------------------------------------------

    # driver.implicitly_wait(random_number)
    # time.sleep(random_number)

    # ActionChains(driver).move_to_element(job_items).key_down(Keys.COMMAND).click(job_items).key_up(Keys.COMMAND).perform()

# saving preferred jobs-------------------------------------------------------------------
def save_jobs(list_of_job_links):
    # False trials-------------------------------------------------------------------
    # job_links = driver.find_elements_by_css_selector('.jobs-search-results__list-item a')
    # list_of_job_links = []
    # for job_link in job_links:
    #     list_of_job_links.append(job_link.get_attribute('href'))


    for job in list_of_job_links:
        driver.get(job)
        driver.implicitly_wait(random_number)
        time.sleep(random_number)
        try:
            jobs_save_button_innerHTML = driver.find_element_by_css_selector('.jobs-save-button').get_attribute('innerHTML')
            jobs_save_button = driver.find_element_by_css_selector('.jobs-save-button')

            driver.implicitly_wait(random_number)
            time.sleep(random_number)

            lines = jobs_save_button_innerHTML.split('\n')
            saved_label = lines[2].strip()
            print(saved_label)
            if saved_label == 'Save':
                driver.implicitly_wait(random_number)
                time.sleep(random_number)
                jobs_save_button.click()
                driver.implicitly_wait(random_number)
                time.sleep(random_number)

            elif saved_label == 'Saved':
                print('saved')
                continue
            else:
                continue
        except:
            continue


    # False trials-------------------------------------------------------------------
    # for link in job_links:
        # link.click()
        # driver.implicitly_wait(random_number)
        # time.sleep(random_number)
        # jobs_save_button = driver.find_element_by_class_name('jobs-save-button')
        # jobs_save_button.click()
        # driver.implicitly_wait(random_number)
        # time.sleep(random_number)

# setup-------------------------------------------------------------------
random_number = random.randint(1,3)

path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(path)
action = ActionChains(driver)


LINKEDIN_LINK = "https://www.linkedin.com/jobs/search/?keywords=python"
driver.get(LINKEDIN_LINK)
driver.implicitly_wait(2)
time.sleep(2)


# sign in-------------------------------------------------------------------
def sign_in():
    try:
        sign_in_button = driver.find_element_by_xpath('/html/body/div[5]/a[1]')
        sign_in_button.click()
        driver.implicitly_wait(random_number)
        time.sleep(random_number)
    except:
        # driver.quit()
        driver.implicitly_wait(random_number)
        time.sleep(random_number)
        driver.get(LINKEDIN_LINK)
        driver.implicitly_wait(random_number)
        time.sleep(random_number)
sign_in()

email = driver.find_element_by_xpath('/html/body/div/main/div[3]/div[1]/form/div[1]/input')
email.send_keys('hubokjaros@gmail.com')
driver.implicitly_wait(random_number)
time.sleep(random_number)

passw = driver.find_element_by_xpath('/html/body/div/main/div[3]/div[1]/form/div[2]/input')
passw.send_keys('ya>xs#cd&')
driver.implicitly_wait(random_number)
time.sleep(random_number)



passw.send_keys(Keys.RETURN)
driver.implicitly_wait(random_number)
time.sleep(random_number)

driver.maximize_window()
driver.implicitly_wait(random_number)
time.sleep(random_number)

# unsave_jobs()
# save_jobs()
# three_dots = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[9]/button')
three_dots = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[2]')


per_page = 1
elemnts_counter  = ''


# Scroll function-------------------------------------------------------------------
def scroll():
    global elemnts_counter
    # job_links = driver.find_elements_by_css_selector('.jobs-search-results__list-item a')
    # last_web_element = ''
    # for each in job_links:
    #     last_web_element = each


    links_per_page = len(element_links) / per_page
    print(links_per_page)
    while links_per_page < 24 :
        last_webelement.send_keys(Keys.PAGE_DOWN)
        collect_links()

    print(element_links)
    print(len(element_links))

    if current + 1 == 1:
        print('colected 1 pages!')

        apply_job(element_links)

    click_next_page()


job_titles = driver.find_elements_by_class_name('jobs-search-results__list-item')
job_list = driver.find_elements_by_class_name('job-card-list__footer-wrapper')
jobs = driver.find_elements_by_class_name('jobs-search-results__list')

last_webelement = ''
previous_link = ''


# Get wanted links-------------------------------------------------------------------
def collect_links():
    global last_webelement, elemnts_counter, is_new_element
    global previous_link
    job_links = driver.find_elements_by_css_selector('.jobs-search-results__list-item a')

    for job_link in job_links:
        my_link = job_link.get_attribute('href')
        if previous_link == my_link:
            continue
        elif 'https://www.linkedin.com/company' in my_link:
            continue
        elif my_link not in element_links:
                element_links.append(my_link)

        previous_link = my_link
        last_webelement = job_link

    driver.implicitly_wait(random_number)
    time.sleep(random_number)

    scroll()

current = 0


# Continue to next page-------------------------------------------------------------------
def click_next_page():
    global current, is_new_element, per_page, new_page


    list_of_page_numbers = driver.find_elements_by_class_name('artdeco-pagination__indicator')
    ul_numbers_move_to = driver.find_element_by_class_name('premium-upsell-link')

    action.move_to_element(ul_numbers_move_to)
    driver.implicitly_wait(random_number)
    time.sleep(random_number)

    page_numbers = []
    for each in list_of_page_numbers:
        page_numbers.append(each)


    page_numbers[current + 1].click()
    per_page += 1
    current += 1
    print(f'currnet page number: {current + 1}')

    collect_links()


element_links = []


# Control if links are proper-------------------------------------------------------------------
def print_job_links():
    driver.implicitly_wait(random_number)
    time.sleep(random_number)

    collect_links()
    # scroll()
    print(element_links)
    print(len(element_links))

    # False trials-------------------------------------------------------------------
    # if len(element_links) < 25:
    #     driver.implicitly_wait(random_number)
    #     time.sleep(random_number)
    #
    #     click_next_page()
    #
    #     driver.implicitly_wait(random_number)
    #     time.sleep(random_number)
    #
    #     print_job_links()


try:
    print_job_links()
except:
    print('exited')


# False trials-------------------------------------------------------------------

# left_rail = driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]')
# driver.implicitly_wait(random_number)
# time.sleep(random_number)
# left_rail.send_keys(Keys.PAGE_DOWN)

















# False trials-------------------------------------------------------------------

# list_of_job_links = {}
# for job_link in job_links:
#     count += 1
#     list_of_job_links[count] = job_link.get_attribute('href')
#
#
# necessary_links = []
# previous_value = ''
# for key, value in list_of_job_links.items():
#     if value == previous_value:
#         continue
#     elif 'https://www.linkedin.com/company' in value:
#         continue
#     else:
#         necessary_links.append(value)
#     previous_value = value
#
# last_link = necessary_links[-1]
# action.move_to_element(last_link)