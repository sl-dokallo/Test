#/usr/bin/env python
# -*- coding: UTF-8 -*-

##############################################################################
# This is a part of the BATON product.
# Copyright (c) Interra Systems Inc.  All rights reserved.
#
# This source code is only intended as a supplement to the BATON API Reference
# and related electronic documentation provided with BATON.
# See these sources for detailed information regarding the BATON product.
##############################################################################


"""
This script demonstrates how to schedule a file for verification in Baton
and obtain its results.

Note
----
Please make sure that you have run contentlocations.py tutorial and ensured
that  the sample contents directory (shipped with this tutorial) has been
registered with local Baton installation.
"""
# import pathsetup

# from batonlib.baton import Baton
# from batonlib.content import sampleProgramFile200KB
import xmlrpclib
import sys,os
import time
reload(sys)
sys.setdefaultencoding('utf8')



address = '172.17.230.202'
port = 8080
login = 'admin'
password = 'admin'

def batonURL(login, password, address, port):
    return 'http://%s:%s@%s:%d/Baton' % (login, password, address, port)

#The URL looks like: http://admin:admin@127.0.0.1:8080

url = batonURL(login, password, address, port)

Baton = xmlrpclib.Server(url)


"""
When we schedule a file for verification, we need to specify:
- its file path on the content location
- the test plan which we will use for verifying the file
- the priority with which we want to schedule the file for verification.

A verification task is created for the file.
The task id of this task is returned.

We can use this task id later for querying any information about the task.

"""

#path of our file to be verified

#lest schedule it with high priority
priority = 'Low'

#Lets select a test plan for this file
testPlan = 'BatonDemo'
def getpath(filepath,result):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            getpath(fi_d,result)
        else:
            result.append(fi_d.replace('/mnt/data/remote/liveData','\\\\172.17.228.6\LiveData').replace('/','\\'))
    return result
            # if '.xml' in fi_d:
            #     DOMTree = xml.dom.minidom.parse(fi_d)
            #     trees = DOMTree.documentElement
            #     TargetPath = trees.getElementsByTagName('TargetPath')[0].firstChild.data
            #     URI = trees.getElementsByTagName('URI')[1].firstChild.data
def sendtask(filepath):
    tasks=[]
    resultFile=getpath(filepath,[])
    #Lets schedule a file for verification
    # print 'Scheduling %s for verification with \ntest plan: %s, priority: %s' % (mediaFilePath,testPlan,priority)
    for result in resultFile:
        # print result
        try:
            taskId = Baton.Tasks.verifyFile(testPlan,'', priority,result)
        except xmlrpclib.Fault, e:
            print 'Fault Code: ', e.faultCode, ' ', e.faultString
            sys.exit(2)
        except Exception, e:
            print 'Could not schedule the task for verification.'
            print 'Reason: ', e
            sys.exit(2)
        # print 'File scheduled for verification. Task id is: %s' % taskId
        tasks.append([taskId,result])
    return tasks

#Lets query the task status, currently it should be ready

def taskStatus(Baton, taskId):
    #We can query status of the task
    status, statusDescription = Baton.Tasks.status(taskId)
    progress = Baton.Tasks.progress(taskId)
    # print 'Current Status: ', status, ' Progress: ', progress, ' %'
    return status

def checkTask(filepath):
    taskIds = sendtask(filepath)
    verificationReports =[]
    #Lets wait for this task to start
    for taskId in taskIds:
        while 'Ready' == taskStatus(Baton, taskId[0]):
            time.sleep(1)
            #although this is not absolutely required, but we can wake-up the task scheduler of Baton
            #also to expedite the task execution
            Baton.wakeupTaskScheduler()

        # print 'File verification has started.'

        #Lets wait for the task to finish
        while 'Running' == taskStatus(Baton, taskId[0]):
            time.sleep(1)

        # print 'File verification has completed.'

        #Lets get the result of this task
        result, resultDescription = Baton.Tasks.result(taskId[0])

        # print 'Result: ', result
        # print 'ResultDescription',resultDescription
        # #Lets get the number of errors reported
        # print 'Number of errors: ', Baton.Tasks.errors(taskId[0])
        #
        # #Lets get the number of warnings reported
        # print 'Number of warnings: ', Baton.Tasks.warnings(taskId[0])

        # #We can access the verification report as XML
        verificationReport = Baton.Tasks.report(taskId[0])
        verificationReports.append([verificationReport,taskId[1],taskId[0]])
    return verificationReports

"""
The verification report XML contains:
 - total number of errors
 - total number of warnings
 - information about the file (its structure, format, audio/video types)
   - information about each elementary stream inside the file
 - details about each error/warning
   - location in file
   - synopsis
   - technical details of the error/warning

We will now parse this verification report and try to extract a lot of useful
information from it.

"""

"If you want you can print the verification report"
#print verificationReport

"if you want to write it to a file, you can do so"
# open('taskreport.xml', 'w').write(verificationReport)

"""
elementtree is a Python Package which helps in very
easy parsing of XML data.

If you don't have elementtree installed in your system,
please get it from:

http://effbot.org/zone/element-index.htm

If Baton is installed on this computer, elementtree package has already
been installed.

"""
def getresult(filepath):
    verificationReports = checkTask(filepath)
    import xml.etree.ElementTree as ET
    for verificationReport in verificationReports:
        """
        We will now parse the XML and get its document root
        """
        docRoot = ET.fromstring(verificationReport[0])

        #toplevelinfo node contains some Top Level Information
        toplevelInfo = docRoot.find('toplevelinfo')

        #Number of errors
        numErrors = toplevelInfo.get('Error')

        numWarnings = toplevelInfo.get('Warning')

        print ' taskId:'+verificationReport[2]+' ,Total number of warnings in this file:'+numWarnings+' ,Total number of errors in this file:'+numErrors+' ,File: '+verificationReport[1].replace('\\\\','\\')


        # #Number of errors
        # numWarnings = toplevelInfo.get('Warning')
        #
        # print 'File: '+verificationReport[1].replace('\\\\','\\')+' ,Total number of warnings in this file:'+numWarnings+' ,taskId:'+verificationReport[2]

        # print 'File: %s Total number of warnings in this file:%s ,taskId:%s',(verificationReport[1], numWarnings, numErrors,verificationReport[2])

        """
        One test plan can be applicable for multiple file formats.
        Baton figures out the file format of a file automatically.
        This is then written as part of vreport.
        """

        #File Format as figured out by Baton
        # Format = toplevelInfo.get('Format')

        # print 'File Format: ', Format

        """
        Stream Hierarchy describes how audio/video streams are organized
        inside the file.
        
        A helper function is there to parse this information from the XML file
        
        In this case its something like:
        {'Program ID = 0': [{'name': 'MPEG2 Video', 'parent': '0', 'id': '224'}, {'name': 'MPEG1 Audio', 'parent': '0', 'id': '192'}]}
        """
        # from batonlib.hierarchy import getStreamHierarchy
        #
        # hierarchy = getStreamHierarchy(docRoot)
        #
        # """
        # hierarchy is essentially a dictionary of information about individual
        # audio/video streams.
        #
        # The interpreation of hierarchy will depend upon file format
        # """
        # print hierarchy
if __name__ == '__main__':
    getresult(sys.argv[1])

