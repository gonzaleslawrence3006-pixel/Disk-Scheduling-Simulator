# Disk Scheduling Algorithm Simulator

A Python-based command-line simulator and visualizer for operating system disk scheduling algorithms (**FCFS**, **SSTF**, and **SCAN**). It calculates step-by-step head movements, computes total seek distance, displays a formatted execution schedule table, and plots the head movement path using `matplotlib`.

---

## Project Structure

Keep all four Python files in the **same root folder** so module imports work properly:

```text
Platform-Tech-Final-Project-Group-5/
├── main.py       # Menu loop, input validation, and matplotlib visualization
├── fcfs.py       # First-Come, First-Served (FCFS) algorithm
├── sstf.py       # Shortest Seek Time First (SSTF) algorithm
├── scan.py       # SCAN (Elevator) algorithm
└── README.md     # Project documentation and setup guide
