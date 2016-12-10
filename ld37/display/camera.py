from pygame.rect import Rect

class Camera(object):
    def __init__(self, screen_width, screen_height, width, height):
        self.camera_man = CameraMan(screen_width, screen_height)
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.cameraMan.update_camera_view(self.state, target.rect)

class CameraMan():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.half_width = int(screen_width / 2)
        self.half_height = int(screen_height / 2)

    def update_camera_view(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l + self.half_width, -t + self.half_height, w, h

        l = min(0, l)                                       # stop scrolling at the left edge
        l = max(-(camera.width - self.screen_width), l)     # stop scrolling at the right edge
        t = max(-(camera.height - self.screen_height), t)   # stop scrolling at the bottom
        t = min(0, t)                                       # stop scrolling at the top
        return Rect(l, t, w, h)
