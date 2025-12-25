from gtx750ti import GTX750Ti
from game import Game
import time

gpu = GTX750Ti()

csgo = Game("CS:GO", vram_usage_mb=800, load=0.4)
gta5 = Game("GTA V", vram_usage_mb=2600, load=0.9)

gpu.load_game(gta5)

while True:
    gpu.render_frame()
    gpu.show_info()
    time.sleep(1)