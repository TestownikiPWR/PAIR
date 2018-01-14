#Autor: Kinoll
#Bierzcie i jedzcie z tego wszyscy
#-*- coding: utf-8 -*-
import csv

def loadFile(filename):
    riders = []
    with open(filename, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            riders.append(row)
    return riders

def getAllQ(filename):
    qs = []
    qs = loadFile(filename)
    return qs

def saveQ(filename, listOf):
    returnFile = ''
    for row in listOf:
        returnFile += (row + '\r\n')
    with open(filename, 'wb') as f:
        f.write(returnFile)
        
def getFilename(num):
    filename  = ""
    if num < 10:
        filename = "00" + str(num)
    elif num < 100:
        filename = "0" + str(num)
    else:
        filename = num
    filename += ".txt"
    return filename

def saveAllQ(qs):
    num = 1
    a = 0
    row = []
    f_row = "X0000"
    for q in qs:
        row.append("".join(q))
        print qs[a+1][0][0]
        if "0123456789".find(qs[a+1][0][0]) != -1:
            print "Dobra odpowiedz do pytania to: " + str(num)
            c = (int(raw_input()))
            d = list(f_row)
            d[c] = str(1);
            b = "".join(d)
            row.insert(0, b)
            saveQ(getFilename(num), row)
            num += 1
            row = []
        a += 1

saveAllQ(getAllQ("baza"))
