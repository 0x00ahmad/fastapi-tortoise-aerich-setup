aerich init -t db.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade
poetry run python main.py
