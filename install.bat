#!/usr/bin/env bash

echo "[lin-vim] installing Lin Rongbin's Vim Distribution"
echo ""

cd %HOMEPATH%\.vim
git pull origin master
install\win32.bat