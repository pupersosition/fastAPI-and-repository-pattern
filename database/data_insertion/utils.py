import time
from contextlib import contextmanager
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import OperationalError
from typing import List, Dict, Union, Any, Generator
import pandas as pd


def create_session(MAX_ATTEMPTS: int, SLEEP_INTERVAL: int, DB_USER: str, DB_PASS: str, DB_HOST: str,
                   DB_NAME: str) -> Session:
    for _ in range(MAX_ATTEMPTS):
        try:
            engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
            Session = sessionmaker(bind=engine)
            return Session()
        except OperationalError:
            time.sleep(SLEEP_INTERVAL)
    raise Exception(f"Failed to connect to the database after {MAX_ATTEMPTS} attempts.")


@contextmanager
def session_scope(MAX_ATTEMPTS: int, SLEEP_INTERVAL: int, DB_USER: str, DB_PASS: str, DB_HOST: str, DB_NAME: str) -> \
Generator[Session, None, None]:
    session = create_session(MAX_ATTEMPTS, SLEEP_INTERVAL, DB_USER, DB_PASS, DB_HOST, DB_NAME)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def bulk_insert_avoid_conflicts(session: Session, table: Table, data: List[Dict[str, Any]]) -> None:
    if not data:
        return
    insert_stmt = insert(table).values(data)
    on_conflict_stmt = insert_stmt.on_conflict_do_nothing()
    session.execute(on_conflict_stmt)


def clean_data(record: Dict[str, Any]) -> Dict[str, Union[str, None]]:
    """Replace all 'nan' values with None for database compatibility."""
    return {k: None if pd.isna(v) else v for k, v in record.items()}
