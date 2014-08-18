# write_urls
# ----------
# write_urls is a simple script written in Python to help automate
# the creation of directory links in an html page.
#
# This script can be adapted to any situation whereby directories
# on a server need to be accessable or archived on a web page. There
# is a lot of room for expansion here and this script serves as a
# starting point.
#
# Author: John Merigliano
# July 2014

import os
import re

# Specify the directory to search for folders here.
curr_dir = os.listdir('./')


# Procedure to extract the specified contents of the directory.
def get_file_names(curr_dir):

    file_names = []

    # Change the following expression to suit your needs.
    # This example will add only directory names that contain
    # 6 numbers to a new list.
    # The relevant search pattern: a directory name with a 6 digit number.
    pattern = r'^\d{1,6}$'

    # Read the current directory and add matches to the list;
    for name in curr_dir:
        if re.match(pattern, name):
            file_names.append(name)
            # Remove if you do not want the list sorted
            # or specify a new sort directive.
            file_names.sort()

    return file_names


# Add the matching directory names to the new URLS.
def add_URLs(file_names):

    # The new URLs:
    URLs = []

    # Generate the URLS and add them to the list.
    for edition in file_names:
        # Specify URL, as needed.
        URLs.append(
            '<a href="#'
            + edition
            + '/index.html">'
            + edition
            + '</a><br />\n'
        )

    return URLs


# Generate an html page with the new urls.
def generate_html_page(urls):

    # Create the file.
    fin = open('index.html', 'w')

    # The html template:
    html_open = '<!DOCTYPE html>\n<html>\n\
    <head>\n\
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>\n\
    <title>index</title>\n</head>\n<body>\n\
    <!--// This page was automatically generated: DO NOT EDIT //-->\n'

    html_close = '</body>\n</html>\n'

    # Generate the page:
    fin.write(html_open)
    for url in urls:
        fin.write(url)
    fin.write(html_close)

    fin.close()


def main():

    # // IN //
    files = get_file_names(curr_dir)

    # // OUT //
    if len(files) != 0:
        urls = add_URLs(files)
        generate_html_page(urls)
    else:
        print 'no matches were found.'


if __name__ == '__main__':
    main()
