from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib
import os


host_server = os.environ.get('host_server', 'hdmysql.mysql.database.azure.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '3306')))
database_name = os.environ.get('database_name', 'hds')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'AbracaData2022@hdmysql')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'abdata@2022')))
SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(db_username,db_password,host_server,db_server_port,database_name)


engine = create_engine(
    #DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL, pool_size=3, max_overflow=0
)


SessionLocal= sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()