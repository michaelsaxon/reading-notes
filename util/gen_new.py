import click
import os
from datetime import datetime as dt

def get_new_fname(title, authors, day, basepath):
    authors = authors.strip().split(",")
    authors = list(map(lambda x: x.strip().split(" ")[-1].lower(), authors))
    title = title.strip().lower().split(" ")
    _authors = authors.pop(0)
    _title = title.pop(0)
    fname = f"{day:02d}-{_authors}-{_title}.md"
    while os.path.isfile(basepath + fname):
        try:
            _title += "-" + title.pop(0)
        except:
            try: 
                _authors += "-" + authors.pop(0)
            except:
                raise Exception("Failed to generate new file: exact filename already exists!")
        fname = f"{day:02d}-{_authors}-{_title}.md"
    return fname

URLDICT = {
    "arxiv.org" : "arXiv",
    "aclweb.org" : "ACL Anthology",
}


@click.command()
@click.option('-d', default = None)
def main(d):
    if d is None:
        t = dt.today()
        d = f"{t.year%100:02d}{t.month:02d}"
        day = t.day
    basepath = "../" + d + "/r/"
    #print(rmex)
    print("Title: ", end="")
    title = input()
    print("Authors: ", end="")
    authors = input()
    print("Venue: ", end="")
    venue = input()
    print("URL: ", end="")
    url = input()
    fname = get_new_fname(title, authors, day, basepath)
    with open(basepath + fname, "w") as f:
        domain = url.split("//")[-1].split("/")[0].strip().strip("www.").lower()
        urlname = URLDICT.get(domain, domain)
        f.write(f"# {title}\nAuthors: **{authors}**\n\nVenue: *{venue}*\n\nLink: [{urlname}]({url})\n\nTopics: \n\n## Summary\n\n## Thoughts\n\n")
    print(f"Generated md file at location: {basepath + fname}")
    with open("tmp.l", "w") as f:
        f.write(basepath + fname)

if __name__ == "__main__":
    main()