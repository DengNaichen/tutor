# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    # Parameters for the simple harmonic oscillator
    m = 1.0      # mass
    k = 1.0      # spring constant
    omega = np.sqrt(k / m) # angular frequency
    A = 1.0      # amplitude
    phi = 0.0    # phase lag

    # Time array for the analytical solution
    t = np.linspace(0, 10 * np.pi, 500)

    # Equations of motion
    x = A * np.cos(omega * t + phi)
    v = -A * omega * np.sin(omega * t + phi)

    # Set up the figure and gridspec
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(2, 2)
    
    # 1. Position and Velocity vs Time Plot
    ax_time = fig.add_subplot(gs[:, 0])
    ax_time.plot(t, x, label='Position (x)', color='dodgerblue')
    ax_time.plot(t, v, label='Velocity (v)', color='darkorange', linestyle='--')
    ax_time.set_title('Position & Velocity vs. Time')
    ax_time.set_xlabel('Time (t)')
    ax_time.set_ylabel('Amplitude')
    ax_time.axhline(0, color='black', linewidth=0.5)
    ax_time.legend(loc='upper right')
    ax_time.grid(True, linestyle=':', alpha=0.7)

    # 2. Phase Space Plot (Velocity vs Position)
    ax_phase = fig.add_subplot(gs[0, 1])
    ax_phase.plot(x, v, color='crimson')
    ax_phase.set_title('Phase Space Trajectory')
    ax_phase.set_xlabel('Position (x)')
    ax_phase.set_ylabel('Velocity (v)')
    ax_phase.axhline(0, color='black', linewidth=0.5)
    ax_phase.axvline(0, color='black', linewidth=0.5)
    ax_phase.grid(True, linestyle=':', alpha=0.7)
    ax_phase.set_aspect('equal', adjustable='box')

    # 3. Animation View (Mass on a spring)
    ax_anim = fig.add_subplot(gs[1, 1])
    ax_anim.set_xlim(-1.5, 1.5)
    ax_anim.set_ylim(-0.5, 0.5)
    ax_anim.set_title('Animation View')
    ax_anim.set_xlabel('Position (x)')
    ax_anim.set_yticks([]) # Hide y-axis
    ax_anim.axhline(0, color='black', linewidth=0.5)
    ax_anim.grid(True, linestyle=':', alpha=0.7)

    # Elements for animation
    line, = ax_time.plot([], [], 'ro')
    mass, = ax_anim.plot([], [], 'o', markersize=20, color='dodgerblue')
    spring, = ax_anim.plot([], [], '-', color='gray', linewidth=2)
    
    def init():
        line.set_data([], [])
        mass.set_data([], [])
        spring.set_data([], [])
        return line, mass, spring

    def animate(i):
        # Update the time series tracer
        line.set_data([t[i]], [x[i]])
        
        # Update the 1D mass
        mass_x = x[i]
        mass.set_data([mass_x], [0])
        
        # Update the spring (a simple line from equilibrium -1.5 to the mass)
        spring_x = np.linspace(-1.5, mass_x, 20)
        # Create a zig-zag pattern for the spring
        spring_y = np.zeros_like(spring_x)
        spring_y[1:-1] = 0.1 * np.sin(np.pi * np.arange(1, 19)) * ((-1)**np.arange(1, 19))
        spring.set_data(spring_x, spring_y)
        
        return line, mass, spring

    # Create the animation
    ani = animation.FuncAnimation(
        fig, animate, init_func=init, 
        frames=len(t), interval=20, blit=True
    )

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
