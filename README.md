# Electrostatic Field Visualization Tool
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


## Overview
This Python-based tool simulates and visualizes electrostatic fields and electric potential distributions generated by point charges in a 2D plane. It provides two visualization modes:
- An interactive 2D plot with adjustable charge properties (magnitude and position).
- A 3D surface plot of the electric potential.
![Image](https://github.com/user-attachments/assets/fd13a219-df6d-41a4-b7f1-b60bcebe3aca)
![Image](https://github.com/user-attachments/assets/b3e0eb37-5a73-4417-a445-578f6d1c2cbd)

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

---
