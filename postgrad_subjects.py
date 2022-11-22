from bs4 import BeautifulSoup
import os

parent_folder = 'sources/'

sources = os.listdir(parent_folder)
output_set = set()
output_file = open("postgrad_subjects.txt", 'w')

for file in sources:
    website = open(parent_folder + file)
    website_content = website.read()
    soup = BeautifulSoup(website_content, "lxml")

    titles = soup.find_all("h3", {"class": "card-title"})

    for title in titles:
        output_set.add(title.text.split(':')[0]+'\n')

for lines in output_set:
    output_file.write(lines)
output_file.close()
