import unittest
from os import remove
from PyLakitu.models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseTestCase(unittest.TestCase):
    '''
    This tests the basic database functionality of the Job table
    This is performed in memory by default using SQL Lite
    '''

    def setUp(self):
        #Initialize an in memory database
        self.engine = create_engine('sqlite:///:memory:')
        #Create tables from metadata
        Base.metadata.create_all(self.engine)
        #Create session maker
        self.Session = sessionmaker(bind=self.engine)

    def test_basic_database_commit(self):
        session_instance = self.Session()
        j1 = Job("localhost", "C:/windows/system32/")

        #Fill in the relationship field to the replicas
        j1.replicas=[Replica("0.1"),Replica("0.2")]

        #Confirm that the session instance contains no Jobs/Replicas yet
        self.assertTrue(session_instance.query(Job).count() is 0)
        self.assertTrue(session_instance.query(Replica).count() is 0)

        session_instance.add(j1)

        #Confirm they are in the session now
        self.assertTrue(session_instance.query(Job).count() is 1)
        self.assertTrue(session_instance.query(Replica).count() is 2)

        session_instance.commit()
        session_instance.close()

        #Confirm they were committed to the DB with a new session
        new_session_instance = self.Session()
        self.assertTrue(new_session_instance.query(Job).count() is 1)
        self.assertTrue(new_session_instance.query(Replica).count() is 2)
        new_session_instance.close()

    def test_primary_key_values(self):
        #This tests to see that primary keys are as expected
        session_instance = self.Session()
        j1 = Job("localhost", "C:/windows/system32/")
        j1.replicas=[Replica("0.1"),Replica("0.2")]
        j2 = Job("localhost", "C:/windows/system32/drivers")
        j2.replicas=[Replica("0.1"),Replica("0.2")]

        session_instance.add(j1)
        session_instance.add(j2)
        session_instance.commit()

        #Select all replicas
        q = session_instance.query(Replica).all()

        #Confirm the foreign key job ids are the same for each replica
        self.assertEqual(q[0].job_id, q[1].job_id)
        self.assertEqual(q[2].job_id, q[3].job_id)

        #Confirm the foriegn key job ids are different for unrelated reps
        self.assertNotEqual(q[1].job_id, q[2].job_id)

        session_instance.close()

class DiskDatabaseTestCase(DatabaseTestCase):
    '''
    This performs an identical test to the Default class
    but it performs it on disk and removes the database after
    '''

    def setUp(self):
        #Initialize a database on disk
        self.engine = create_engine('sqlite:///test.db')
        #Create tables from metadata
        Base.metadata.create_all(self.engine)
        #Create session maker
        self.Session = sessionmaker(bind=self.engine)

    def tearDown(self):
        remove('test.db')

if __name__ == '__main__':
    unittest.main()
