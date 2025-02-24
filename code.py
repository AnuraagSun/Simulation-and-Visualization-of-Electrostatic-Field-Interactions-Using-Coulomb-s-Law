

import numpy as np  # 'np' is a common alias for numpy, making it easier to type.
import matplotlib.pyplot as plt  # 'plt' is a common alias for matplotlib.pyplot.
from matplotlib.widgets import Slider, Button  # Import specific classes (Slider, Button) from matplotlib.widgets.
import plotly.graph_objects as go  # 'go' is a common alias for plotly.graph_objects.

k = 8.9875517923e9  # Coulomb's constant (N⋅m²/C²)

epsilon_0 = 8.854187817e-12  # Permittivity of free space (F/m)


class Charge:
    def __init__(self, q, x, y):
        self.q = q  # Charge value in Coulombs
        self.pos = np.array([x, y])  # Position in meters

# Define a class to represent the electrostatic field
# This class handles calculations and visualizations for the electric field and potential.
class ElectrostaticField:
    def __init__(self, charges, grid_size=10, grid_points=30):
        # Assign the list of charges to 'self.charges'.
        self.charges = charges
        # Assign the grid size to 'self.grid_size'.
        self.grid_size = grid_size
        # Assign the number of grid points to 'self.grid_points'.
        self.grid_points = grid_points
        x = np.linspace(-grid_size/2, grid_size/2, grid_points)
        y = np.linspace(-grid_size/2, grid_size/2, grid_points)
        self.X, self.Y = np.meshgrid(x, y)
    def calculate_field(self, point):
        """Calculate electric field at a point due to all charges"""
        E_total = np.zeros(2)
        point = np.array(point)
        for charge in self.charges:
            r = point - charge.pos
            r_magnitude = np.linalg.norm(r)
            if r_magnitude < 0.1:
                continue
            E = k * charge.q * r / (r_magnitude**3)
            E_total += E
        return E_total

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
                
        return Ex, Ey, V

charges = [
    # Create a positive charge with q = 1e-9 C (1 nanocoulomb) at position (-2, 0).
    Charge(1e-9, -2, 0),  # Positive charge
    # Create a negative charge with q = -1e-9 C (-1 nanocoulomb) at position (2, 0).
    Charge(-1e-9, 2, 0)   # Negative charge
]

def plot_interactive_field():
    global charges
    field = ElectrostaticField(charges)
    Ex, Ey, V = field.calculate_field_grid()
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(bottom=0.25)
    Q = ax.quiver(field.X, field.Y, Ex, Ey, color='blue', alpha=0.6)
    cont = ax.contour(field.X, field.Y, V, levels=20, colors='red', alpha=0.5)
    for charge in charges:
        color = 'red' if charge.q > 0 else 'blue'
        ax.plot(charge.pos[0], charge.pos[1], 'o', color=color, markersize=10)
    ax.set_xlabel('X (m)')
    # 'ax.set_ylabel' function: Sets the label for the y-axis.
    ax.set_ylabel('Y (m)')
    # 'ax.set_title' function: Sets the title of the plot.
    ax.set_title('Electrostatic Field and Equipotential Lines')
    # 'ax.grid' function: Adds a grid to the plot for better readability.
    # Syntax: ax.grid(True)
    ax.grid(True)
    
    ax_q1 = plt.axes([0.1, 0.1, 0.65, 0.03])  # Axis for charge (Q1) slider
    ax_x1 = plt.axes([0.1, 0.15, 0.65, 0.03])  # Axis for x-position (X1) slider
    
   
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
    
  
    q1_slider.on_changed(update)  # Connect the charge (Q1) slider to the update function.
    x1_slider.on_changed(update)  # Connect the x-position (X1) slider to the update function.
    
 
    plt.show()


def plot_3d_potential(charges):
    """Create 3D visualization of potential using Plotly"""

    field = ElectrostaticField(charges)
     _, _, V = field.calculate_field_grid()
    fig = go.Figure(data=[
        go.Surface(
            x=field.X,  # X-coordinates of the grid
            y=field.Y,  # Y-coordinates of the grid
            z=V,        # Z-values (potential) for the surface
            colorscale='Viridis',  # Color scheme for the surface
            showscale=True         # Show the color scale on the side
        )
    ])
    

    for charge in charges:
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
    
    fig.update_layout(
        title='Electric Potential Distribution',  # Set the title of the plot
        scene=dict(  # Define the 3D scene properties
            xaxis_title='X (m)',  # Label for the x-axis
            yaxis_title='Y (m)',  # Label for the y-axis
            zaxis_title='Potential (V)'  # Label for the z-axis (potential)
        )
    )
    fig.show()

if __name__ == "__main__":
    plot_interactive_field()
    plot_3d_potential(charges)
