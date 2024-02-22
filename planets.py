import turtle
import math

# Function to draw a planet
def draw_planet(color, radius):
    planet = turtle.Turtle()
    planet.speed(0)
    planet.shape("circle")
    planet.color(color)
    planet.penup()
    planet.goto(radius, 0)
    planet.pendown()
    return planet

# Function to update planet's position
def update_position(planet, angle, radius):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    planet.goto(x, y)

# Main function to simulate orbiting planets
def simulate_orbit():
    screen = turtle.Screen()
    screen.bgcolor("black")

    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(2)  # Sun's radius

    planets = [
        ("gray", 50, 360/88),   # Mercury
        ("orange", 80, 360/225), # Venus
        ("blue", 110, 360/365),  # Earth
        ("red", 150, 360/687),   # Mars
        ("cyan", 220, 360/4332), # Jupiter
        ("magenta", 280, 360/10759), # Saturn
        ("orange", 330, 360/30687), # Uranus
        ("blue", 380, 360/60190),   # Neptune
        ("red", 430, 360/90553)    # Pluto
    ]

    for planet_color, planet_radius, orbit_speed in planets:
        planet = draw_planet(planet_color, planet_radius)
        for _ in range(10):
            for angle in range(0, 360, orbit_speed):
                update_position(planet, angle, planet_radius)
    
    screen.mainloop()

# Run simulation
simulate_orbit()
