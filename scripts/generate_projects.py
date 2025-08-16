import requests

USERNAME = "VigneshPoojary-05"
API_URL = f"https://api.github.com/users/{USERNAME}/repos?sort=updated"

response = requests.get(API_URL)
repos = response.json()

project_lines = []
for repo in repos:
    if not repo['fork']:
        name = repo['name']
        url = repo['html_url']
        description = repo['description'] or "No description provided"
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        project_lines.append(f"- [{name}]({url}) — {description} ⭐ {stars} | Forks: {forks}")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start_tag = "<!-- PROJECTS_LIST_START -->"
end_tag = "<!-- PROJECTS_LIST_END -->"

if start_tag in readme and end_tag in readme:
    before = readme.split(start_tag)[0] + start_tag + "\n"
    after = "\n" + end_tag + readme.split(end_tag)[1]
    new_readme = before + "\n".join(project_lines) + after
else:
    new_readme = readme + f"\n\n{start_tag}\n" + "\n".join(project_lines) + f"\n{end_tag}"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
