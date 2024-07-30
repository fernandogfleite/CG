from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from algorithms import bresenham_algorithm


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black and opaque
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer (background)
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)  # Set the orthographic projection


def draw_points(points):
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    glColor3f(1.0, 1.0, 1.0)  # Set pixel color to white
    glBegin(GL_POINTS)  # Start drawing points
    for x, y in points:
        glVertex2i(x, y)  # Specify the pixel coordinates
    glEnd()  # End drawing points
    glFlush()  # Render now


def multiply_vector(vector, scalar):
    return [scalar * element for element in vector]


def display():
    # Use the Bresenham algorithm to get the points for a line
    initial_point = (1, 1)
    final_point = (8, 5)

    final_point = multiply_vector(final_point, 20)

    x_inicial, y_inicial = initial_point
    x_final, y_final = final_point

    points = bresenham_algorithm(x_inicial, y_inicial, x_final, y_final)
    draw_points(points)


def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set the display mode
    glutInitWindowSize(640, 480)  # Set the window size
    glutInitWindowPosition(100, 100)  # Set the window position
    glutCreateWindow(b"OpenGL Pixel Drawing")  # Create the window with a title
    init()  # Call the initialization function
    glutDisplayFunc(display)  # Register the display callback function
    glutMainLoop()  # Enter the GLUT event processing loop


if __name__ == "__main__":
    main()
