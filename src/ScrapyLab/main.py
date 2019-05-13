import os
from lxml import etree
from scrapy import cmdline


def task1_parse():
    try:
        os.remove("results/task1.xml")
    except OSError:
        print("OS Error occurred while trying to delete task1.xml")

    cmdline.execute("scrapy crawl task1 -o results/task1.xml -t xml".split())

def print_urls():
    root = etree.parse("results/task1.xml")
    for url in root.iterfind(".//item//url"):
        print(url.text)

def task2_parse():
    try:
        os.remove("results/task2.xml")
    except OSError:
        print("OS Error occurred while trying to delete task2.xml")

    cmdline.execute("scrapy crawl task2 -o results/task2.xml -t xml".split())


def xml_to_xhtml():
    dom = etree.parse("results/task2.xml")
    xslt = etree.parse("xslscripts/task2.xslt")
    transform = etree.XSLT(xslt)
    result = transform(dom)
    #print(result)
    try:
        os.remove("results/task2.html")
    except OSError:
        print("OS Error occurred while trying to delete task2.html")
    result.write_output("results/task2.html")


def do_task2():
    task2_parse()


def do_task1():
    task1_parse()


#do_task1()
#do_task2()
#xml_to_xhtml()
print_urls()