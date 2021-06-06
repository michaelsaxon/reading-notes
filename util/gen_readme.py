import click
import os
from datetime import datetime as dt

MMAP = {
    "01" : "January",
    "02" : "February",
    "03" : "March",
    "04" : "April",
    "05" : "May",
    "06" : "June",
    "07" : "July",
    "08" : "August",
    "09" : "September",
    "10" : "October",
    "11" : "November",
    "12" : "December"
}


def gen_link_line(basepath, fname):
    lines = open(basepath + fname, "r").readlines()
    title = lines[0].strip("# ").strip()
    authors = lines[1].strip("Authors: ").strip().strip("**")
    topicstr = lines[7].strip()
    return f"#### {title}\nAuthors: *{authors}*\n\n{topicstr}\n\n[My Summary](r/{fname})\n\n"

@click.command()
@click.option('-d', default = None)
def main(d):
    if d is None:
        t = dt.today()
        d = f"{t.year%100:02d}{t.month:02d}"
    path = "../" + d + "/"
    rmex = os.path.isfile(path + "README.md")
    
    dfd = {}
    basepath = path + "r/"
    fnames = os.listdir(path + "r/")
    for fname in fnames:
        day = fname.split("-")[0]
        if day in dfd.keys():            
            dfd[day].append(fname)
        else:
            dfd[day] = [fname]

    month = MMAP[d[2:4]]
    year = "20" + d[0:2]

    with open(path + "README.md", "w") as f:
        ostr = f"# Michael's Reading Notes ({month} {year})\n[Back to home](../README.md)\n\n## By Date\n\n"
        days = reversed(list(dfd.keys()))
        for day in dfd.keys():
            ostr += f"### {month} {int(day)}, {year}\n\n"
            for fname in dfd[day]:
                ostr += gen_link_line(basepath, fname)
        f.write(ostr)

    print(f"README.md generated for {month} {year} at ../{d}/README.md")

if __name__ == "__main__":
    main()