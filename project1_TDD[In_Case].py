# Created for Backend and Front End Testing using pytest module unit tests
# Date: Friday October 27 2023 
# Instructions: please run command: pytest # in master directory for testing project-1-web-application-design-group30-bytes

import pytest
import datetime
import json
from pathlib import Path
import psycopg2
import os


# Test suite 1: Database creation and Table Existence 

# Test 1: Database existence: 
def test_flask_database():
    """Ensure that the flask database exists"""
    try:
        # Establish connection using the same db.py file os variables
        conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD']
        )
        # If connection is successful, close it and assert True
        conn.close()
        assert True
    except Exception:
        assert False, "Database does not exist or connection failed"

# Test 2 User table Exists? :
def test_user_table_exists():
    """Ensure that the specified user exists"""
    table_name = "users"  # Replace with the name of table

    try:
        # Establish connection using the environment variables
        conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        
        # Create a new cursor
        cur = conn.cursor()

        # Execute a query to check if the table exists
        cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name= %s);", (table_name,))

        # Fetch the result
        exists = cur.fetchone()[0]

        # Close the cursor and the connection
        cur.close()
        conn.close()

        # Assert that the table exists
        assert exists, f"Table '{table_name}' does not exist in the database."

    except Exception as e:
        assert False, str(e)

# Test 3 Event table Exists? : 
def test_event_table_exists():
    """Ensure that the specified user exists"""
    table_name = "events"  # Replace with the name of the table 

    try:
        # Establish connection using the environment variables
        conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        
        # Create a new cursor
        cur = conn.cursor()

        # Execute a query to check if the table exists
        cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name= %s);", (table_name,))

        # Fetch the result
        exists = cur.fetchone()[0]

        # Close the cursor and the connection
        cur.close()
        conn.close()

        # Assert that the table exists
        assert exists, f"Table '{table_name}' does not exist in the database."

    except Exception as e:
        assert False, str(e)

# Test 4 ratings table Exists? : 
def test_ratings_table_exists():
    """Ensure that the specified user exists"""
    table_name = "ratings"  # Replace with the name of the table 

    try:
        # Establish connection using the environment variables
        conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        
        # Create a new cursor
        cur = conn.cursor()

        # Execute a query to check if the table exists
        cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name= %s);", (table_name,))

        # Fetch the result
        exists = cur.fetchone()[0]

        # Close the cursor and the connection
        cur.close()
        conn.close()

        # Assert that the table exists
        assert exists, f"Table '{table_name}' does not exist in the database."

    except Exception as e:
        assert False, str(e)

# Test 5: RSVP table exists? : 
def test_rsvp_table_exists():
    """Ensure that the specified user exists"""
    table_name = "rsvp"  # Replace with the name of the table 

    try:
        # Establish connection using the environment variables
        conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        
        # Create a new cursor
        cur = conn.cursor()

        # Execute a query to check if the table exists
        cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name= %s);", (table_name,))

        # Fetch the result
        exists = cur.fetchone()[0]

        # Close the cursor and the connection
        cur.close()
        conn.close()

        # Assert that the table exists
        assert exists, f"Table '{table_name}' does not exist in the database."

    except Exception as e:
        assert False, str(e)

# Test suite 2:  Data insertion Tests

#Test 6 - Can users be added? : 
def test_adding_users_to_db():
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    cur = conn.cursor()

    # Insert a record 
    test_user_id = 9999  # Some unique ID for testing purposes
    test_user_name = "TestUser"
    cur.execute("INSERT INTO users (id, name) VALUES (%s, %s);", (test_user_id, test_user_name))
    conn.commit()

    # Check if the record was inserted
    cur.execute("SELECT * FROM users WHERE id = %s;", (test_user_id,))
    assert cur.fetchone() is not None, "Failed to insert the test record."

    # Delete the record
    cur.execute("DELETE FROM users WHERE id = %s;", (test_user_id,))
    conn.commit()

    # Check if the record was deleted
    cur.execute("SELECT * FROM users WHERE id = %s;", (test_user_id,))
    assert cur.fetchone() is None, "Failed to delete the test record."

    # Close the connection
    cur.close()
    conn.close()

# Test 7: Foreign Key logic Handling for adding a rating? - Made by Haris Rasul
def test_add_rating():
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    cur = conn.cursor()

    # Insert a test user
    test_user_name = "TestUserForRating"
    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (test_user_name,))
    test_user_id = cur.fetchone()[0]
    conn.commit()

    # Insert a test event
    test_event_title = "TestEventForRating"
    test_event_description = "This is a test event for the rating system."
    test_event_location = "TestLocation"
    cur.execute("INSERT INTO events (title, organizer_id, description, location, date) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING id;", (test_event_title, test_user_id, test_event_description, test_event_location))
    test_event_id = cur.fetchone()[0]
    conn.commit()

    # Insert a rating
    test_rating = 4
    test_comment = "Great event!"
    cur.execute("INSERT INTO ratings (author, event, rating, comment, date) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP);", (test_user_id, test_event_id, test_rating, test_comment))
    conn.commit()

    # Check if the rating was inserted
    cur.execute("SELECT rating, comment FROM ratings WHERE author = %s AND event = %s;", (test_user_id, test_event_id))
    fetched_rating, fetched_comment = cur.fetchone()
    assert fetched_rating == test_rating, "Failed to insert the correct rating."
    assert fetched_comment == test_comment, "Failed to insert the correct comment."

    # Cleanup: delete the inserted data
    cur.execute("DELETE FROM ratings WHERE author = %s AND event = %s;", (test_user_id, test_event_id))
    conn.commit()
    cur.execute("DELETE FROM events WHERE id = %s;", (test_event_id,))
    conn.commit()
    cur.execute("DELETE FROM users WHERE id = %s;", (test_user_id,))
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()


# Test Suite 3: Front-End Test cases 
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Test 8: Does the home page render or not?: Made By Haris Rasul
def test_react_webapp_render():
    """Ensure the React web app home page renders successfully"""

    # React Path - please run from main directory when running pytest 
    react_app_path = "frontend/fly-high"
    
    # npm start in front end directory for testing 
    process = subprocess.Popen(["npm", "start"], cwd=react_app_path)
    
    # Give some time for the app to start up. before going on with the info scrapijn g 
    time.sleep(10)

    # Set up the path to chrome driver for tag extraction, install chrome driver and work with sleenium 
    chromedriver_path = ChromeDriverManager().install()
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    
    # set up chromdriver settings to enusre no error with system compatibility
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # optional, run browser in the background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # React local host by default 
        driver.get("http://localhost:3000")

        
        #print("waiting")
        driver.implicitly_wait(10)  # 10 seconds to extract something before timeout forcing
        #print("getting element")
        
        element = driver.find_element(By.TAG_NAME, "body") #extract the main ody tag to ensure dahsboard homepage loaded
        #print("got element")
        
        # No error: the element was found = page rendered successfully
        assert element is not None, "React app did not render successfully"

    finally:
        # close the browser for clean up
        driver.quit()
        
        # Terminate the React 
        process.terminate()
