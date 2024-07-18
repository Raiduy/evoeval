
from typing import List, Optional, Tuple

def longest_planet_chain(planet1: str, planet2: str, chains: List[Tuple[str, ...]]) -> Optional[Tuple[str, ...]]:
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return None
    longest_chain = None
    max_length = 0
    for chain in chains:
        if chain[0] == planet1 and chain[-1] == planet2:
            if len(chain) > max_length:
                longest_chain = chain
                max_length = len(chain)
    return longest_chain