# Conway's Game of Life — Desktop GUI

An interactive graphical implementation of Conway's Game of Life built in Python using `tkinter`. Features customizable grid scaling, manual initial cell layout creation, automated time tracking, dynamic population statistics, and step-by-step execution.

---

## Game Rules & Algorithm
1. **Birth:** Any dead cell with exactly 3 living neighbors becomes alive
2. **Survival:** Any living cell with 2 or 3 living neighbors stays alive
3. **Death:** Any living cell with fewer than 2 or more than 3 living neighbors dies

---

## Controls & Interface Features
* **Grid Controls:** Resize grid dynamically between `10x10` and `50x50` cells.
* **Cell Placement:** Toggle individual cell states directly on the grid using mouse clicks during pause mode.
* **Randomize:** Generates a randomized board with ~25% initial population density.
* **Control Buttons:** `Start` (auto-run simulation), `Stop` (pause timer & step count), `One step` (single generation tick), and `Clear` (wipe grid & metric counters).

---

## How to Run

### Prerequisites
* Python 3.x installed (includes built-in `tkinter`)

### Execution
1. Clone or download this repository
2. Run the application

### Repository Structure
1. main.py: Full GUI interface implementation and cellular automaton engine.
2. specifications.md: Official task specifications and game mechanics.
3. examples.txt: Standard cellular patterns and coordinates for testing (Blinker, Glider, Corner, etc.).
