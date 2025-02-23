# HackScraper

**HackScraper** is a Python-based web scraper that fetches and ranks the top stories from [Hacker News](https://news.ycombinator.com/) based on user-defined vote thresholds. It allows users to specify the number of pages to scrape and saves the results to a file if needed.

## Features
- Scrapes top stories from Hacker News
- Allows user input for:
  - Number of pages to scrape
  - Minimum vote threshold
- Ranks stories based on vote count (descending order)
- Saves results to a text file if the user chooses

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed along with the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage
Run the script and follow the on-screen prompts:
```bash
python hackscraper.py
```

### Example Interaction:
```
Enter the number of pages to scrape (default: 2): 1
Enter the minimum vote threshold (default: 100): 50

Fetching news... Please wait...

Top Hacker News Articles:

1. OpenAI announces GPT-5 release (150 votes)
   Link: https://openai.com/gpt-5

2. New Linux Kernel 6.7 released with performance improvements (120 votes)
   Link: https://linuxnews.org/kernel-6.7

Do you want to save the results to a file? (yes/no): yes

Results saved to output.txt
```

### Viewing Saved Results
To view the saved results in Windows Command Prompt:
```bash
type output.txt
```
Or on Linux/macOS:
```bash
cat output.txt
```

## File Structure
```
HackScraper/
│── .gitignore
│── LICENSE
│── HackScraper.py   # Main script
│── README.md    # Project documentation
│── output.txt   # (Optional) File where results are saved

```

---
**Developed by Aditya Bhatt** 🚀

