from imagescraper import *
from get_terms import *
from combine_images import *


# Get the search terms, title term, output path, and number of images from the user
search_terms, title_term, output_path, number_of_images, combine_images = get_terms()

dirs = glob(output_path + "*")
dirs = [dir.split("/")[-1].replace("_", " ") for dir in dirs]

# Exclude terms already stored.
search_terms = [term for term in search_terms if term not in dirs]

for i, term in enumerate(search_terms):
    search_and_download(term, output_path, number_of_images, title_term, i)

if combine_images:
    photo_quilt(output_path, 1000, 1000)
    # Open the quilt
    quilt = Image.open('my_quilt.png')
    quilt.show()
