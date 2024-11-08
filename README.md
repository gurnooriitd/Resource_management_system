# Distributed Resource Management System

## Project Overview
This project simulates a distributed system for efficiently scheduling and managing tasks across multiple processing units. It uses a heap structure to distribute tasks based on load balancing and priority policies.

## Features
- **Heap-based Task Distribution**: Assigns tasks to the processing unit with the lowest current load, utilizing efficient heap operations.
- **Optimized Time Complexities**:
  - **Initialization**: `O(m)`
  - **Adding Tasks**: `O(log n + log m)`
  - **Completion Time Retrieval**: `O(n(log n + log m))`

## Files
Download the files and run the project directly:

- `strawhat.py`: Manages task distribution and scheduling logic.
- `crewmate.py`: Defines the processing unit and task queue management.
- `heap.py`: Implements the heap structure for prioritizing tasks.
- `main.py`: Defines task properties like ID, size, and arrival time.

## Usage
1. Download the project files and place them in a single directory.
2. Run the main script to initialize the scheduler and add tasks.

---
"""
