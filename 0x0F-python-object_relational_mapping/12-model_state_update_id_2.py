#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    session = Session(bind=engine)
    session.query(State).filter(State.id == 2).update(
        {State.name: "New Mexico"}, synchronize_session=False)
    session.commit()
    session.close()
