#!/usr/bin/env python
#color setting
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

#import public module
import sys
import math
import re
import csv
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

#General reactions
class Reactions():
    def __init__(self,time=0):
        self.time = time

    def Readseq(self, readseq='sequence.txt'):
        seq = open(readseq)
        self.f = seq.read()
        self.m = []
        for i in range(len(self.f)):
            self.m.append([0,0,0,0,0,0,0,0,0,0,self.f[i],''])
        #ds,dnaA,dnaB,dnaC,dnaG,SSB,Topo1,SDC,DNApol1,DNApol3
        return self.f,self.m,self.time

    def Generate(self,name,num):
        self.name = str(name)
        self.num = num
        print "{:<27}".format(YELLOW+self.name+ENDC)+" = "+BLUE+`self.num`+ENDC
        gn = [self.name,self.num]
        return gn

    def Complex(self,name1,name2,num):
        self.name1 = str(name1)
        self.name2 = str(name2)
        self.Cname = str(self.name1+"/"+self.name2)
        self.num = num
        print "{:<27}".format(RED+self.Cname+ENDC)+" = "+BLUE+`self.num`+ENDC
        return [self.Cname,self.num]

    def Compose(self, list, csubA, csubB, k):
        self.Complex = str(csubA+"/"+csubB)
        self.k = k
        for i in range(len(list)):
            if list[i][0] == str(csubA):
                self.a = list[i][1]
                list[i][1] = list[i][1] - 1
                print "["+GREEN+str(list[i][0])+ENDC+","+BLUE+str(list[i][1])+ENDC+"]",
            if list[i][0] == str(csubB):
                self.b = list[i][1]
                list[i][1] = list[i][1] - 1
                print "["+GREEN+str(list[i][0])+ENDC+","+BLUE+str(list[i][1])+ENDC+"]",
            if list[i][0] == self.Complex:
                list[i][1] = list[i][1] + 1
                print "["+GREEN+str(list[i][0])+ENDC+","+RED+str(list[i][1])+ENDC+"]",
        print ENDC
        self.p = self.k * self.a * self.b
        return list

    def Decompose(self, list, dsubAB,k):
        self.Complex = dsubAB.split('/')
        self.k = k
        for i in range(len(list)):
            if list[i][0] == str(self.Complex[0]):
                list[i][1] = list[i][1] + 1
                print "["+GREEN+str(list[i][0])+ENDC+","+RED+str(list[i][1])+ENDC+"]",
            if list[i][0] == str(self.Complex[1]):
                list[i][1] = list[i][1] + 1
                print "["+GREEN+str(list[i][0])+ENDC+","+RED+str(list[i][1])+ENDC+"]",
            if list[i][0] == dsubAB:
                self.ab = list[i][1]
                list[i][1] = list[i][1] - 1
                print "["+GREEN+str(list[i][0])+ENDC+","+BLUE+str(list[i][1])+ENDC+"]",
        print ENDC
        self.p = self.k * self.ab
        return list

class Enzyme():
    def __init__(self):
        pass

    def dnaA(self, location, mseq, state, k):
        return

    def dnaB(self, location, mseq, state, k):
        mseq[location][0] = 1
        state[1][1] -= 1
        return location, mseq, state

    def dnaC(self, time, state, k):
        return

    def dnaG(self, time, state, k):
        return

    def RNaseH(self, time, state, k):
        return

    def SSB(self, time, state, k):
        return

    def Topo1(self, time, state, k):
        return

    def SDC(self, time, state, k):
        mseq[location][7] = 1
        state[7][1] -= 1
        return location, mseq, state

    def DNApol1(self, time, state, k):
        return

    def DNApol3(self, location, mseq, state, k, r):
        if mseq[location][0] == 1:
            mseq[location][9] = 1
            state[9][1] -= 1
            error = 0.001#%
            rate = rand()*100
            if mseq[location][10]=='a':
                if rate >= error:mseq[location][11]='t'
                else:
                    mseq[location][11]='miss'
                    r[0] += 1
            if mseq[location][10]=='t':
                if rate >= error:mseq[location][11]='a'
                else:
                    mseq[location][11]='miss'
                    r[0] += 1
            if mseq[location][10]=='g':
                if rate >= error:mseq[location][11]='c'
                else:
                    mseq[location][11]='miss'
                    r[0] += 1
            if mseq[location][10]=='c':
                if rate >= error:mseq[location][11]='g'
                else:
                    mseq[location][11]='miss'
                    r[0] += 1
            mseq[location][0] = 0
            location += 1
        return location, mseq, state, k, r

    def DNApol3holoenzyme(self, time, state, k):
        return

class Propensity:
    def __init__(self):
        pass

    def dnaA(self, location, mseq, state, k):
        return

    def dnaB(self, location, mseq, state, k):
        return

    def dnaC(self, time, state, k):
        return

    def dnaG(self, time, state, k):
        return

    def RNaseH(self, time, state, k):
        return

    def SSB(self, time, state, k):
        return

    def Topo1(self, time, state, k):
        return

    def SDC(self, time, state, k):
        return

    def DNApol1(self, time, state, k):
        return

    def DNApol3(self, time, state, k):
        return

    def DNApol3holoenzyme(self, time, state, k):
        return

class Simulation:
    def __init__(self):
        Propensity().dnaA(1,1,1,1)

    def Propensity(self, state, k):
        pass

    def Step(self, time, state, events):
        atotal = 0
        alist = []
        for i in range(len(events)):
            atotal += events[i]

    def Makedata(self, dirname="result"):
        if os.path.exists(os.getcwd()+"/"+dirname):
            swt = 1
            print BLUE+dirname+RED+" already exists !!"+ENDC
            dirname = raw_input(YELLOW+"Please input other name : "+ENDC)
            while swt == 1:
                if os.path.exists(os.getcwd()+"/"+dirname):
                    dirname = raw_input(RED+"ERROR "+GREEN+"Please input other name : "+ENDC)
                else:
                    break
        os.mkdir(dirname)
        if os.path.exists(os.getcwd()+'/error.png'): shutil.move('error.png',os.getcwd()+"/"+dirname)
        if os.path.exists(os.getcwd()+'/result.txt'): shutil.move('result.txt',os.getcwd()+"/"+dirname)
