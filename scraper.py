from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json

def main():
    with open("wikispeedruns-com-2026-10-31.json") as f:
        data = json.load(f)

    driver = webdriver.Chrome()

    for i in range(len(data)):
        x = data[i]
        driver.get(f"https://wikispeedruns.com/leaderboard/{x['prompt']}?preset=ffa&offset=0")
        
        time.sleep(1) # wait for javascript to fetch and load data

        avg_links, avg_time = driver.find_elements(by=By.CSS_SELECTOR, value=".stat")
        completion_rate = driver.find_element(by=By.CSS_SELECTOR, value=".progress")
        num_runs = driver.find_element(by=By.CSS_SELECTOR, value=".my-1")
        
        if int(num_runs.text[:-11]) != 0: # non-zero number of runs = data has finished loading
            data[i]["average_links"] = float(avg_links.text)
            data[i]["average_time"] = float(avg_time.text[:-1])
            data[i]["completion_rate"] = round(float(completion_rate.text[:-1]) / 100, 10) # convert % into fraction
        else: # data hasn't loaded yet? (or no data)
            time.sleep(1)
            num_runs = driver.find_element(by=By.CSS_SELECTOR, value=".my-1")
            if int(num_runs.text[:-11]) == 0: # really no data
                print(i, data[i]) # flag it, fix manually
            else: # if data has loaded after waiting longer
                avg_links, avg_time = driver.find_elements(by=By.CSS_SELECTOR, value=".stat")
                completion_rate = driver.find_element(by=By.CSS_SELECTOR, value=".progress")
                data[i]["average_links"] = float(avg_links.text)
                data[i]["average_time"] = float(avg_time.text[:-1])
                data[i]["completion_rate"] = float(completion_rate.text[:-1]) / 100

    driver.quit()

    with open('full_data.json', 'w') as f:
        json.dump(data, f)

main()
