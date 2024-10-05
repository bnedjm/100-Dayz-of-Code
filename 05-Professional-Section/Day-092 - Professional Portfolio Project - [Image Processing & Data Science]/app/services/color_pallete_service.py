import numpy as np
from sklearn.cluster import KMeans
import webcolors

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_top_colors(image, num_colors=10):
    if image.mode != 'RGB':
        image = image.convert('RGB')
        
    # Resize the image to reduce computation
    image = image.resize((100, 100))
    
    # Convert the image into an array of RGB values
    image_array = np.array(image)
    
    # Reshape the image to be a list of pixels
    pixels = image_array.reshape((-1, 3))

    # Use KMeans clustering to find `num_colors` clusters (colors)
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Get the cluster centers (most dominant colors)
    colors = kmeans.cluster_centers_

    # Convert colors from float to integer
    colors = colors.round(0).astype(int)

    # Convert RGB to hex format and find the closest color name
    hex_colors = []
    for color in colors:
        hex_code = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        name = closest_color(color)
        hex_colors.append({
            'name': name,
            'hex': hex_code
        })
    
    return hex_colors
