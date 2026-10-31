# Wikipedia Speedruns: Archived Dataset

Data collected from [Wikipedia Speedruns](https://wikispeedruns.com/archive) on 31 October, 2026. 

To collect prompt IDs for all past daily challenges, I used a [web scraper Chrome extension](https://chromewebstore.google.com/detail/jnhgnonknehpejjnehehllkliplmbmhn?utm_source=item-share-cb). This provided me with a .csv file that contained the prompt ID, start article, and end article for around 1800 daily challenges.
<img width="100%" alt="Web scraper screenshot" src="https://github.com/user-attachments/assets/2069bf35-df14-419f-9888-0eb77a0f93ab" />

I then used a Selenium script in Python to the scrape statistical data from the [leaderboard page](https://wikispeedruns.com/leaderboard/1899?preset=ffa&offset=0) for each challenge. All data collected was from "First Attempt" mode, to reduce the effect of cheaters looking up the most efficient path. This data, along with the data in the .csv file, is stored in a .json file.

Any missing, erroneous, or buggy data was corrected and checked by me.

## Sample data
```
{
  "prompt": 1,
  "starting_article": "Walt Whitman",
  "ending_article": "Walt Disney",
  "average_links": 8.08,
  "average_time": 185.91,
  "completion_rate": 0.4368
}
```
