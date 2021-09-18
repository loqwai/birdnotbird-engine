
import random
from typing import Iterator


class BirdFaker:
    def __init__(self) -> None:
        self._descriptors = []
        self._varieties = []
        self._birds = set()

    def train(self, filename) -> None:
        with open(filename) as f:
            self._birds.update([bird.strip() for bird in f])

        all_descriptors = set()
        all_varieties = set()

        for bird in self._birds:
            *descriptors, variety = bird.strip().split(" ")

            all_descriptors.update(descriptors)
            all_varieties.add(variety)

        self._descriptors = list(set(self._descriptors) | all_descriptors)
        self._varieties = list(set(self._varieties) | all_varieties)

    def fake_bird(self) -> str:
        num_descriptors = random.randrange(1, 4)
        descriptors = random.choices(self._descriptors, k=num_descriptors)
        variety = random.choice(self._varieties)

        bird = " ".join([*descriptors, variety])

        if bird in self._birds:
            return self.fake_bird()

        return bird

    def fake_birds(self) -> Iterator[str]:
        yield self.fake_bird()
