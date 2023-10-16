# Step 1: Change to the project root directory
$projectRootDir = "."
Set-Location -Path $projectRootDir

# Step 2: Use git to add all changes
git add .

# Step 3: Prompt for a commit message
$commitMessage = Read-Host -Prompt "Enter a commit message"

# Commit the changes with the provided message
git commit -m $commitMessage

# Push the changes to the remote repository
git push
