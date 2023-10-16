import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Read the HTML content from the "index.html" file
with open("index.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find the "news" section
news_section = soup.find("section", {"id": "news"})

if news_section:
    # Create the root element for the RSS feed
    rss = ET.Element("rss", attrib={"version": "2.0"})

    # Create the channel element
    channel = ET.SubElement(rss, "channel")

    # Find and append new <li> items to the RSS feed
    for li in news_section.find("ul", class_="wip").find_all("li"):
        # Extract the content of the <li> element
        li_text = ' '.join([text for text in li.stripped_strings])

        # Check if the <li> contains an <a> tag with an 'href' attribute
        link_element = li.find("a", href=True)
        if link_element:
            link = link_element["href"]
        else:
            link = ""

        item = ET.SubElement(channel, "item")
        item_title = ET.SubElement(item, "title")
        item_title.text = li_text

        item_link = ET.SubElement(item, "link")
        item_link.text = link

    # Create an XML tree and save it to a file
    xml_tree = ET.ElementTree(rss)
    xml_tree.write("news_feed.xml")

    print("New items appended to the RSS feed.")
else:
    print("No 'news' section found in the HTML.")
