StatusBarTime
=========================

Small package for displaying current time (or uptime) on status bar.
Works with Sublime 2 and 3.

## Preview

![Preview] (https://github.com/lowliet/sublimetext-StatusBarTime/raw/master/preview.png)

--------------

## How to install

 - Clone or [download](https://github.com/lowliet/sublimetext-StatusBarTime/archive/master.zip) git repo into your packages folder

Using [Package Control](http://wbond.net/sublime_packages/package_control):

 - Run “Package Control: Install Package” command, and find `StatusBarTime` package

--------------

## Settings

Example config:

	// Clock type as sublime text uptime: 0 - time, 1 - sublime uptime
    "StatusBarClock_type": 0,

    // Clock update interval (in millisecond)
    "StatusBarClock_Interval": 1000,

	// If true then clock will only be displayed when there is a file in view
    "StatusBarClock_display_onlyinview": true,

    // Time format, for "%a - %H:%M:%S" -> Mon - 22:58:24
    "StatusBarTime_format": "%H:%M:%S"

For more information refer to [Python documentation](http://docs.python.org/2/library/time.html#time.strftime)

--------------