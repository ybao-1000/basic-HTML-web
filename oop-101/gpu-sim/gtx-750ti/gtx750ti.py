from gpu import GPU
import random

class GTX750Ti(GPU):
    def __init__(self):
        super().__init__(
            name="GTX 750 Ti",
            cuda_cores=640,
            base_clock=1020,
            boost_clock=1085
        )
        self.vram_mb = 2048
        self.vram_used = 0
        self.temperature = 35.0
        self.fps = 0
        self.current_game = None

    def load_game(self, game):
        self.current_game = game
        self.vram_used = game.vram_usage_mb

    def render_frame(self):
        if not self.current_game:
            return

        clock = random.uniform(self.base_clock, self.boost_clock)
        load = self.current_game.load

        self.fps = clock * 0.12 * load
        self.temperature += load * random.uniform(0.3, 0.7)

        if self.vram_used > self.vram_mb:
            self.fps *= 0.5  # VRAM overflow

        if self.temperature > 80:
            self.fps *= 0.7  # thermal throttle

    def show_info(self):
        print(f"GPU: {self.name}")
        print(f"Game: {self.current_game.name}")
        print(f"FPS: {self.fps:.1f}")
        print(f"Temp: {self.temperature:.1f}°C")
        print(f"VRAM: {self.vram_used}/{self.vram_mb} MB")
        print("-" * 35)