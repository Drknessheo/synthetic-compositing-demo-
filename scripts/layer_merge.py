# layer_merge.py

""" 
This script demonstrates a layer merging and compositing workflow. 
"""

import numpy as np
import cv2

# Function to merge two images using alpha blending

def merge_layers(background, overlay, alpha=0.5):
    """Merge two images with a given alpha value."""
    return cv2.addWeighted(background, 1 - alpha, overlay, alpha, 0)

# Example usage
if __name__ == '__main__':
    # Load background and overlay images
    background = cv2.imread('background.jpg')
    overlay = cv2.imread('overlay.png')

    # Check if images are loaded
    if background is None or overlay is None:
        print("Error loading images. Please check the file paths.")
    else:
        # Merge the images
        merged_image = merge_layers(background, overlay)
        
        # Save the result
        cv2.imwrite('merged_image.jpg', merged_image)
        print('Merged image saved as merged_image.jpg')
