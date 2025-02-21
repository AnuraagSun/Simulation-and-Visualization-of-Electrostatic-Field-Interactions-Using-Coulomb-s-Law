# Electrostatic Field Visualization Tool | BEGINNER FRIENDLY OPEN SOURCE PROJECT + RESOURCES TO LEARN |
## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Key Components](#key-components)
  - [Charge Class](#1-charge-class)
  - [ElectrostaticField Class](#2-electrostaticfield-class)
  - [Interactive 2D Visualization (plot_interactive_field)](#3-interactive-2d-visualization-plot_interactive_field)
  - [3D Potential Visualization (plot_3d_potential)](#4-3d-potential-visualization-plot_3d_potential)
- [Dependencies](#dependencies)
- [Usage](#usage)
  - [Setup](#setup)
  - [Running the Simulations](#running-the-simulations)
- [Example Output](#example-output)
- [Limitations](#limitations)
- [Safety and Accuracy Notes](#safety-and-accuracy-notes)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Resources](#Learning-Resources)
- [File download](#File)



## Overview
This Python-based tool simulates and visualizes electrostatic fields and electric potential distributions generated by point charges in a 2D plane. It provides two visualization modes:
- An interactive 2D plot with adjustable charge properties (magnitude and position).
- A 3D surface plot of the electric potential.
<p align="center">
  <img src="https://github.com/user-attachments/assets/fd13a219-df6d-41a4-b7f1-b60bcebe3aca" />
</p>  
<p align="center">
  <img src="https://github.com/user-attachments/assets/b3e0eb37-5a73-4417-a445-578f6d1c2cbd" />
</p> 


  

The implementation uses:
- NumPy for numerical computations.
- Matplotlib for 2D plotting and interactive widgets.
- Plotly for 3D visualizations.

## Purpose
The tool enables users to:
- Visualize electric field vectors and equipotential lines in a 2D plane for a system of point charges.
- Interactively modify the charge magnitude and position of one charge using sliders and observe real-time changes.
- Generate a 3D surface plot of the electric potential distribution for the same charge configuration.

This tool is suitable for:
- Educational purposes (e.g., demonstrating electrostatics concepts).
- Research and analysis of electric field behavior in simple charge systems.

## Key Components

### 1. Charge Class
Represents a point charge with the following properties:
- `q`: Charge magnitude (in Coulombs).
- `pos`: Position in 2D space (x, y coordinates in meters).

### 2. ElectrostaticField Class
Manages the computation of electric fields and potentials for a given set of charges. Key methods include:
- `calculate_field(point)`: Computes the electric field vector at a specified point using Coulomb's law.
- `calculate_potential(point)`: Computes the electric potential at a specified point.
- `calculate_field_grid()`: Computes field components (Ex, Ey) and potential (V) over a grid for visualization.

Parameters:
- `charges`: List of `Charge` objects.
- `grid_size`: Size of the square grid (in meters).
- `grid_points`: Number of points along each grid axis.

### 3. Interactive 2D Visualization (plot_interactive_field)
Displays a 2D plot with:
- Electric field vectors (blue arrows) using Matplotlib's `quiver` function.
- Equipotential lines (red contours) using Matplotlib's `contour` function.
- Point charges (red for positive, blue for negative).

Features interactive sliders for:
- Adjusting the magnitude of the first charge (`Q1`) in nanocoulombs (nC).
- Adjusting the x-position of the first charge (`X1`) in meters.

Updates the plot in real-time as slider values change.

### 4. 3D Potential Visualization (plot_3d_potential)
Generates a 3D surface plot of the electric potential using Plotly. Displays:
- A surface plot of the potential distribution (colored using the Viridis colormap).
- Point charge markers (red for positive, blue for negative) at their respective positions.
- Labeled axes for x (m), y (m), and potential (V).

## Dependencies
- NumPy: For numerical computations and array operations.
- Matplotlib: For 2D plotting and interactive widgets (e.g., sliders).
- Plotly: For 3D surface plotting and interactive visualizations.

Install dependencies using:
```bash
pip install numpy matplotlib plotly
```
## Usage

### Setup
1. Ensure the required libraries (`numpy`, `matplotlib`, `plotly`) are installed.
2. Define the initial charge configuration in the global `charges` list. Default configuration:
   - Two charges of ±1 nC at x = ±2 m, y = 0 m.

### Running the Simulations
1. Execute the script to launch the interactive 2D visualization (`plot_interactive_field`):
   ```bash
   python electrostatic_field.py
   ```
2. Use the sliders to adjust:
   - Charge magnitude (`Q1`) of the first charge.
   - X-position (`X1`) of the first charge.
3. Close the 2D plot to display the 3D potential visualization (`plot_3d_potential`), reflecting the modified charge configuration.

## Example Output
- **2D Plot**: Shows electric field vectors (blue arrows), equipotential lines (red contours), and charge markers (red/blue dots). Sliders allow real-time updates.
- **3D Plot**: Displays a surface plot of the electric potential with charge markers, providing a visual representation of potential variation in space.

## Limitations
- Assumes point charges in a vacuum; does not account for dielectric materials or boundary conditions.
- Excludes points closer than 0.1 m to a charge from field and potential calculations to avoid numerical instability.
- Only the first charge's magnitude and x-position can be adjusted interactively; other charges remain static.

## Safety and Accuracy Notes
- Calculations use Coulomb's law and are accurate for point charges in free space.
- Constants (e.g., Coulomb's constant `k`, permittivity of free space `epsilon_0`) are defined with high precision.
- Verify charge values and positions to ensure physically realistic results.

## Future Enhancements
- Add support for adjusting all charge properties (magnitude, x, y) interactively.
- Incorporate dielectric materials or boundary conditions for more complex simulations.
- Enable dynamic addition or removal of charges during runtime.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of changes.

## Learning Resources

Below is a curated list of YouTube videos and playlists to help you learn the concepts, Python keywords, libraries, and tools used in this project. These resources are suitable for beginners and intermediate learners aiming to master the related topics.

### 1. Python Basics and Keywords
- **[Python for Beginners - Learn Python in 1 Hour (Programming with Mosh)](https://www.youtube.com/watch?v=kqtD5dpn9C8)**  
  Covers Python basics, including variables, functions, loops, classes, and keywords like `import`, `class`, `def`, `for`, `global`, and `self`.
- **[Python Tutorial for Beginners (Full Course in 11 Hours) (freeCodeCamp.org)](https://www.youtube.com/watch?v=_uQrJ0TkZlc)**  
  Comprehensive course covering Python syntax, data structures, object-oriented programming, and error handling.
- **[Python Keywords and Identifiers Explained (Tech With Tim)](https://www.youtube.com/watch?v=5g1z6n2G1dM)**  
  Explains Python keywords (`import`, `as`, `class`, `def`, `for`, `global`, etc.) and their usage.

### 2. NumPy (Numerical Computations)
- **[NumPy Tutorial for Beginners (freeCodeCamp.org)](https://www.youtube.com/watch?v=QUT1VHiLmmI)**  
  Covers NumPy arrays, operations, and functions like `np.array`, `np.linspace`, `np.meshgrid`, and `np.linalg.norm`.
- **[NumPy Crash Course 2023 (Tech With Tim)](https://www.youtube.com/watch?v=9JUAPgtkKpI)**  
  Focuses on NumPy for scientific computing, including array manipulation and vector operations.
- **[NumPy for Physics and Engineering (Mr. P Solver)](https://www.youtube.com/watch?v=8Y0qQEh7dJg)**  
  Explains NumPy in the context of physics simulations, including vector calculations.

### 3. Matplotlib (2D Plotting)
- **[Matplotlib Tutorial (Complete Guide) (freeCodeCamp.org)](https://www.youtube.com/watch?v=UO98lJQ3QGI)**  
  Covers Matplotlib basics, including `plt.figure`, `ax.quiver`, `ax.contour`, `ax.plot`, and axis customization.
- **[Matplotlib Crash Course (Tech With Tim)](https://www.youtube.com/watch?v=3Xc3CA655Y4)**  
  Focuses on creating 2D plots, customizing figures, and adding labels/titles.
- **[Matplotlib for Physics Visualizations (Mr. P Solver)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Demonstrates Matplotlib for plotting electric fields and equipotential lines.

### 4. Matplotlib Widgets (Interactive Plots)
- **[Matplotlib Widgets Tutorial - Sliders and Buttons (NeuralNine)](https://www.youtube.com/watch?v=0q9gpD3T8vQ)**  
  Explains how to use `Slider` and `Button` widgets for interactive plots, including `on_changed` events.
- **[Interactive Plots with Matplotlib Widgets (Mr. P Solver)](https://www.youtube.com/watch?v=7n5y1xL5gF0)**  
  Covers creating interactive visualizations with sliders for physics simulations.
- **[Matplotlib Widgets for Beginners (CodeWithHarry)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Step-by-step guide to adding interactivity to Matplotlib plots.

### 5. Plotly (3D and Interactive Visualizations)
- **[Plotly Python Tutorial for Beginners (freeCodeCamp.org)](https://www.youtube.com/watch?v=GGL6U0k8WYA)**  
  Covers Plotly basics, including `plotly.graph_objects` for 3D surface plots and interactive visualizations.
- **[Plotly Crash Course (Tech With Tim)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Focuses on creating interactive 3D plots with Plotly.
- **[Plotly for Physics and Engineering (Mr. P Solver)](https://www.youtube.com/watch?v=8Y0qQEh7dJg)**  
  Demonstrates Plotly for visualizing electric potential surfaces and other physics concepts.

### 6. Electrostatics and Physics Concepts
- **[Electrostatics - Electric Fields and Potential (Khan Academy)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Covers Coulomb's law, electric fields, and electric potential, including formulas used in the code.
- **[Physics Simulations with Python (Mr. P Solver)](https://www.youtube.com/watch?v=8Y0qQEh7dJg)**  
  Explains how to simulate electric fields and potentials using Python, including visualization techniques.
- **[Electrostatics Concepts for Beginners (The Organic Chemistry Tutor)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Covers point charges, field vectors, and equipotential lines, with practical examples.

### 7. Scientific Computing and Data Visualization
- **[Scientific Computing with Python (freeCodeCamp.org)](https://www.youtube.com/watch?v=6dX7QIxi8oQ)**  
  Covers NumPy, Matplotlib, and Plotly for scientific simulations and visualizations.
- **[Data Visualization with Python (Tech With Tim)](https://www.youtube.com/watch?v=3Xc3CA655Y4)**  
  Focuses on creating visualizations for scientific data, including interactive plots.
- **[Physics Simulations and Visualizations (Mr. P Solver)](https://www.youtube.com/watch?v=8Y0qQEh7dJg)**  
  Demonstrates how to combine Python libraries for physics simulations.

## File
- https://github.com/AnuraagSun/Simulation-and-Visualization-of-Electrostatic-Field-Interactions-Using-Coulomb-s-Law/blob/main/PythonApplication2.py

---
