#! /usr/bin/env bash

cmdname=${0##*/}

helpmsg () {
    echo "Brief:"
    echo "    1. find all files of current directory recursively"
    echo "    2. find file by [name] of current directory recursively"
    echo "Usage:"
    echo "    1. $cmdname"
    echo "    2. $cmdname [name]"
    echo "Try again"
    echo ""
}

count=0
if [[ $# -lt 1 ]]; then
    # no name specified, list all
    for i in $(find . -type f -not -path "*.svn/*" -not -path "*.git/*" -not -path "*.svn" -not -path "*.git"); do
        len=$(echo -e "${#i} - 2" | bc)
        echo "$PWD/${i:2:$len}"
        count=$(echo -e "$count + 1" | bc)
    done
else
    # list by name
    for i in $(find . -name "*$1" -type f -not -path "*.svn/*" -not -path "*.git/*" -not -path "*.svn" -not -path "*.git"); do
        len=$(echo -e "${#i} - 2" | bc)
        echo "$PWD/${i:2:$len}"
        count=$(echo -e "$count + 1" | bc)
    done
fi
echo "[lin-vim] file count: $count"