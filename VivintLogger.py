#!/usr/bin/env python

import urllib2
import sys, re, time

from twisted.internet import task
from twisted.internet import reactor

# Important bits are of the form:
#
# <!-- START MAIN PAGE CONTENT -->
#    <h1>System Energy Production</h1>
#    <div style="margin-right: auto; margin-left: auto;"><table>
#    <tr><td colspan="3">System has been live since
#                           <div class=good>Thu Jan 30, 2014 10:23 AM EST</div></td></tr>
#    <tr><td>Currently</td>    <td> 2.56 kW</td></tr><tr><td>Today</td>     <td> 2.44 kWh</td></tr><tr><td>Past Week</td>    <td> 86.7 kWh</td></tr><tr><td>Since Installation</td>    <td>  151 kWh</td></tr>
#    </table><br></div>
#  <!-- END MAIN PAGE CONTENT -->

productionTable = re.compile(r'<!-- START MAIN PAGE CONTENT -->(?P<production>.*)<!-- END MAIN PAGE CONTENT -->')

def getCurrentProductionData():
    response = urllib2.urlopen("http://192.168.1.3/production?locale=en")
    page = response.read()
    #print page

    startTag = '<!-- START MAIN PAGE CONTENT -->'
    stopTag = '<!-- END MAIN PAGE CONTENT -->'
    start = page.find(startTag) + len(startTag)
    stop = page.find(stopTag)
    table = page[start:stop]

    dataPoint = {}

    rows = table.strip().split("<tr>")
    for r in rows:
        cols = r.strip().split("<td>")
        c_data = [c.strip().split("<")[0] for c in cols]
        if len(c_data) != 3:
            continue
        dataPoint[c_data[1]] = c_data[2]

    return dataPoint

def doUpdate():
    print "----- %s -----" % time.asctime()
    dataPoint = getCurrentProductionData()    
    for k,v in dataPoint.iteritems():
        print k, v

def main(args):
    l = task.LoopingCall(doUpdate)
    l.start(15)
    reactor.run()
    

if __name__=="__main__":
    args = sys.argv
    main(args)
