from abc import ABC, abstractmethod

class GPU(ABC):
    def __init__(self, name, cuda_cores, base_clock, boost_clock):
        self.name = name
        self.cuda_cores = cuda_cores
        self.base_clock = base_clock
        self.boost_clock = boost_clock

    @abstractmethod
    def render_frame(self):
        pass

    @abstractmethod
    def show_info(self):
        pass