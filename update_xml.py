import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import datetime

# Base URL for the links in the RSS feed
base_url = "https://ramirogarcia.xyz"

date_format = "%a, %d %B %Y"
date = datetime.datetime.now().strftime(date_format)
# datetime.datetime.now().strftime("%B %d, %Y")
# datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")


# Read the existing RSS feed (if any) to check for duplicates
existing_items = set()

try:
    existing_xml = ET.parse("news_feed.xml")
    existing_root = existing_xml.getroot()
    for item in existing_root.findall(".//item"):
        title = item.findtext(".//title")
        existing_items.add(title)
except FileNotFoundError:
    pass  # If the XML file doesn't exist, ignore the exception

# Read the HTML content from the "index.html" file
with open("index.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find the "news" section
news_section = soup.find("section", {"id": "news"})

# Create the root element for the RSS feed
rss = ET.Element("rss", attrib={"version": "2.0"})

# Create the channel element
channel = ET.SubElement(rss, "channel")

# Add <title> and <link> to the channel
channel_title = ET.SubElement(channel, "title")
channel_title.text = soup.title.string
channel_link = ET.SubElement(channel, "link")
channel_link.text = base_url

# Add <lastBuildDate> to the channel
last_build_date = ET.SubElement(channel, "lastBuildDate")
last_build_date.text = date

items_appended = False  # Flag to track whether items were appended

for li in news_section.find("ul", class_="wip").find_all("li"):
    title_text = "News from Ramiro"
    
    # Check if the <li> contains an <a> tag with an 'href' attribute
    link_element = li.find("a", href=True)

    if link_element:
        # If a link is present, use all the text within the <li> as the xml <description>
        description = ' '.join([str(text) for text in li.stripped_strings])
        # Use the link URL as the xml <link>
        link = link_element["href"]
    else:
        # If no link is present, use all the text within the <li> as the title and avoid generating a <link>
        description = ' '.join([str(text) for text in li.stripped_strings])
        link = ""

    if description:
        # Check if the item title already exists in the RSS feed
        if description not in existing_items:
            # Add the item to the existing items set and the RSS feed
            existing_items.add(description)

            item = ET.SubElement(channel, "item")
            item_title = ET.SubElement(item, "title")
            item_title.text = title_text

            item_description = ET.SubElement(item, "description")
            item_description.text = description
            
            item_link = ET.SubElement(item, "link")
            item_link.text = link
            
            items_appended = True  # Items were appended


# Insert the lastBuildDate into the HTML
dateline_span = soup.find("span", class_="dateline")
if dateline_span:
    time_element = dateline_span.find("time")
    if time_element:
        time_element["datetime"] = datetime.datetime.now().strftime(date_format)
        time_element.string = date

# Prettify the HTML with 4 spaces for indentation
soup_prettified = soup.prettify(formatter="html")

# Save the modified HTML back to a file
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(str(soup_prettified))

# Create an XML tree and save it to a file
xml_tree = ET.ElementTree(rss)
xml_tree.write("news_feed.xml")

if items_appended:
    print("New items appended to the RSS feed")
else:
    print("No new items appended to the RSS feed")
