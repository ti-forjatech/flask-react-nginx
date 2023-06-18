from sqlalchemy import create_engine, URL, MetaData
from dotenv import dotenv_values

env = dotenv_values(".env")

url_object = URL.create(
    "mysql",
    username=env["DB_USER"],
    password=env["DB_PASSWORD"],
    host=env["DB_HOST"],
    database=env["DB_NAME"],
)

engine = create_engine(url_object, echo=True)

metadata_obj = MetaData()