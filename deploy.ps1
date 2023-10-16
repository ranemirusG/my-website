$projectRootDir = "."
Set-Location -Path $projectRootDir




$HtmlFilePath = ".\index.html"
$RssFilePath = ".\news_feed.xml"
$StoredHashFile = ".\stored_hash.txt"

# Function to update the RSS feed
function UpdateRSSFeed {
    # Read the current RSS feed XML
    [xml]$rss = Get-Content $RssFilePath

    # Find the "News" section in your HTML (you may need to adjust this based on your HTML structure)
    $newsSection = $rss.SelectSingleNode("//channel/item[title='News']")

    # Check if the "News" section exists
    if ($newsSection -eq $null) {
        # If not found, create a new "News" item
        $newsSection = $rss.CreateElement("item")

        # Add the title and description (adjust as needed)
        $title = $rss.CreateElement("title")
        $title.InnerText = "News"
        $description = $rss.CreateElement("description")
        $description.InnerText = "Latest news and updates from ramirogarcia.xyz"

        # Append the title and description to the "News" section
        $newsSection.AppendChild($title)
        $newsSection.AppendChild($description)

        # Append the "News" section to the RSS feed
        $rss.channel.AppendChild($newsSection)
    }

    # Insert your code here to update the news items based on changes in the HTML file
    # For each news item in the HTML, create a new item in the RSS feed
    # Example:
    # $newItem = $rss.CreateElement("item")
    # $newTitle = $rss.CreateElement("title")
    # $newTitle.InnerText = "News Title"
    # $newDescription = $rss.CreateElement("description")
    # $newDescription.InnerText = "News Description"
    # $newPubDate = $rss.CreateElement("pubDate")
    # $newPubDate.InnerText = (Get-Date).ToString("r")
    # $newLink = $rss.CreateElement("link")
    # $newLink.InnerText = "https://ramirogarcia.xyz/news#news-item"

    # Append the title, description, pubDate, and link to the new item
    # $newItem.AppendChild($newTitle)
    # $newItem.AppendChild($newDescription)
    # $newItem.AppendChild($newPubDate)
    # $newItem.AppendChild($newLink)

    # Append the new item to the "News" section
    # $newsSection.AppendChild($newItem)

    # Save the updated RSS feed
    $rss.Save($RssFilePath)
}


# Function to calculate the hash of a file
function GetFileHash($FilePath) {
    $hash = Get-FileHash -Algorithm MD5 -Path $FilePath
    return $hash.Hash
}

# Check if the HTML file has changed
$CurrentHash = GetFileHash $HtmlFilePath

# Load the previously stored hash, if available
if (Test-Path $StoredHashFile) {
    $StoredHash = Get-Content $StoredHashFile
} else {
    $StoredHash = $null
}

if ($CurrentHash -ne $StoredHash) {
    # HTML file has changed
    UpdateRSSFeed
    # Store the new hash
    $CurrentHash | Set-Content $StoredHashFile
}






git add .
$commitMessage = Read-Host -Prompt "Enter a commit message"
git commit -m $commitMessage
git push
