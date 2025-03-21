import yaml
with open('login_backend/config.yaml','r') as file:
    config = yaml.safe_load(file)

class Config:
    USER_DATABASE_URL = f"mysql+pymysql://{config['mysql_db']['MYSQL_USER']}:{config['mysql_db']['MYSQL_PASSWORD']}@{config['mysql_db']['HOST']}:{config['mysql_db']['PORT']}/{config['mysql_db']['USER_DB']}"