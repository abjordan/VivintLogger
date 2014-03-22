VivintLogger
============
Author: Alex Jordan (abjordan@gmail.com)

Primitive logging service for Enphase Energy solar panel monitor.

The Enphase Energy solar panel monitor has a very primitive local interface
that tells you your current production rate, how much energy you produced
today, and how much you have produced over the lifetime of the system. This
is a nice start, but wouldn't it be nice to see how your production
changes over time, or to see what the variations are like throughout the day?

This is an initial version of a tool to dump the current readings to the 
console. Next up is a fancy web server interface that stores the data, 
produces line charts, etc.

(Note: it looks like Enphase has a web service called MyEnlighten 
(see http://enphase.com/enlighten_content/myenlighten-launch-site/), but 
Vivint doesn't seem to provide its customers with access to the full
interface.)

Requires twisted-internet.