#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' 
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
    for state_obj in session.query(State).order_by(State.id):
        if "a" in state_obj.name:
            print("{}: {}".format(state_obj.id, state_obj.name))
    session.close()
