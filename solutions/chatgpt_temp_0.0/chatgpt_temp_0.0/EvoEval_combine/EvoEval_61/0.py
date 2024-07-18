
from typing import List, Optional, Tuple

def longest_planet_chain(planet1: str, planet2: str, chains: List[Tuple[str, ...]]) -> Optional[Tuple[str, ...]]:
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return None
    for chain in chains:
        if chain[0] == planet1 and chain[-1] == planet2:
            if not hasattr(longest_planet_chain, 'longest_chain') or len(chain) > len(longest_planet_chain.longest_chain):
                longest_planet_chain.longest_chain = chain
    return longest_planet_chain.longest_chain if hasattr(longest_planet_chain, 'longest_chain') else None