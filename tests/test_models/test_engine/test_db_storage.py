#!/usr/bin/python3
"""
Module for testing DB storage
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_db_storage(unittest.TestCase):
    """
    """

    def test_all_users(db):
        """Test retrieving all User objects."""
        users = db.all(User)
        assert len(users) > 0
        for user_id, user in users.items():
            assert isinstance(user, User)

    def test_all_states(db):
        """Test retrieving all State objects."""
        states = db.all(State)
        assert len(states) > 0
        for state_id, state in states.items():
            assert isinstance(state, State)

    def test_new_user(db):
        """Test adding a new User object to the database."""
        user = User(email="test@email.com", password="test_password")
        db.new(user)
        db.save()

        users = db.all(User)
        assert user.id in users
        assert users[user.id] == user

    def test_save_user(db):
        """Test saving changes to a User object."""
        user = User(email="test@email.com", password="test_password")
        db.new(user)
        db.save()

        user.email = "updated@email.com"
        db.save()

        users = db.all(User)
        assert users[user.id].email == "updated@email.com"

    def test_delete_user(db):
        """Test deleting a User object from the database."""
        user = User(email="test@email.com", password="test_password")
        db.new(user)
        db.save()

        db.delete(user)
        db.save()

        users = db.all(User)
        assert user.id not in users

    def test_reload(db):
        """Test reloading the database and creating a new session."""
        # Create some objects and save them to the database
        user = User(email="test@email.com", password="test_password")
        db.new(user)
        db.save()

        # Reload the database
        db.reload()

        # Query for the user again
        users = db.all(User)
        assert user.id in users
        assert users[user.id] == user

    def test_close(db):
        """Test closing the database session."""
        # Create a session and close it
        db.close()

        # Try to query the database again
        with pytest.raises(Exception):
            db.all(User)


if __name__ == "__main__":
    unittest.main()
