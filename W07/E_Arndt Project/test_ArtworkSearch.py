# Author: Eric Arndt
# Class: CSE 111 Student Project - TEST Artwork Search
# Program that tests the db_query function of the Artwork Search program.
# Two arguments will be passed to the function, an SQL Query statement and a number (artist_id).
# Testing the db_query function will also test the connection to the v_art database,
# the execution of the SQL Query Statement and the Result String of that Query.


from ArtworkSearch import db_query
import pytest


def test_db_queery():

    assert db_query("SELECT artist_id, fname, lname FROM artist WHERE artist_id = %s", (8, )) == ([(8, 'Michelangelo', 'Simoni')])
    assert db_query("SELECT artist_id, fname, lname FROM artist WHERE artist_id = %s", (5, )) == ([(5, 'Deborah', 'Gill')])
    assert db_query("SELECT artist_id, fname, lname FROM artist WHERE artist_id = %s", (2, )) == ([(2, 'Rembrandt', 'van Rijn')])
    assert db_query("SELECT artist_id, fname, lname FROM artist WHERE artist_id = %s", (6, )) == ([(6, 'Claude', 'Monet')])





pytest.main(["-s", "-v", "--tb=line", "-rN", __file__])