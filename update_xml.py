import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Base URL for the links in the RSS feed
base_url = "https://ramirogarcia.xyz"

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
        # Check if the <li> contains an <a> tag with an 'href' attribute
        link_element = li.find("a", href=True)
        if link_element:
            # Extract the content of the <li> element
            li_text = ''.join([str(text) for text in li.contents if isinstance(text, str)])

            # Extract the text between the <a> tags
            link_text = link_element.get_text()

            # Use the link text within the title and the link as the description
            item_title = ET.SubElement(channel, "title")
            item_title.text = f"{li_text} {link_text}"

            item_description = ET.SubElement(channel, "description")
            item_description.text = link_element["href"]
        else:
            # If no link is present, use the entire <li> content as both title and skip generating a description
            li_text = ' '.join(map(str, li.contents))

            item = ET.SubElement(channel, "item")
            item_title = ET.SubElement(item, "title")
            item_title.text = li_text

    # Create an XML tree and save it to a file
    xml_tree = ET.ElementTree(rss)
    xml_tree.write("news_feed.xml")

    print("New items appended to the RSS feed.")
else:
    print("No 'news' section found in the HTML.")
