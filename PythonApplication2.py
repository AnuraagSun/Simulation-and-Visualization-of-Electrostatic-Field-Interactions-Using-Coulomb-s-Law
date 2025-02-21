# Import required libraries
# 'import' keyword: Used to include external libraries or modules in your code.
# Syntax: import <library_name> [as <alias>]
# 'as' keyword: Allows you to give a shorter or more convenient name (alias) to the library.
# Here, we import:
# - numpy: A library for numerical computations, especially with arrays and matrices.
# - matplotlib.pyplot: A plotting library for creating 2D visualizations (like graphs and plots).
# - matplotlib.widgets: A module within matplotlib that provides interactive widgets like sliders and buttons.
# - plotly.graph_objects: A library for creating interactive 3D and 2D visualizations, often used for web-based plots.

import numpy as np  # 'np' is a common alias for numpy, making it easier to type.
import matplotlib.pyplot as plt  # 'plt' is a common alias for matplotlib.pyplot.
from matplotlib.widgets import Slider, Button  # Import specific classes (Slider, Button) from matplotlib.widgets.
import plotly.graph_objects as go  # 'go' is a common alias for plotly.graph_objects.

# Define physical constants
# These are fundamental constants used in electrostatics calculations.
# 'k' is Coulomb's constant, which relates the strength of the electric force between charges.
# Its value is approximately 8.9875517923e9 N⋅m²/C² (Newton-meter squared per Coulomb squared).
k = 8.9875517923e9  # Coulomb's constant (N⋅m²/C²)

# 'epsilon_0' is the permittivity of free space, a measure of how electric fields propagate in a vacuum.
# Its value is approximately 8.854187817e-12 F/m (Farads per meter).
epsilon_0 = 8.854187817e-12  # Permittivity of free space (F/m)

# Define a class to represent a point charge
# 'class' keyword: Used to define a new class, which is a blueprint for creating objects.
# Syntax: class <ClassName>:
# A class can have attributes (data) and methods (functions) associated with it.
# Here, we define a 'Charge' class to represent a point charge with a charge value and position.

class Charge:
    # '__init__' method: This is the constructor, called when a new Charge object is created.
    # 'self' keyword: Refers to the instance of the class (the object itself).
    # It is used to access attributes and methods of the class.
    # Syntax: def __init__(self, <parameters>):
    # Parameters:
    # - q: The charge value in Coulombs (C).
    # - x, y: The x and y coordinates of the charge's position in meters (m).
    def __init__(self, q, x, y):
        # Assign the charge value (q) to the instance variable 'self.q'.
        self.q = q  # Charge value in Coulombs
        # Create a numpy array for the position [x, y] and assign it to 'self.pos'.
        # 'np.array' function: Converts a list or tuple into a numpy array for efficient numerical operations.
        # Syntax: np.array([<elements>])
        self.pos = np.array([x, y])  # Position in meters

