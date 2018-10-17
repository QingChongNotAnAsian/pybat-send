# pybat-send
Battery script in Python for notify-send

### Examples:

To run this script, start it in the background of your .xinitrc with the following line:

`python /path/to/pybat-send.py &`

To run this script without accidentally starting a new one (if your .xinitrc is run multiple times per power cycle), use the following to avoid running duplicate scripts: 


```
user=$(whoami)
bn_notifs=$(ps -aux | grep -c "python /home/$user/.local/bin/pybat-send/pybat-send.py")

if [ $bn_notifs -eq 1 ]; then
	python ~/.local/bin/pybat-send/pybat-send.py &
fi
```
