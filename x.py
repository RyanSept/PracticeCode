# -*- coding: utf-8 -*-
##class cartesianPoint: 
##    pass 
##cp1 = cartesianPoint() 
##cp2 = cartesianPoint() 
##cp1.x = 1.0 
##cp1.y = 2.0 
##cp2.x = 1.0 
##cp2.y = 3.0 
##def samePoint(p1,p2): 
##    return (p1.x == p2.x) and (p1.y == p2.y) 
##def printPoint(p): 
##    print '(' + str(p.x) + ', ' + str(p.y) + ')' 
##def __cmp__(self,other):
##    return (self>other)
##class Rectangle: 
##    def __init__(self,width,height,corner): 
##        self.width = width 
##        self.height = height 
##        self.corner = corner
import os 
x=u"C:\Python27\KANA-BOON _ ないものねだり.txt"
f=open(unicode(x),'rb')
print f.readline()
f.close()
os.path.basename(x)
print "ないものねだり"
##print x.replace(os.path.sep,'\\')
##print os.path.basename(x)
###print os.path.basename(x).encode('utf8')
##print os.path.basename(x).decode('utf8')

