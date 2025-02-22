import requests
from bs4 import BeautifulSoup

# Function to fetch Hacker News articles from multiple pages
def fetch_hackernews_pages(pages=2):
    mega_links, mega_subtext = [], []

    for page in range(1, pages + 1):
        try:
            res = requests.get(f"https://news.ycombinator.com/news?p={page}", timeout=10)
            res.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            continue  # Skip this page and move to the next

        soup = BeautifulSoup(res.text, "html.parser")
        mega_links.extend(soup.select(".titleline"))  # Extracts news titles
        mega_subtext.extend(soup.select(".subtext"))  # Extracts vote counts

    return mega_links, mega_subtext

# Function to extract news articles with votes above the threshold
def extract_news(links, subtexts, min_votes=100):
    hn = []

    for idx, item in enumerate(links):
        title = item.get_text(strip=True)  # Extracts the title text
        href = item.find('a')['href'] if item.find('a') else "No Link"  # Gets the link

        vote_tag = subtexts[idx].select_one(".score")  # Extracts vote count
        points = int(vote_tag.get_text().replace(" points", "")) if vote_tag else 0

        if points >= min_votes:  # Filters articles based on vote count
            hn.append({"Title": title, "Link": href, "Votes": points})

    return sorted(hn, key=lambda k: k["Votes"], reverse=True)  # Sorts by votes (descending)

# Function to display news articles
def display_news(news_list):
    for idx, news in enumerate(news_list, start=1):
        print(f"{idx}. {news['Title']} ({news['Votes']} votes)")
        print(f"   🔗 {news['Link']}\n")

# Function to save extracted news data to a file
def save_to_file(news_list, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for idx, news in enumerate(news_list, start=1):
            f.write(f"{idx}. {news['Title']} ({news['Votes']} votes)\n")
            f.write(f"   🔗 {news['Link']}\n\n")
    print(f"\n✅ Results saved to {filename}")

# Function to handle user input for pages and vote threshold
def get_user_input():
    while True:
        try:
            pages = int(input("Enter the number of pages to scrape (default: 2): ") or 2)
            min_votes = int(input("Enter the minimum vote threshold (default: 100): ") or 100)
            return pages, min_votes
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Main function to run the scraper
def main():
    pages, min_votes = get_user_input()
    
    print("\n⏳ Fetching news... Please wait...\n")
    links, subtexts = fetch_hackernews_pages(pages)
    
    top_news = extract_news(links, subtexts, min_votes)
    
    if top_news:
        print("\n🔥 Top Hacker News Articles:\n")
        display_news(top_news)

        # Ask if user wants to save the results
        save_option = input("\nDo you want to save the results to a file? (yes/no): ").strip().lower()
        if save_option in ["yes", "y"]:
            save_to_file(top_news)
    else:
        print("\n❌ No articles found with the given criteria.")

# Run the script
if __name__ == "__main__":
    main()
