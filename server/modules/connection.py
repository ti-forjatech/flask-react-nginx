from sqlalchemy import create_engine, URL, MetaData
import os

url_object = URL.create(
    "mysql",
    username=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    host="rioservice_db",
    database=os.environ.get("MYSQL_DATABASE"),
    port=3306
)

engine = create_engine(url_object, echo=True)

metadata_obj = MetaData()