# Define a class to represent the electrostatic field
# This class handles calculations and visualizations for the electric field and potential.
class ElectrostaticField:
    # Constructor for the ElectrostaticField class.
    # Parameters:
    # - charges: A list of Charge objects.
    # - grid_size: The size of the grid (in meters) for field calculations (default is 10 meters).
    # - grid_points: The number of points along each axis of the grid (default is 30 points).
    def __init__(self, charges, grid_size=10, grid_points=30):
        # Assign the list of charges to 'self.charges'.
        self.charges = charges
        # Assign the grid size to 'self.grid_size'.
        self.grid_size = grid_size
        # Assign the number of grid points to 'self.grid_points'.
        self.grid_points = grid_points
        
        # Create a grid for field calculations
        # 'np.linspace' function: Creates an array of evenly spaced points over a specified range.
        # Syntax: np.linspace(start, stop, num)
        # - start: Starting value (-grid_size/2).
        # - stop: Ending value (grid_size/2).
        # - num: Number of points (grid_points).
        # This creates arrays 'x' and 'y' for the grid coordinates.
        x = np.linspace(-grid_size/2, grid_size/2, grid_points)
        y = np.linspace(-grid_size/2, grid_size/2, grid_points)
        
        # Create a mesh grid for 2D calculations
        # 'np.meshgrid' function: Converts 1D arrays into 2D grids for coordinate calculations.
        # Syntax: np.meshgrid(x, y)
        # - 'self.X' and 'self.Y' are 2D arrays representing the x and y coordinates of the grid.
        self.X, self.Y = np.meshgrid(x, y)

    # Method to calculate the electric field at a specific point
    # Parameters:
    # - point: A 2D point [x, y] where the field is calculated.
    def calculate_field(self, point):
        """Calculate electric field at a point due to all charges"""
        # Initialize the total electric field (E_total) as a 2D zero vector [0, 0].
        # 'np.zeros' function: Creates an array filled with zeros.
        # Syntax: np.zeros(shape)
        E_total = np.zeros(2)
        # Convert the input point to a numpy array for vector operations.
        point = np.array(point)
        
        # Loop through each charge in the list of charges
        # 'for' keyword: Used to iterate over a sequence (like a list).
        # Syntax: for <variable> in <sequence>:
        for charge in self.charges:
            # Calculate the displacement vector (r) from the charge to the point.
            r = point - charge.pos
            # Calculate the magnitude of the displacement vector.
            # 'np.linalg.norm' function: Computes the Euclidean norm (length) of a vector.
            # Syntax: np.linalg.norm(vector)
            r_magnitude = np.linalg.norm(r)
            # Avoid division by zero by skipping points too close to the charge.
            if r_magnitude < 0.1:
                continue
            # Calculate the electric field contribution from this charge using Coulomb's law.
            # Formula: E = k * q * r / |r|^3, where k is Coulomb's constant.
            E = k * charge.q * r / (r_magnitude**3)
            # Add the field contribution to the total field.
            E_total += E
        # Return the total electric field vector [Ex, Ey].
        return E_total

    # Method to calculate the electric potential at a specific point
    # Parameters:
    # - point: A 2D point [x, y] where the potential is calculated.
    def calculate_potential(self, point):
        """Calculate electric potential at a point"""
        # Initialize the total electric potential (V_total) to zero.
        V_total = 0
        # Convert the input point to a numpy array.
        point = np.array(point)
        
        # Loop through each charge in the list of charges
        for charge in self.charges:
            # Calculate the distance (r) from the charge to the point.
            r = np.linalg.norm(point - charge.pos)
            # Avoid division by zero by skipping points too close to the charge.
            if r < 0.1:
                continue
            # Calculate the potential contribution from this charge.
            # Formula: V = k * q / r, where k is Coulomb's constant.
            V = k * charge.q / r
            # Add the potential contribution to the total potential.
            V_total += V
        # Return the total electric potential.
        return V_total

    # Method to calculate the electric field and potential over the entire grid
    def calculate_field_grid(self):
        """Calculate field components over the entire grid"""
        # Initialize 2D arrays for the x and y components of the electric field (Ex, Ey).
        # 'np.zeros_like' function: Creates an array of zeros with the same shape as the input array.
        # Syntax: np.zeros_like(array)
        Ex = np.zeros_like(self.X)
        Ey = np.zeros_like(self.Y)
        # Initialize a 2D array for the electric potential (V).
        V = np.zeros_like(self.X)

        # Loop through each point in the grid
        for i in range(self.grid_points):
            for j in range(self.grid_points):
                # Get the coordinates of the current grid point.
                point = [self.X[i,j], self.Y[i,j]]
                # Calculate the electric field at this point.
                E = self.calculate_field(point)
                # Store the x and y components of the field.
                Ex[i,j] = E[0]
                Ey[i,j] = E[1]
                # Calculate the potential at this point.
                V[i,j] = self.calculate_potential(point)
        
        # Return the field components (Ex, Ey) and potential (V).
        
        return Ex, Ey, V

