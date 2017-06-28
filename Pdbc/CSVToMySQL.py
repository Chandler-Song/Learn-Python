import sys
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

reload(sys)
sys.setdefaultencoding('utf-8')
host = '127.0.0.1'
port = 3306
db ='test'
user = 'root'
password ='you'

engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user,password,host,db) )
try:
    df = pd.read_csv(r'C:\Users\Administrator\Desktop\hello.csv',encoding='gbk')
    print df
    df.to_sql('test',con = engine,if_exists='append',index=False)
except Exception as e:
    print e.message