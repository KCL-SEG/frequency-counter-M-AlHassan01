"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    """returns a dictionary containing the frequency in which an item in an input list appears"""
    frequencies = {}
    for item in items:
        # Checks if an item exists in the dictionary
        if frequencies.__contains__(str(item)):
            frequencies[str(item)] += 1
        else:
            frequencies[str(item)] = 1
    return frequencies
