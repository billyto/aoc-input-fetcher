import os
import sys
import argparse
import requests
from datetime import datetime
from dotenv import load_dotenv

def download_aoc_input(year, day):
    """
    Download the input file for a specific Advent of Code day.
    
    :param year: The Advent of Code year
    :param day: The day number (1-25)
    """
    # Load environment variables
    load_dotenv()
    
    # Get the session cookie from environment variable
    session_cookie = os.getenv('AOC_SESSION_COOKIE')
    
    if not session_cookie:
        print("Error: AOC_SESSION_COOKIE not found in .env file")
        sys.exit(1)
    
    # Construct the URL for the input file
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    
    # Prepare the cookies for the request
    cookies = {'session': session_cookie}
    
    try:
        # Send GET request to download the input file
        response = requests.get(url, cookies=cookies)
        
        # Raise an error for bad responses
        response.raise_for_status()
        
        # Create the inputs directory if it doesn't exist
        os.makedirs('inputs', exist_ok=True)
        
        # Save the input file
        input_path = f"inputs/day{day:02d}.txt"
        with open(input_path, 'w') as f:
            f.write(response.text.strip())
        
        print(f"Successfully downloaded input for Day {day}, {year}")
        return input_path
    
    except requests.RequestException as e:
        print(f"Error downloading input: {e}")
        sys.exit(1)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Download Advent of Code input file')
    
    # Add arguments
    parser.add_argument('day', type=int, help='Day number (1-25)')
    parser.add_argument('-y', '--year', type=int, 
                        help='Advent of Code year (default: current year)',
                        default=datetime.now().year)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate day
    if args.day < 1 or args.day > 25:
        print("Error: Day must be between 1 and 25")
        sys.exit(1)
    
    # Validate year (Advent of Code started in 2015)
    if args.year < 2015:
        print("Error: Invalid year. Advent of Code started in 2015.")
        sys.exit(1)
    
    # Download the input file
    download_aoc_input(args.year, args.day)

if __name__ == "__main__":
    main()
