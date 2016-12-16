from lxml import etree, html
from StringIO import StringIO
import csv

# Make sure your html file is in the same directory as this script

parsed = html.parse('results.html')

tweets = parsed.xpath("//div[contains(@class, 'js-original-tweet')]")

#/div[contains(@class, 'js-tweet-text-container')]//text()")


with open('parse_results.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter = ",", quotechar = '"')
    writer.writerow(["Tweet ID", "Direct response to Wintana's original status?", "Sent when?", "Sender", "Sender's name", "Text" , "In reply to what tweet, if any?",  "Data source"])
    for t in tweets:
        tweet_id = t.get("data-tweet-id").encode('UTF-8')
        screen_name = t.get("data-screen-name").encode('UTF-8')
        name = t.get("data-name").encode('UTF-8')
        data_source = "Twitter advanced search url:'https://twitter.com/search?q=to%3Awintanamn%20since%3A2016-11-29%20until%3A2016-12-06&src=typd&lang=en' "
        print tweet_id, screen_name, name
        writer.writerow([tweet_id, " ", "No date", screen_name, name, "text", "In reply to status_id", data_source])
print len(tweets)