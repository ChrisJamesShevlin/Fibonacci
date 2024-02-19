import mysql.connector
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

mydb = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Uia86w!md',
    'database': 'fibonacci',
}

# Establish a connection to the MySQL database
connection = mysql.connector.connect(**mydb)

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    cursor = connection.cursor()

    # Execute a simple SELECT query to retrieve all data from the fibonacci_table
    query = "SELECT * FROM fibonacci_numbers"
    cursor.execute(query)

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Extract ID and Value columns
    ids = [row[0] for row in rows]
    values = [row[1] for row in rows]

    # Calculate polar coordinates with increased spacing
    theta = np.linspace(0, 4 * np.pi, len(values)) * 2  # Increase the scaling factor for more spacing
    radius = values

    # Convert polar coordinates to Cartesian coordinates
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = ids

    # Clear previous plot
    ax.cla()

    # Plot the data in 3D
    ax.scatter(x, y, z, marker='o')

    # Set labels
    ax.set_title('Fibonacci Spiral - Value Column (3D)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Print the header
    print("ID\tValue")

    # Print each row
    for row in rows:
        print(f"{row[0]}\t{row[1]}")

# Create an animation
animation = FuncAnimation(fig, update, frames=None, repeat=False, interval=1000)  # Adjust interval as needed

# Show the animated plot
plt.show()

# Close the connection after the animation is finished
connection.close()
