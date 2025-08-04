#!/usr/bin/env python
import warnings

from hello_world_crew.crew import HelloWorldCrew
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'requirement': 'I need your help to write a hello world with Python. I only need to demo the basic function of Python to print hello world in console. No other feature required.'
    }
    
    try:
        HelloWorldCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()