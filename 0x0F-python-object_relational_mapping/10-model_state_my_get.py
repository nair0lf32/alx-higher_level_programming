#!/usr/bin/python3
"""Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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
    state_obj = session.query(State).filter(State.name == sys.argv[4]).first()
    if state_obj.name is not None:
        print("{}".format(state_obj.id))
    else:
        print("Not found")
    session.close()
