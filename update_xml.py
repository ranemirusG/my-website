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

    # Add required elements for the channel
    title = ET.SubElement(channel, "title")
    title.text = "Your RSS Feed Title"

    link = ET.SubElement(channel, "link")
    link.text = "http://example.com"

    description = ET.SubElement(channel, "description")
    description.text = "Your RSS Feed Description"

    # Find and append new <li> items to the RSS feed
    for li in news_section.find("ul", class_="wip").find_all("li"):
        li_text = li.get_text(strip=True)

        # Check if the <li> item already exists in the RSS feed
        item_exists = False
        for item in channel.findall("item"):
            if item.find("title").text.strip() == li_text:
                item_exists = True
                break

        # If the <li> item is new, append it to the RSS feed
        if not item_exists:
            item = ET.SubElement(channel, "item")
            item_title = ET.SubElement(item, "title")
            item_title.text = li_text

            item_link = ET.SubElement(item, "link")
            # You can set the link value if applicable, e.g., a link to the original source

            item_description = ET.SubElement(item, "description")
            item_description.text = "Description of " + li_text  # Modify this as needed

    # Create an XML tree and save it to a file
    xml_tree = ET.ElementTree(rss)
    xml_tree.write("news_feed.xml")

    print("New items appended to the RSS feed.")
else:
    print("No 'news' section found in the HTML.")
