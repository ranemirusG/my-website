from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Read the HTML content from the "index.html" file
with open("index.html", "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find the "news" section
news_section = soup.find("section", {"id": "news"})

if news_section:
    # Create an XML element tree
    root = ET.Element("root")

    # Find and append new <li> items to the XML
    for li in news_section.find("ul", class_="wip").find_all("li"):
        li_text = li.get_text(strip=True)

        # Check if the <li> item already exists in the XML
        item_exists = False
        for existing_li in root.findall("li"):
            if existing_li.text.strip() == li_text:
                item_exists = True
                break

        # If the <li> item is new, append it to the XML
        if not item_exists:
            new_li = ET.Element("li")
            new_li.text = li_text
            root.append(new_li)

    # Create an XML tree and save it to a file
    xml_tree = ET.ElementTree(root)
    xml_tree.write("news_feed.xml")

    print("New <li> items appended to the XML.")
else:
    print("No 'news' section found in the HTML.")
