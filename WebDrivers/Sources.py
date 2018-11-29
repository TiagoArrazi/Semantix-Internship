#! /usr/bin/env python3

from math import pi, e, tau

def getXPath(i):

    xpathList = ["//ytd-button-renderer[@class='style-scope ytd-masthead style-blue-text size-default']", "//input[@type='email']", "//input[@type='password']", "//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]", "//*[@id='placeholder-area']", "//*[@id='contenteditable-textarea']", "//*[@id='submit-button']"]

    return xpathList[i]

def getAP_631():
    
    return str(pi).replace('.','')

def getAP2():

    return str(e).replace('.','')

def getAP3():

    return str(tau).replace('.','')

