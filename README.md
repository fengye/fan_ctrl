DIY PWM Raspberry Pi Fan Project
================================
This repo is mostly based on [Aerandir14's work](https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/) with a few changes to suit my needs.

Also the repo aggregate stuff together so I won't get lost next time building one.

Tested on Raspberry Pi 4 running Raspbian busty.

Building
--------
For parts and building instruction, please refer to the [original post](https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/).

Calibrating
-----------
Modify the pin on GPIO and PWM frequency.
```shell
$ python calib_fan.py
```

Production
----------
Apply the same pin and frequency to fan_ctrl.py, then
```shell
$ python fan_ctrl.py &
```
If you want to run the script whenever system start up, put it in rc.local/cron job.
Or, even better, running as a service
```shell
$ sudo cp fan-ctrl.service /lib/systemd/system/ 
$ sudo systemctl enable fan-ctrl.service
$ sudo systemctl start fan-ctrl.service
```

