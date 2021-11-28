class SceneManager:

    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def get_scene(self, scene_id: int):
        return self.scenes.get(scene_id)

    def set_scene(self, scene, sc_id: int):
        self.scenes[sc_id] = scene

    def go_to(self, scene_id: int):
        last_scene = self.current_scene
        if last_scene:
            last_scene.on_scene_quit()

        self.current_scene = self.get_scene(scene_id)
        self.current_scene.on_scene_enter()

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def render(self):
        if self.current_scene:
            self.current_scene.render()
