from sqlalchemy import create_engine, URL, MetaData

url_object = URL.create(
    "mysql",
    username="root",
    password="#eM#3X76*y",
    host="localhost",
    database="rioservice"
)

engine = create_engine(url_object, echo=True)

metadata_obj = MetaData()