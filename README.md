StatusBarTime
=========================

Small Sublime Text 2 package that is displaying current time on status bar

## How to install

 - Clone or [download](https://github.com/lowliet/sublimetext-StatusBarTime/archive/master.zip) git repo into your packages folder

Using [Package Control](http://wbond.net/sublime_packages/package_control):

 - Run “Package Control: Install Package” command, and find `StatusBarTime` package

--------------

## Settings

Set clock type as sublime text uptime

Set the clock update interval

Set the display clock only when there is a file in view or display always like before

Set the format of the time using the StatusBarTime__format setting. Defaults to '%H:%M:%S'

Example:

    "StatusBarClock_type": 1    // Now it will display sublime text uptime
    
    "StatusBarClock_Interval": 5000 // Now clock will be updated every 5 sec
    
    "StatusBarClock_display_onlyinview": true   // Now clock will only be displayed when there is a file in view
    
    "StatusBarTime_format": "%a - %H:%M:%S" // Mon - 22:58:24

For more information refer to [documentation](http://docs.python.org/2/library/time.html#time.strftime)

--------------

## Preview

![Preview] (https://github.com/lowliet/sublimetext-StatusBarTime/raw/master/preview.png)

--------------
