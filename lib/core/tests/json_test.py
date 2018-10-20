import json

def file_read(path,log = False):
    if log == True:
        print("Opening file ",path,"...")
        f = open(path,'r')
        print("Reading file ",path,"...")
        lignes  = f.readlines()
        print("Closing file ",path,"...")
        f.close()
        print("Done !")
    else :
        f = open(path,'r')
        lignes = f.readlines()
        f.close()
    return lignes

def jsonFileRead(path,log = False):
    if log == True:
        print("Opening file ",path,"...")
        f = open(path,'r')
        print("Reading file ",path,"...")
        lignes  = ''.join([e for e in f.readlines() if type(e) == str])
        print("Closing file ",path,"...")
        f.close()
        print("Done !")
    else :
        f = open(path,'r')
        lignes = ''.join([e for e in f.readlines() if type(e) == str])
        f.close()
    return lignes


#file_read("0-2001000.primes",True)


#EXPORT
d = {
    "a": "a",
    "b": 1
}

print(d)
print("")
z = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
z_compact = json.dumps(d, sort_keys=True, separators=(',', ': '))
print(z)
print(z_compact)



#IMPORT
d_in = json.loads(jsonFileRead("lib/data/rulesets/test.casruleset"))
print(d_in)

for rule in d_in['ruleset']['rules']:
    print("name    :",d_in['ruleset']['rules'][rule]['name'])
    print("setup   :",' '.join([str(e) for e in d_in['ruleset']['rules'][rule]['setup'][0]]))
    print("         ",' '.join([str(d_in['ruleset']['rules'][rule]['setup'][1][0]),"X",str(d_in['ruleset']['rules'][rule]['setup'][1][1])]))
    print("         ",' '.join([str(e) for e in d_in['ruleset']['rules'][rule]['setup'][2]]))
    print("outcome :",d_in['ruleset']['rules'][rule]['outcome'])





d_in = json.loads(jsonFileRead("lib/data/grids/test.casgrid"))
print(d_in)

for rule in d_in['ruleset']['rules']:
    print("name    :",d_in['ruleset']['rules'][rule]['name'])
    print("setup   :",' '.join([str(e) for e in d_in['ruleset']['rules'][rule]['setup'][0]]))
    print("         ",' '.join([str(d_in['ruleset']['rules'][rule]['setup'][1][0]),"X",str(d_in['ruleset']['rules'][rule]['setup'][1][1])]))
    print("         ",' '.join([str(e) for e in d_in['ruleset']['rules'][rule]['setup'][2]]))
    print("outcome :",d_in['ruleset']['rules'][rule]['outcome'])













