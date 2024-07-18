
def bf(planet1, planet2):
    # Define the order of the planets in the solar system
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    # Check if both planet1 and planet2 are in the list of planets
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indexes of planet1 and planet2
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Ensure index1 is less than index2 for correct slicing
    if index1 > index2:
        index1, index2 = index2, index1
    
    # Return the planets between planet1 and planet2, exclusive
    return planets[index1 + 1:index2]
