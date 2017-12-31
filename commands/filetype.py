#! /usr/bin/env bash

cmdname=${0##*/}

helpmsg () {
    echo "Brief:"
    echo "    rename file type from [oldtype] to [newtype]"
    echo "Usage:"
    echo "    $cmdname [oldtype] [newtype]"
    echo "Try again"
    echo ""
}

# error 1: miss parameter
if [[ $# -lt 2 ]]; then
    helpmsg
    exit 1
fi

oldtype="$1"
newtype="$2"
backup="$PWD.old"
while [[ -d $backup ]]; do
    backup="$backup.old"
done
echo "[lin-vim] replace $oldtype with $newtype in $PWD, backup is $backup"
cp -rf $PWD $backup

file_type_dir() {
    curdir=$1
    cd $curdir
    for i in $(ls); do
        if [[ -d $i ]]; then
            if [[ ${i:0:1} != '.' ]]; then
                file_type_dir $i
            fi
        else
            if [[ -f $i ]]; then
                extension="${i##*.}"
                filename="${i%.*}"
                if [[ $extension == "${oldtype}" && $extension != "$i" ]]; then
                    mv "$i" "$filename.$newtype"
                fi
            fi
        fi
    done
    cd ..
}

file_type_dir .