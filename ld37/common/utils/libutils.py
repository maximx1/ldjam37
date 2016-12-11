import math

def update_image_rect(image, rect):
    image_rect = image.get_rect()
    image_rect.x = rect.x
    image_rect.y = rect.y

def distance_between_rects(rect1, rect2):
    (r1_center_x, r1_center_y) = rect1.center
    (r2_center_x, r2_center_y) = rect2.center
    x_squared = (r2_center_x - r1_center_x)**2
    y_squared = (r2_center_y - r1_center_y)**2
    return math.sqrt(x_squared + y_squared)
