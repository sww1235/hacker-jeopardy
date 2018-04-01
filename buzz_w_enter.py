#!/usr/bin/python

# Copyright Skullspace, 2014
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved. This file is offered as-is,
# without any warranty.
# http://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html
# @author Mark Jenkins <mark@markjenkins.ca>

from sys import argv

from buzz import buzz


def main():
    buzz_number = int(argv[1])

    while True:
        raw_input("> ")
        buzz(buzz_number)


if __name__ == "__main__":
    main()
