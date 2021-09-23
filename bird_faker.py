
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

        for bird in self._birds:
            *descriptors, variety = bird.strip().split(" ")

            self._descriptors.extend(descriptors)
            self._varieties.append(variety)

    def fake_bird(self) -> str:
        num_descriptors = random.randrange(1, 4)
        descriptors = random.choices(self._descriptors, k=num_descriptors)
        variety = random.choice(self._varieties)

        bird = " ".join([*descriptors, variety])

        if bird in self._birds:
            return self.fake_bird()

        self._birds.add(bird)
        return bird

    def fake_birds(self) -> Iterator[str]:
        yield self.fake_bird()
