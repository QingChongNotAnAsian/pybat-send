#!/usr/bin/env python3

NOTIFY_EVERY = 5

import subprocess
import time

command_low_battery = "notify-send 'Battery' '10%, will die soon!' -u critical"
command_medium_battery = "notify-send 'Battery' '25%, charge soon!' -u normal"
command_half_battery = "notify-send 'Battery' 'Half Battery' -u low"
command_full_battery = "notify-send 'Battery' 'Full Battery' -u low"
command_start_charging = "notify-send 'Battery' 'Charging @ {0}%' -u low"
command_stop_charging = "notify-send 'Battery', 'Discharging @ {0}%' -u low"

times_lb = 0
times_mb = 0
times_hb = 0
times_fb = 0

times_stc = 0
times_spc = 0

def run_command(cmd):
    """
    Run command as /bin/bash script.
    """
    subprocess.Popen(["/bin/bash", "-c", cmd])

def battery_precentage():
    """
    This function returns the battery percentage.
    A custom script (battery_percentage.sh) could be used,
    but it was decided it'd be nice to have a standalone script.
    """
    command = "upower -i $(upower -e | grep BAT)|grep --color=never -E percentage|xargs|cut -d' ' -f2|sed s/%//"
    get_battery_data = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
    return get_battery_data.communicate()[0].decode('utf-8').replace("\n", "")

def get_state():
    """
    Get battery state:
     1) charging
     2) discharging
    """
    command = "upower -i $(upower -e | grep BAT) | grep --color=never -E state |tr -s ' '|cut -d' ' -f3"
    get_battery_state = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
    return get_battery_state.communicate()[0].decode('utf-8').replace("\n", "")

def is_bat_charging():
    """
    Boolean: isBatCharging
    """
    bat_state = str(get_state())
    if bat_state == "charging":
        return True
    elif bat_state == "discharging":
        return False

def do_actions():
    """
    Do different actions based on the state of the battery.
    """

    global times_lb, times_mb, times_hb, times_fb, times_stc, times_spc
    global command_low_battery, command_medium_battery, command_half_battery, command_full_battery, command_start_charging, command_stop_charging

    charge = int(battery_precentage())
    is_charging = is_bat_charging() 

    if charge == 100 and times_fb == 0:
        run_command(command_full_battery)
        times_fb = 1
    elif charge <= 50 and charge > 25 and times_hb == 0:
        run_command(command_half_battery)
        times_hb = 1
    elif charge <= 25 and charge > 10 and times_mb == 0:
        run_command(command_medium_battery)
        times_mb = 1
    elif charge <= 10 and times_lb == 0:
        run_command(command_low_battery)
        times_lb = 1

    if is_charging and times_stc == 0:
        run_command(command_start_charging.format(charge))
        times_stc = 1
        times_spc = 0
        
    elif not is_charging and times_spc == 0:
        run_command(command_stop_charging.format(charge))
        times_spc = 1
        times_stc = 0


if __name__ == '__main__':
    while True:
        do_actions()
        time.sleep(NOTIFY_EVERY)

