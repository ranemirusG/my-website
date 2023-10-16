$projectRootDir = "."
Set-Location -Path $projectRootDir


C:\Users\zgzen\virtualenvs_python\scraping\Scripts\python.exe $projectRootDir\update_xml.py


git add .
$commitMessage = Read-Host -Prompt "Enter a commit message"
git commit -m $commitMessage
git push
