#!/usr/bin/env bash
notify-send "$(xsel -o)" "$(wget -U "Mozilla/5.0" -qO - "http://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q=$(xsel -o | sed "s/[\"'<>]//g")" | sed "s/,,,0]],,.*//g" | awk -F'"' '{print $2, $6}')"
