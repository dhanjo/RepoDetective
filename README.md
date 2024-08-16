# Repository Leak Checker for Jenkins

This tool scans an organization's GitHub repositories and identifies any public repositories that might have been leaked. It is designed to be integrated into a Jenkins pipeline, helping to automate security checks and prevent unintended public exposure of repositories.

## How It Works

The script makes an API call to GitHub to retrieve all repositories for the specified organization. It filters out any private repositories and flags those that are public. The results are logged and saved in a JSON file, ensuring transparency and traceability of repository statuses.

## Features

- Scans all repositories within an organization.
- Identifies public repositories that could be unintentionally exposed.
- Saves the scanned data to a JSON file with a timestamp.
- Automates security checks within a Jenkins CI/CD pipeline.
- Handles pagination in the GitHub API response to ensure all repositories are checked.

## Installation

1. Clone this repository to your Jenkins server:
   ```bash
   git clone https://github.com/yourusername/repo-leak-checker.git
```
2. Navigate into the repository directory:
   ```bash
   cd repo-leak-checker
```
3. Ensure you have the required dependencies:
   ```bash
   pip install requests
  ```
## Usage
Set up your GitHub API Token:
Update the headers variable in the script to include your personal access token:

headers = {"Authorization": "Bearer YOUR_GITHUB_ACCESS_TOKEN"}

Run the script:
Execute the script manually or include it as part of a Jenkins pipeline to check for public repositories in your organization:

bash
python3 repo_leak_checker.py
Output:
The script will print out any public repositories found and save the repository information to a JSON file named Json_Data_<MM_DD_YYYY>.json. If no public repositories are found, the script will notify you with [+] No Public Repository Discovered.


