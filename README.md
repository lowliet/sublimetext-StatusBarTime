StatusBarTime
=========================

Small package that is displaying current time on status bar.
Works with Sublime 3 (and 2).

## How to install

 - Clone or [download](https://github.com/lowliet/sublimetext-StatusBarTime/archive/master.zip) git repo into your packages folder

Using [Package Control](http://wbond.net/sublime_packages/package_control):

 - Run “Package Control: Install Package” command, and find `StatusBarTime` package

--------------

## Settings

Example config:

    "StatusBarClock_type": 0,    	// Clock type as sublime text uptime: 0 - time, 1 - sublime uptime
    "StatusBarClock_Interval": 1000, // Clock update interval (in millisecond)
    "StatusBarClock_display_onlyinview": true,   // If true then clock will only be displayed when there is a file in view
    "StatusBarTime_format": "%H:%M:%S" // Time format, for "%a - %H:%M:%S" -> Mon - 22:58:24

For more information refer to [Python documentation](http://docs.python.org/2/library/time.html#time.strftime)

--------------

## Preview

![Preview] (https://github.com/lowliet/sublimetext-StatusBarTime/raw/master/preview.png)

--------------
