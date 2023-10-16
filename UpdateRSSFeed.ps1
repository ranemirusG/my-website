# Read the HTML content from the "index.html" file
$htmlFilePath = "index.html"
$htmlContent = Get-Content $htmlFilePath -Raw

# Define the "news" section
$startTag = '<section id="news">'
$endTag = '</section>'

# Find the "news" section within the HTML content
$startIndex = $htmlContent.IndexOf($startTag)
$endIndex = $htmlContent.IndexOf($endTag, $startIndex)

if ($startIndex -ne -1 -and $endIndex -ne -1) {
    $newsSection = $htmlContent.Substring($startIndex, $endIndex - $startIndex + $endTag.Length)

    # Define the XML filename
    $xmlFilename = "news_feed.xml"

    # Create a new XML document
    $xmlDoc = New-Object System.Xml.XmlDocument

    # Create the root element if it doesn't exist
    if (-not (Test-Path $xmlFilename)) {
        $root = $xmlDoc.CreateElement("root")
        $xmlDoc.AppendChild($root)
    } else {
        # Load the existing XML file
        $xmlDoc.Load($xmlFilename)
    }

    # Iterate through <li> elements in the "news" section
    [xml]$newsXml = $newsSection
    foreach ($li in $newsXml.section.wip.li) {
        $liText = $li.InnerText

        # Check if the <li> item already exists in the XML
        $itemExists = $false
        foreach ($xmlLi in $xmlDoc.root.SelectNodes("//li")) {
            if ($xmlLi.InnerText.Trim() -eq $liText) {
                $itemExists = $true
                break
            }
        }

        # If the <li> item is new, append it to the XML
        if (-not $itemExists) {
            $newLi = $xmlDoc.CreateElement("li")
            $newLi.InnerText = $liText
            $xmlDoc.root.AppendChild($newLi)
        }
    }

    # Save the updated XML
    $xmlDoc.Save($xmlFilename)
    Write-Host "New <li> items appended to the XML."
} else {
    Write-Host "No 'news' section found in the HTML."
}
