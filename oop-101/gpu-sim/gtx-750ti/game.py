class Game:
    def __init__(self, name, vram_usage_mb, load):
        self.name = name
        self.vram_usage_mb = vram_usage_mb
        self.load = load  # 0.0 → 1.0