# Define a global list of charges
# 'global' keyword: Used to declare that a variable is defined in the global scope.
# This means the variable can be accessed and modified anywhere in the code.
# Here, we create a list of Charge objects to represent point charges.
charges = [
    # Create a positive charge with q = 1e-9 C (1 nanocoulomb) at position (-2, 0).
    Charge(1e-9, -2, 0),  # Positive charge
    # Create a negative charge with q = -1e-9 C (-1 nanocoulomb) at position (2, 0).
    Charge(-1e-9, 2, 0)   # Negative charge
]

# Define a function for interactive 2D visualization
# 'def' keyword: Used to define a function.
# Syntax: def <function_name>(<parameters>):
def plot_interactive_field():
    # Use the global 'charges' list defined earlier.
    # This allows the function to access and modify the global 'charges' variable.
    global charges
    
    # Create an ElectrostaticField object with the list of charges.
    # This object will handle field and potential calculations for the given charges.
    field = ElectrostaticField(charges)
    
    # Calculate the electric field components (Ex, Ey) and potential (V) over the grid.
    # The 'calculate_field_grid' method returns these values as a tuple.
    Ex, Ey, V = field.calculate_field_grid()
    
    # Create a figure for plotting
    # 'plt.figure' function: Creates a new figure window for plotting.
    # Syntax: plt.figure(figsize=(width, height))
    # - figsize: A tuple specifying the width and height of the figure in inches.
    fig = plt.figure(figsize=(10, 8))
    
    # Add a subplot (axis) to the figure
    # 'fig.add_subplot' function: Adds an axis (plot area) to the figure.
    # Syntax: fig.add_subplot(rows, cols, index)
    # - Here, '111' means 1 row, 1 column, and this is the first (and only) subplot.
    ax = fig.add_subplot(111)
    
    # Adjust the layout to make space for sliders
    # 'plt.subplots_adjust' function: Adjusts the spacing of subplots.
    # Syntax: plt.subplots_adjust(bottom=<value>)
    # - 'bottom=0.25' leaves space at the bottom for sliders.
    plt.subplots_adjust(bottom=0.25)
    
    # Plot the electric field as a vector field
    # 'ax.quiver' function: Creates a quiver plot (arrows) to represent vector fields.
    # Syntax: ax.quiver(X, Y, U, V, color=<color>, alpha=<opacity>)
    # - X, Y: Grid coordinates (field.X, field.Y).
    # - U, V: Vector components (Ex, Ey).
    # - color: Color of the arrows ('blue').
    # - alpha: Opacity of the arrows (0.6 for semi-transparent).
    Q = ax.quiver(field.X, field.Y, Ex, Ey, color='blue', alpha=0.6)
    
    # Plot equipotential lines (contour lines of constant potential)
    # 'ax.contour' function: Creates a contour plot for scalar fields (like potential).
    # Syntax: ax.contour(X, Y, Z, levels=<num>, colors=<color>, alpha=<opacity>)
    # - X, Y: Grid coordinates (field.X, field.Y).
    # - Z: Scalar field (V, the potential).
    # - levels: Number of contour levels (20).
    # - colors: Color of the contour lines ('red').
    # - alpha: Opacity of the lines (0.5 for semi-transparent).
    cont = ax.contour(field.X, field.Y, V, levels=20, colors='red', alpha=0.5)
    
    # Plot the charges as markers
    # Loop through each charge in the list of charges
    for charge in charges:
        # Determine the color based on the charge's sign
        # 'if' and 'else' keywords: Used for conditional statements.
        # Syntax: <value> if <condition> else <value>
        # - If charge.q > 0, use 'red'; otherwise, use 'blue'.
        color = 'red' if charge.q > 0 else 'blue'
        # Plot the charge as a circular marker
        # 'ax.plot' function: Plots data points or lines.
        # Syntax: ax.plot(x, y, marker=<marker>, color=<color>, markersize=<size>)
        # - x, y: Coordinates of the charge (charge.pos[0], charge.pos[1]).
        # - 'o': Circular marker.
        # - markersize: Size of the marker (10).
        ax.plot(charge.pos[0], charge.pos[1], 'o', color=color, markersize=10)
    
    # Set labels and title for the plot
    # 'ax.set_xlabel' function: Sets the label for the x-axis.
    # Syntax: ax.set_xlabel(<label>)
    ax.set_xlabel('X (m)')
    # 'ax.set_ylabel' function: Sets the label for the y-axis.
    ax.set_ylabel('Y (m)')
    # 'ax.set_title' function: Sets the title of the plot.
    ax.set_title('Electrostatic Field and Equipotential Lines')
    # 'ax.grid' function: Adds a grid to the plot for better readability.
    # Syntax: ax.grid(True)
    ax.grid(True)
    
    # Add sliders for interactive charge manipulation
    # Create axes for the sliders
    # 'plt.axes' function: Creates a new axis (area) for widgets like sliders.
    # Syntax: plt.axes([left, bottom, width, height])
    # - The values are in figure coordinates (0 to 1).
    ax_q1 = plt.axes([0.1, 0.1, 0.65, 0.03])  # Axis for charge (Q1) slider
    ax_x1 = plt.axes([0.1, 0.15, 0.65, 0.03])  # Axis for x-position (X1) slider
    
    # Create sliders for charge value and position
    # 'Slider' class: Creates an interactive slider widget.
    # Syntax: Slider(ax, label, valmin, valmax, valinit)
    # - ax: The axis where the slider is placed.
    # - label: Label for the slider.
    # - valmin, valmax: Minimum and maximum values for the slider.
    # - valinit: Initial value of the slider.
    # Create a slider for the charge value (Q1) in nanocoulombs (nC).
    q1_slider = Slider(ax_q1, 'Q1 (nC)', -5, 5, valinit=charges[0].q/1e-9)
    # Create a slider for the x-position (X1) in meters.
    x1_slider = Slider(ax_x1, 'X1 (m)', -4, 4, valinit=charges[0].pos[0])
    
    # Define an update function for the sliders
    def update(val):
        # Use the global 'charges' list to modify charge properties.
        global charges
        # Update the charge value (Q1) based on the slider value.
        # Convert from nanocoulombs (nC) to coulombs (C) by multiplying by 1e-9.
        charges[0].q = q1_slider.val * 1e-9
        # Update the x-position (X1) based on the slider value.
        charges[0].pos[0] = x1_slider.val
        # Recalculate the field and potential with the updated charge properties.
        Ex, Ey, V = field.calculate_field_grid()
        
        # Clear the current plot
        # 'ax.clear' function: Removes all elements from the axis.
        ax.clear()
        # Redraw the vector field with updated values.
        ax.quiver(field.X, field.Y, Ex, Ey, color='blue', alpha=0.6)
        # Redraw the equipotential lines with updated values.
        ax.contour(field.X, field.Y, V, levels=20, colors='red', alpha=0.5)
        
        # Redraw the charges with updated positions and colors
        for charge in charges:
            color = 'red' if charge.q > 0 else 'blue'
            ax.plot(charge.pos[0], charge.pos[1], 'o', color=color, markersize=10)
        
        # Reset labels, title, and grid
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_title('Electrostatic Field and Equipotential Lines')
        ax.grid(True)
        # Redraw the figure
        # 'fig.canvas.draw_idle' function: Updates the figure canvas.
        fig.canvas.draw_idle()
    
    # Connect the sliders to the update function
    # 'on_changed' method: Calls the specified function when the slider value changes.
    # Syntax: slider.on_changed(<function>)
    # - When the slider value changes, the 'update' function is called to redraw the plot.
    q1_slider.on_changed(update)  # Connect the charge (Q1) slider to the update function.
    x1_slider.on_changed(update)  # Connect the x-position (X1) slider to the update function.
    
    # Display the plot
    # 'plt.show' function: Displays the figure window with the plot.
    # Syntax: plt.show()
    # This opens the interactive plot window where users can adjust sliders.
    plt.show()

