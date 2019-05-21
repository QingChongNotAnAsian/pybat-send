upower -i $(upower -e | grep BAT) | grep --color=never -E state |tr -s ' '|cut -d' ' -f3
