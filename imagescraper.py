import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil #pip install shutil
from glob import glob

##############
# Parameters
##############

# number_of_images = 4
GET_IMAGE_TIMEOUT = 2
SLEEP_BETWEEN_INTERACTIONS = 0.1
SLEEP_BEFORE_MORE = 5
IMAGE_QUALITY = 85

#output_path = "cats-crimes/cat_images/"

# # Get terms already recorded.
# dirs = glob(output_path + "*")
# dirs = [dir.split("/")[-1].replace("_", " ") for dir in dirs]


# search_terms = [
#     "image of a cat",
#     "cat",
#     "cat image",
#     "photo of a cat",
#     "cat photo",
#     "kitten image",
#     "kitten",
#     "kitten photo"
# ]

# title_term = "cat_img"
# # Exclude terms already stored.
# search_terms = [term for term in search_terms if term not in dirs]

##########
# Web Scraping
##########

image_urls = []



wd = webdriver.Chrome()


def fetch_image_urls(
    query: str,
    max_links_to_fetch: int,
    wd: webdriver,
    sleep_between_interactions: int = 1,
):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    # Build the Google Query.
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    # Declared as a set, to prevent duplicates.
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # Get all image thumbnail results
        thumbnail_results = wd.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(
            f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}"
        )

        # Loop through image thumbnail identified
        for img in thumbnail_results[results_start:number_results]:
            # Try to click every thumbnail such that we can get the real image behind it.
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # Extract image urls
            actual_images = wd.find_elements(By.CSS_SELECTOR, "img.n3VNCb")
            for actual_image in actual_images:
                if actual_image.get_attribute(
                    "src"
                ) and "http" in actual_image.get_attribute("src"):
                    image_urls.add(actual_image.get_attribute("src"))

            image_count = len(image_urls)

            # If the number images found exceeds our `num_of_images`, end the seaerch.
            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            # If we haven't found all the images we want, let's look for more.
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(SLEEP_BEFORE_MORE)

            # Check for button signifying no more images.
            not_what_you_want_button = ""
            try:
                not_what_you_want_button =  wd.find_elements(By.CSS_SELECTOR, ".r0zKGf")
            except:
                pass

            # If there are no more images return.
            if not_what_you_want_button:
                print("No more images available.")
                return image_urls

            # If there is a "Load More" button, click it.
            load_more_button =  wd.find_elements(By.CSS_SELECTOR, ".mye4qd")
            if load_more_button and not not_what_you_want_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # Move the result startpoint further down.
        results_start = len(thumbnail_results)

    return image_urls


def download_image(folder_path: str, url: str, i: int, index: int, quantity: int = 5):
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            image_number = i + quantity * index
            with open(folder_path + str(image_number) + '.jpg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print("SUCCESS- Got image" + str(image_number) + " - saved to " + folder_path + str(image_number) + '.jpg')
        else:
            print("ERROR - Could not download {url} - {r.status_code}")


    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")


def search_and_download(search_term: str, target_path="./images", number_images=5, title_term="cat_img", index = 0):
    # Create a folder name.
    target_folder = os.path.join(target_path, "_".join(title_term.lower().split(" ")))

    # Open Chrome
    with webdriver.Chrome() as wd:
        # Search for images URLs.
        res = fetch_image_urls(
            search_term,
            number_images,
            wd=wd,
            sleep_between_interactions=SLEEP_BETWEEN_INTERACTIONS,
        )

        # Download the images.
        if res is not None:
            for i, elem in enumerate(res):
                download_image(target_folder, elem, i, number_images, index)
        else:
            print(f"Failed to return links for term: {search_term}")


# for i, term in enumerate(search_terms):
#     search_and_download(term, output_path, number_of_images, title_term, i)