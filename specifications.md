Conway's Game of Life is a cellular automaton modeling the evolution of living cell colonies on a 2D grid according to strict rules.

Rules of Game of Life:
Evolution occurs generation by generation. The initial distribution of living cells is the first generation. Each subsequent generation is computed according to the following rules:

- Birth: A dead cell with exactly three living neighbors becomes a living cell.
- Survival: A living cell with two or three living neighbors survives to the next generation.
- Death: A living cell dies if it has fewer than 2 neighbors (underpopulation) or more than 3 neighbors (overpopulation).

In this implementation, the game pauses or stops when the user clicks the "Stop" or "Clear" button; otherwise, evolution continues.

The player is presented with a GUI window containing an interactive canvas grid. Grid size can be adjusted between 10 cells and 50 cells per side (default is 10).
Five control buttons are provided:
- "One step": Advances evolution by exactly 1 generation (works during pause or active simulation).
- "Start": Begins automated simulation progression.
- "Stop": Pauses simulation and records current elapsed time.
- "Random": Fills approximately 25% of grid cells randomly.
- "Clear": Resets grid state, cell counts, generation counter, and timer.

Cell interactions:
- Cells display two states: dead (light background) and alive (dark background).
- Manual input: Single click on any cell in pause mode toggles cell state (alive/dead).
- Active simulation displays real-time metrics in window header: generation counter, active living cell count, and timer in seconds.
