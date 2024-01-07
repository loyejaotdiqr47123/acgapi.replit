#!/bin/bash

URL=${REPL_SLUG}.${REPL_OWNER}.repl.co

echo -e "Replit 保活日志：\e[0m"

while true; do curl -s 'https://35932bc2-d342-4ddc-8d8f-718cb3f8eb9c-00-16ourpq2b2y16.riker.replit.dev/' --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" >/dev/null 2>&1 && echo "$(date +'%Y%m%d%H%M%S') 请求成功 ..." && sleep 1; done &
python3 index.py