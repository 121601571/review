import redis
import json


def getCon():
    pass
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r

con1 = getCon()

def getRankingStatus(contact ):
    pass
    global con1
    res = con1.get(contact)
    if res == None:
        return {}
    return json.loads(res)

def setLocalCache(contact, res):
    global con1
    res = json.dumps(res)
    con1.set(contact, res, 60)
    return

if __name__ == '__main__':
    pass
    a = getRankingStatus('liyi2')
