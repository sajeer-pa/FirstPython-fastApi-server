from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))
sys.path.append(BASE_DIR)

# Ensure DATABASE_URL is set
if 'DATABASE_URL' not in os.environ:
    raise EnvironmentError("DATABASE_URL environment variable not set in .env file")

# Alembic Config object, providing access to values within the .ini file
config = context.config

# Setting the sqlalchemy.url from environment variable
config.set_main_option('sqlalchemy.url', os.environ['DATABASE_URL'])

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

import models
# Add your model's MetaData object here for 'autogenerate' support
target_metadata = models.Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL and not an Engine.
    Calls to context.execute() here emit the given string to the script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
