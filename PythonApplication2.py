import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import plotly.graph_objects as go

# Constants
k = 8.9875517923e9  # Coulomb's constant (N⋅m²/C²)
epsilon_0 = 8.854187817e-12  # Permittivity of free space (F/m)

class Charge:
    def __init__(self, q, x, y):
        self.q = q  # Charge value in Coulombs
        self.pos = np.array([x, y])  # Position in meters

class ElectrostaticField:
    def __init__(self, charges, grid_size=10, grid_points=30):
        self.charges = charges
        self.grid_size = grid_size
        self.grid_points = grid_points
        
        # Create grid for field calculations
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
            if r_magnitude < 0.1:  # Avoid division by zero
                continue
            E = k * charge.q * r / (r_magnitude**3)
            E_total += E
        return E_total

    def calculate_potential(self, point):
        """Calculate electric potential at a point 302"""
        V_total = 0
        point = np.array(point)
        
        for charge in self.charges:
            r = np.linalg.norm(point - charge.pos)
            if r < 0.1:  # Avoid division by zero
                continue
            V = k * charge.q / r
            V_total += V
        return V_total

    def calculate_field_grid(self):
        """Calculate field components over the entire grid"""
        Ex = np.zeros_like(self.X)
        Ey = np.zeros_like(self.Y)
        V = np.zeros_like(self.X)

        for i in range(self.grid_points):
            for j in range(self.grid_points):
                point = [self.X[i,j], self.Y[i,j]]
                E = self.calculate_field(point)
                Ex[i,j] = E[0]
                Ey[i,j] = E[1]
                V[i,j] = self.calculate_potential(point)
        
        return Ex, Ey, V

# Global charges list
charges = [
    Charge(1e-9, -2, 0),  # Positive charge
    Charge(-1e-9, 2, 0)   # Negative charge
]

def plot_interactive_field():
    global charges  # Use the global charges list
    
    field = ElectrostaticField(charges)
    Ex, Ey, V = field.calculate_field_grid()
    
    # Create the figure and axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(bottom=0.25)
    
    # Plot vector field
    Q = ax.quiver(field.X, field.Y, Ex, Ey, color='blue', alpha=0.6)
    
    # Plot equipotential lines
    cont = ax.contour(field.X, field.Y, V, levels=20, colors='red', alpha=0.5)
    
    # Plot charges
    for charge in charges:
        color = 'red' if charge.q > 0 else 'blue'
        ax.plot(charge.pos[0], charge.pos[1], 'o', color=color, markersize=10)
    
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_title('Electrostatic Field and Equipotential Lines')
    ax.grid(True)
    
    # Add sliders for charge manipulation
    ax_q1 = plt.axes([0.1, 0.1, 0.65, 0.03])
    ax_x1 = plt.axes([0.1, 0.15, 0.65, 0.03])
    q1_slider = Slider(ax_q1, 'Q1 (nC)', -5, 5, valinit=charges[0].q/1e-9)
    x1_slider = Slider(ax_x1, 'X1 (m)', -4, 4, valinit=charges[0].pos[0])
    
    def update(val):
        global charges
        charges[0].q = q1_slider.val * 1e-9
        charges[0].pos[0] = x1_slider.val
        Ex, Ey, V = field.calculate_field_grid()
        
        ax.clear()
        ax.quiver(field.X, field.Y, Ex, Ey, color='blue', alpha=0.6)
        ax.contour(field.X, field.Y, V, levels=20, colors='red', alpha=0.5)
        
        for charge in charges:
            color = 'red' if charge.q > 0 else 'blue'
            ax.plot(charge.pos[0], charge.pos[1], 'o', color=color, markersize=10)
        
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_title('Electrostatic Field and Equipotential Lines')
        ax.grid(True)
        fig.canvas.draw_idle()
    
    q1_slider.on_changed(update)
    x1_slider.on_changed(update)
    
    plt.show()

def plot_3d_potential(charges):
    """Create 3D visualization of potential using Plotly"""
    field = ElectrostaticField(charges)
    _, _, V = field.calculate_field_grid()
    
    fig = go.Figure(data=[
        go.Surface(
            x=field.X,
            y=field.Y,
            z=V,
            colorscale='Viridis',
            showscale=True
        )
    ])
    
    # Add charge markers
    for charge in charges:
        fig.add_trace(go.Scatter3d(
            x=[charge.pos[0]],
            y=[charge.pos[1]],
            z=[field.calculate_potential(charge.pos)],
            mode='markers',
            marker=dict(
                size=10,
                color='red' if charge.q > 0 else 'blue'
            )
        ))
    
    fig.update_layout(
        title='Electric Potential Distribution',
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Potential (V)'
        )
    )
    
    fig.show()

# Run the simulations
if __name__ == "__main__":
    # Interactive 2D visualization
    plot_interactive_field()
    
    # 3D potential visualization using the modified charges
    plot_3d_potential(charges)