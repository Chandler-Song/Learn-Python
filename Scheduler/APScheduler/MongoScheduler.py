from apscheduler import executors
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient

def my_job():
    print 'hello world'
host='192.168.136.129'
port=27017
client=MongoClient(host,port)

jobstores = {
    'mongo':MongoDBJobStore(collection='job',database='test',client=client),
    'default': MemoryJobStore()
}

executors={
    'default': ThreadPoolExecutor(10),
    'processpool':ProcessPoolExecutor(3)
}

job_defaults = {
    'coalesce': False,
    'max_instances':3
}

scheduler = BlockingScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults)
scheduler.add_job(my_job,'interval',seconds=5)

try:
    scheduler.start()
except SystemExit:
    client.close()



