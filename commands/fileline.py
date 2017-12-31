#! /usr/bin/env bash

cmdname=${0##*/}

helpmsg () {
    echo "Brief:"
    echo "    1. count lines of all text files in current directory recursively"
    echo "    2. count lines of file which suffix is [type] in current directory recursively"
    echo "    3. count lines of a specified [file]"
    echo "Usage:"
    echo "    1. $cmdname"
    echo "    2. $cmdname [type]"
    echo "    3. $cmdname [file]"
    echo "Try again"
    echo ""
}

parameter=

if [[ $# -ge 1 ]]; then
    parameter="$1"
fi

count=0
for i in $(filelist $parameter); do
    if file $i | grep "text" 1>/dev/null 2>&1 ; then
        tmp_count=$(grep -v '^$' $i | wc -l)
        count=$(echo -e "$count + $tmp_count" | bc)
    fi
done
echo "$count"