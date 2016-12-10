def update_image_rect(image, rect):
    image_rect = image.get_rect()
    image_rect.x = rect.x
    image_rect.y = rect.y
