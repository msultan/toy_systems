#!/usr/bin/env python

import string,random, os,sys,multiprocessing
from IPython import parallel
from IPython.parallel import require
from IPython.parallel import Client

print "test"

def func(x):

    return x, x**3

def log_result(result):
    partial_results.append(result)
    file=open('partial.txt','w')
    save(file,partial_results)



def main():
    partial_results=[]
    c=Client(profile='default')
    print c.ids
    view=c.load_balanced_view()
    ar = view.map_async(func, range(10))
    #print ar.get_dict(timeout=0)
    print ar.msg_ids
    for i, r in enumerate(ar):
        print r[1]
    print ar.get()
    #print 'results'
    #print r.get()
    #full=view.map(func,range(50))
    #    #callback=partial_results.extend)

    #full.wait()
    #a=full.get()
    #print "hello",a,temp
    #if(a==partial_results):
        #    print "YES"
    #file=open('full.txt','w')
    #file.write(full.get())


if __name__=="__main__":
    main()
