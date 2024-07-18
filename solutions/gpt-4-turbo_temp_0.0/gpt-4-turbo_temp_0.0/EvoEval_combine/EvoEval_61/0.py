
from typing import List, Optional, Tuple

def longest_planet_chain(planet1: str, planet2: str, chains: List[Tuple[str, ...]]) -> Optional[Tuple[str, ...]]:
    valid_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in valid_planets or planet2 not in valid_planets:
        return None
    longest_chain = None
    for chain in chains:
        if chain[0] == planet1 and chain[-1] == planet2:
            if longest_chain is None or len(chain) > len(longest_chain):
                longest_chain = chain
    return longest_chain