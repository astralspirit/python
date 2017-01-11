#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import httplib
import urllib

 
def sendhttp():
    conn = httplib.HTTPConnection('bugs.python.org')
    conn = httplib.HTTPConnection('10.46.158.10',8088,timeout=30)
    conn.request('POST', '/fcgi-bin/UIG_SFC_186', '', {})
    httpres = conn.getresponse();
    
    print httpres.status
    print httpres.reason
    print httpres.read()
              
if __name__ == '__main__':  
    sendhttp() 