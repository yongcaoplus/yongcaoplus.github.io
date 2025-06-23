import csv
import os

with open('../../social.csv', 'r') as file:
    reader = csv.reader(file)
    paper_titles = []
    paper_urls = []
    for row in reader:
        paper_titles.append(" ".join(row[0:-1]).replace(",", " ").replace("\n", "").strip())
        paper_urls.append(row[-1].replace("abs", "pdf").replace("\n", "").strip())


# SORT BY URLS AND TITLES BY SAME INDEX
paper_titles, paper_urls = zip(*sorted(zip(paper_titles, paper_urls), key=lambda x: x[0]))


with open('../../social_titles.csv', 'w') as file:
    for title, url in zip(paper_titles, paper_urls):
        file.write(title + "\n")

with open('../../social_urls.csv', 'w') as file:
    for url in paper_urls:
        file.write(url + "\n")