from imagescraper import *


#########################
# Paramaters to change
#########################
output_path = "data/cat-images/"

number_of_images = 10

search_terms = [
    "image of a cat",
    "cat",
    "cat image",
    "photo of a cat",
    "cat photo",
    "kitten image",
    "kitten",
    "kitten photo"
]

title_term = "cat_img"

#### End of parameters to change ####





dirs = glob(output_path + "*")
dirs = [dir.split("/")[-1].replace("_", " ") for dir in dirs]

# Exclude terms already stored.
search_terms = [term for term in search_terms if term not in dirs]

for i, term in enumerate(search_terms):
    search_and_download(term, output_path, number_of_images, title_term, i)