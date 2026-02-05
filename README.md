Student Performance Tracker

This project is a Python-based command-line application that manages and analyzes student academic records. It lets users input student data, store it in JSON and CSV formats, and generate statistics like averages and rankings.

## Key Features

- Data Persistence: Automatically saves student records to class_register.json and class_list.csv to ensure no data is lost between sessions.

- Statistical Analysis: Calculates the total number of students, average marks, and identifies the highest and lowest scores in the class.

- Automated Ranking: Sorts students based on their performance, from highest to lowest marks.

- Status Tracking: Automatically determines "Pass" or "Fail" status based on a 50% threshold.

## File Structure
File	Description
main.py	Contains the StudentPerformance class and the main menu logic for user interaction and file I/O.
analyzer.py	Contains the Analyzer class responsible for calculating statistics and rankings.
class_register.json	The primary storage file for student data in JSON format.
class_list.csv	A secondary export file for viewing student data in spreadsheet applications.

## How to Use

- Run the Application: Execute the program using Python:
  ```Bash

  python main.py

- Add Students: Select Option 1 to input a student's first name, surname, and numerical marks.

- View List: Select Option 2 to see a formatted table of all currently loaded students and their pass/fail status.

- Analyze Data: Select Option 3 to view class-wide statistics and a ranked leaderboard.

- Save and Exit: Select Option 4 to ensure all changes are saved before closing the program.

## Requirements

- Python 3.x

- Standard Libraries: json, csv (No external installations required).