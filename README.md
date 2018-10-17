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

##### Running at a custom time (e.g. cron, macro)

If you want to run this script on a key macro, or from cron, etc.. use the file `run_do_actions.py`. In i3 this key macro would look like this:

```
bindsym $mod+Control+b exec --no-startup-id /path/to/run_do_actions.py
```

As a cron job:

```
* * * * * /path/to/run_do_actions.py
```