# Define a function for 3D visualization of the electric potential
# This function uses Plotly to create an interactive 3D surface plot of the potential.
def plot_3d_potential(charges):
    """Create 3D visualization of potential using Plotly"""
    # Create an ElectrostaticField object with the list of charges.
    # This object will handle field and potential calculations for the given charges.
    field = ElectrostaticField(charges)
    
    # Calculate the electric field components (Ex, Ey) and potential (V) over the grid.
    # The 'calculate_field_grid' method returns these values as a tuple.
    # We only need the potential (V) for the 3D plot, so we ignore Ex and Ey using '_'.
    _, _, V = field.calculate_field_grid()
    
    # Create a 3D surface plot using Plotly
    # 'go.Figure' class: Creates a new Plotly figure for interactive visualizations.
    # Syntax: go.Figure(data=[<traces>])
    # - 'data' is a list of traces (like surfaces, scatter plots, etc.) to display.
    fig = go.Figure(data=[
        # Add a surface plot for the electric potential
        # 'go.Surface' class: Creates a 3D surface plot.
        # Syntax: go.Surface(x=<X>, y=<Y>, z=<Z>, colorscale=<colorscale>, showscale=<bool>)
        # - x, y: Grid coordinates (field.X, field.Y).
        # - z: Scalar field (V, the potential).
        # - colorscale: Color scheme for the surface ('Viridis' is a common colormap).
        # - showscale: Whether to show the color scale (True).
        go.Surface(
            x=field.X,  # X-coordinates of the grid
            y=field.Y,  # Y-coordinates of the grid
            z=V,        # Z-values (potential) for the surface
            colorscale='Viridis',  # Color scheme for the surface
            showscale=True         # Show the color scale on the side
        )
    ])
    
    # Add markers for the charges on the 3D plot
    # Loop through each charge in the list of charges
    for charge in charges:
        # Add a scatter plot for the charge marker
        # 'go.Scatter3d' class: Creates a 3D scatter plot for points.
        # Syntax: go.Scatter3d(x=<X>, y=<Y>, z=<Z>, mode=<mode>, marker=<dict>)
        # - x, y, z: Coordinates of the point (charge position and potential).
        # - mode: Type of plot ('markers' for points).
        # - marker: Dictionary specifying marker properties (size, color).
        fig.add_trace(go.Scatter3d(
            x=[charge.pos[0]],  # X-coordinate of the charge
            y=[charge.pos[1]],  # Y-coordinate of the charge
            # Calculate the potential at the charge's position for the Z-coordinate
            z=[field.calculate_potential(charge.pos)],
            mode='markers',  # Display as markers (points)
            marker=dict(     # Marker properties
                size=10,     # Size of the marker
                # Color based on charge sign: red for positive, blue for negative
                color='red' if charge.q > 0 else 'blue'
            )
        ))
    
    # Update the layout of the 3D plot
    # 'fig.update_layout' function: Updates the layout of the Plotly figure.
    # Syntax: fig.update_layout(<layout_settings>)
    fig.update_layout(
        title='Electric Potential Distribution',  # Set the title of the plot
        scene=dict(  # Define the 3D scene properties
            xaxis_title='X (m)',  # Label for the x-axis
            yaxis_title='Y (m)',  # Label for the y-axis
            zaxis_title='Potential (V)'  # Label for the z-axis (potential)
        )
    )
    
    # Display the 3D plot
    # 'fig.show' function: Displays the Plotly figure in the default viewer (usually a web browser).
    # Syntax: fig.show()
    # This opens an interactive 3D plot where users can rotate and zoom.
    fig.show()

# Run the simulations
# 'if' keyword: Used for conditional statements.
# Syntax: if <condition>:
# '__name__' is a special variable in Python:
# - If the script is run directly, '__name__' is set to '__main__'.
# - If the script is imported as a module, '__name__' is set to the module name.
# This block ensures the visualizations run only when the script is executed directly.
if __name__ == "__main__":
    # Run the interactive 2D visualization
    # This displays the 2D plot with sliders for charge manipulation.
    plot_interactive_field()
    
    # Run the 3D potential visualization using the modified charges
    # This displays the 3D surface plot of the electric potential.
    # Note: The charges may have been modified by the interactive 2D plot.
    plot_3d_potential(charges)
