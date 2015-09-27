import csv
import sys
class BoltSettings(object):
    @staticmethod
    def saveDict(dict_rap):
        f=open('settings.dict', "wb")
        w = csv.writer(f)
        for key, val in dict_rap.items():
            w.writerow([key, val])
        f.close()
    
    @staticmethod
    def readDict():
        f=open('settings.dict','rb')
        dict_rap={}
        for key, val in csv.reader(f):
            dict_rap[key]=val #eval(val)
        f.close()
        return(dict_rap)



 






