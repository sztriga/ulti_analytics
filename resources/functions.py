import os

from .card import Card
from typing import Iterable
from math import comb
from IPython.display import display, HTML


def display_cards(cards: Iterable[Card]) -> None:
    # Loop through the cards and display the images
    image_folder = "resources/card_graphics"  # Make sure this folder exists

    # Start HTML for displaying images
    html_content = '<div style="display: flex; flex-direction: row; flex-wrap: nowrap;">'

    for card in cards:
        # Create the filename based on the card's color and value
        image_filename = f"card_piece_{str(card)}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        
         # Display the image if it exists
        if os.path.isfile(image_path):
            html_content += f'<img src="{image_path}" style="width: 100px; margin: 5px;">'
        else:
            html_content += f'<div style="width: 100px; margin: 5px;">Image not found for card: {image_path}</div>'
        
    # Close the HTML div
    html_content += "</div>"

    # Display the images in one row
    display(HTML(html_content))


def probability_color_distribution(n: int, m: int, total_no_cards: int = 20) -> float:
    """
    Calculate the probability of distributing n target cards 
    such that m are in one hand and n - m are in the other.
    
    Parameters:
        n (int): Total number of target cards.
        m (int): Number of target cards in one hand.
        total_no_cards (int): Total number of cards (default 20).
        
    Returns:
        float: Probability of the distribution.
    """
    
    if m < 0 or m > n:
        return 0  # Probability is 0 if m is out of bounds
    
    if n > total_no_cards:
        return 0  # Probability is 0 if there are more red cards than total cards
    
    # Calculate the number of ways to choose m target cards for hand 1
    ways_hand1 = comb(n, m)
    
    # Calculate the number of ways to choose (10 - m) cards from (20 - n)
    ways_hand2 = comb(total_no_cards - n, 10 - m)

    # Calculate the total ways to choose 10 cards from 20
    total_ways = comb(total_no_cards, 10)

    # Calculate the probability
    probability = (ways_hand1 * ways_hand2) / total_ways
    
    # Distribution is symmetrical, multiply probability by 2 if cards are not evenly distributed
    if n != 2 * m:
        probability *= 2

    return probability