# _*_ coding: utf-8 _*_
import os
print "listdir"
print os.listdir("/boss/uig/zjftemp")

print "walk"
for root, dir, files in os.walk("/boss/uig/zjftemp"):
    print root, dir, files