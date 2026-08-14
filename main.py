import tkinter as tk
import random
import time


min_size = 10  # Minimum and maximum grid size
max_size = 50
size_of_cell = 15  # Cell size in pixels
delay = 300  # Delay in milliseconds between generations


class GameOfLife:
    def __init__(self, root):  # Initialize game, create GUI interface
        self.root = root
        self.root.title("Game of Life")
        self.size = min_size  # Initial grid size is minimum
        self.grid = []  # 2D list storing cell states (alive/dead - 1/0)
        self.running = False  # Simulation active status
        self.generation = 0  # Generation counter
        self.start_time = None  # Start timestamp
        self.elapsed_time = 0.0  # Elapsed time counter

        self.create_widgets()  # Create GUI widgets
        self.reset_grid()  # Initialize empty grid of given size

    def create_widgets(self):  # Main function creating all game widgets
        self.canvas = tk.Canvas(  # Interactive canvas grid for clicking cells
            self.root,
            bg='#DCE2F0',
            width=self.size * size_of_cell,
            height=self.size * size_of_cell,
            highlightthickness=0  # Remove border around grid
        )
        self.canvas.pack(padx=0, pady=0)  # Place grid without margins

        control_frame = tk.Frame(self.root)  # Control window frame
        control_frame.pack(pady=5)
        # Create five main game control buttons
        tk.Button(control_frame, text="One step", command=self.step).pack(side=tk.LEFT, padx=3)
        tk.Button(control_frame, text="Start", command=self.start).pack(side=tk.LEFT, padx=3)
        tk.Button(control_frame, text="Stop", command=self.stop).pack(side=tk.LEFT, padx=3)
        tk.Button(control_frame, text="Random", command=self.randomize).pack(side=tk.LEFT, padx=3)
        tk.Button(control_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=3)

        size_frame = tk.Frame(self.root)  # Frame for grid size controls
        size_frame.pack(pady=5)
        tk.Label(size_frame, text="Grid size (10–50):").pack(side=tk.LEFT)
        self.size_var = tk.StringVar(value=str(self.size))
        size_entry = tk.Entry(size_frame, textvariable=self.size_var, width=5)
        size_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(size_frame, text="Apply", command=self.apply_size).pack(side=tk.LEFT)  # Apply new grid size

        self.canvas.bind("<Button-1>", self.on_canvas_click)  # Click handler for manual cell filling

        self.root.after(100, self.auto_step)  # Run auto_step every 100 ms to handle generation ticks

    def apply_size(self):  # Takes grid size input, validates range, and updates grid size
        new_size = int(self.size_var.get())
        if min_size <= new_size <= max_size:
            self.size = new_size
            self.reset_grid()
            self.canvas.config(width=self.size * size_of_cell, height=self.size * size_of_cell)
            self.draw()
        else:  # Raise error if outside permissible bounds
            tk.messagebox.showerror("Error", f"Size must be from {min_size} to {max_size}")

    def reset_grid(self):  # Resets grid to empty and clears all metrics
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.generation = 0
        self.elapsed_time = 0.0
        self.start_time = None
        self.running = False

    def neighbours_counter(self, y, x):  # Counts living neighbors surrounding a cell
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                ny, nx = y + dy, x + dx  # Check boundary limits
                if 0 <= ny < self.size and 0 <= nx < self.size:
                    count += self.grid[ny][nx]
        return count

    def step(self):  # Advances simulation by one generation
        new_grid = [[0 for _ in range(self.size)] for _ in range(self.size)]  # Prepare next grid iteration
        for y in range(self.size):
            for x in range(self.size):
                neighbors = self.neighbours_counter(y, x)  # Update cell states according to game rules
                if self.grid[y][x] == 1:
                    new_grid[y][x] = 1 if neighbors in (2, 3) else 0
                else:
                    new_grid[y][x] = 1 if neighbors == 3 else 0
        self.grid = new_grid
        self.generation += 1
        self.draw()  # Redraw canvas

    def auto_step(self):  # Handles game loop progression while active
        if self.running:
            self.step()
        self.root.after(delay, self.auto_step)  # Trigger next evaluation after delay

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time  # Continue timing

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time  # Save current elapsed time

    def randomize(self):  # Randomly populates grid
        self.stop()
        for y in range(self.size):
            for x in range(self.size):
                self.grid[y][x] = 1 if random.random() < 0.25 else 0  # Fill approx 25% cells
        self.generation = 0
        self.elapsed_time = 0.0
        self.start_time = None
        self.draw()

    def clear(self):  # Grid reset function
        self.stop()
        self.reset_grid()
        self.draw()

    def on_canvas_click(self, event):  # Canvas click handler
        if self.running:
            return  # Manual editing allowed only during pause
        x = event.x // size_of_cell
        y = event.y // size_of_cell
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[y][x] = 1 - self.grid[y][x]
            self.draw()

    def draw(self):  # Renders grid and updates status indicators
        alive_count = sum(sum(row) for row in self.grid)  # Count living cells

        if self.running:  # Track time
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        self.root.title(  # Update title bar status
            f"Game of Life — generation {self.generation} | "
            f"alive: {alive_count} | "
            f"time: {current_time:.1f} s"
        )

        # Rendering
        self.canvas.delete("all")
        for y in range(self.size):
            for x in range(self.size):
                color = "#50586C" if self.grid[y][x] else "#DCE2F0"
                self.canvas.create_rectangle(
                    x * size_of_cell, y * size_of_cell,
                    (x + 1) * size_of_cell, (y + 1) * size_of_cell,
                    fill=color, outline="#6A7BA2", width=1
                )

def main():  # Application entry point
    root = tk.Tk()  # Create root window
    GameOfLife(root)  # Initialize game
    root.mainloop()  # Run event loop

main()
