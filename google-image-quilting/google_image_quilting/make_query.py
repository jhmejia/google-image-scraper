def make_img_query():

    from google_image_quilting.imagescraper import fetch_image_urls, download_image, search_and_download
    from google_image_quilting.get_terms import get_terms
    from google_image_quilting.combine_images import photo_quilt, get_smallest_image_size

    
    # Get the search terms, title term, output path, and number of images from the user
    search_terms, title_term, output_path, number_of_images, combine_images = get_terms()

    print("Got search terms: ", search_terms)
    print("Got title term: ", title_term)
    print("Got output path: ", output_path)
    print("Got number of images: ", number_of_images)
    print("Got combine images: ", combine_images)

    dirs = glob(output_path + "*")
    dirs = [dir.split("/")[-1].replace("_", " ") for dir in dirs]

    # Exclude terms already stored.
    search_terms = [term for term in search_terms if term not in dirs]

    for i, term in enumerate(search_terms):
        search_and_download(term, output_path, number_of_images, title_term, i)

    if combine_images:
        # Combine the images into a quilt
        print("Combining images into a quilt...")
        photo_quilt(output_path, 1000, 1000)
        # Open the quilt
        quilt = Image.open('my_quilt.png')
        quilt.show()


if __name__ == "__main__":
    make_query()