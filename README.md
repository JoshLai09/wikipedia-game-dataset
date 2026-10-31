# Wikipedia Speedruns: Archived Dataset

This dataset contains the average statistics for around 1800 rounds of [the Wikipedia Game](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game). Each round was played hundreds of times by users online.
Data collected from [Wikipedia Speedruns](https://wikispeedruns.com/archive) on 31 October, 2026. 

## Sample data
```
[
  ...
  {
    "prompt": 1899,
    "starting_article": "Peru",
    "ending_article": "Paper",
    "average_links": 6.7,
    "average_time": 213.57,
    "completion_rate": 0.7803
  },
  ...
]
```

## Process
To collect prompt IDs for all past daily challenges, I used a [web scraper Chrome extension](https://chromewebstore.google.com/detail/jnhgnonknehpejjnehehllkliplmbmhn?utm_source=item-share-cb) to scrape the Daily Challenge Archive page. This provided me with a [.csv file](wikispeedruns-com-2026-10-31.csv) that contained the prompt ID, start article, and end article for around 1800 daily challenges.
<img width="100%" alt="Web scraper screenshot" src="https://github.com/user-attachments/assets/2069bf35-df14-419f-9888-0eb77a0f93ab" />

I then used a [Selenium script](scraper.py) in Python to the scrape statistical data from the public [leaderboard page](https://wikispeedruns.com/leaderboard/1899?preset=ffa&offset=0) for each challenge. All data collected was from "First Attempt" mode, to reduce the effect of cheaters looking up the most efficient path. This data, along with the data in the .csv file, is stored in a [.json file](full_data.json).

Any missing, erroneous, or buggy data was corrected and checked manually.

### Notes
what the website calls "Avg. # of Clicks" includes the starting page, meaning it represents the average number of nodes and not average number of links.

E.g. for the path "Peru → Chronicle → Newspaper → Paper":
- \# of clicks = 4
- \# of nodes = 4
- \# of links/edges = 3
