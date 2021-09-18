
import random
from typing import Iterator


class BirdFaker:
    def __init__(self) -> None:
        self._descriptors = []
        self._varieties = []

    def train(self, filename) -> None:
        all_descriptors = set()
        all_varieties = set()

        with open(filename) as f:
            for bird in f:
                *descriptors, variety = bird.strip().split(" ")
                all_descriptors.update(descriptors)
                all_varieties.add(variety)

        self._descriptors = list(set(self._descriptors) | all_descriptors)
        self._varieties = list(set(self._varieties) | all_varieties)

    def fake_bird(self) -> str:
        num_descriptors = random.randrange(1, 4)
        descriptors = random.choices(self._descriptors, k=num_descriptors)
        variety = random.choice(self._varieties)

        return " ".join([*descriptors, variety])

    def fake_birds(self) -> Iterator[str]:
        yield self.fake_bird()
