
import random
from typing import Iterator
from collections import defaultdict


class BirdFaker:
    def __init__(self) -> None:
        self._descriptors = []
        self._varieties = []
        self._birds = set()
        self._descriptor_weights = defaultdict(int)

    def train(self, filename) -> None:
        with open(filename) as f:
            self._birds.update([bird.strip() for bird in f])

        for bird in self._birds:
            *descriptors, variety = bird.strip().split(" ")

            self._descriptor_weights[len(descriptors)] += 1
            self._descriptors.extend(descriptors)
            self._varieties.append(variety)


    def fake_bird(self) -> str:
        descriptor_nums = sorted(self._descriptor_weights.keys())
        descriptor_weights = [self._descriptor_weights[num] for num in descriptor_nums]

        [num_descriptors] = random.choices(
                descriptor_nums,
                weights=descriptor_weights,
                k=1,
        )
        descriptors = random.choices(self._descriptors, k=num_descriptors)
        variety = random.choice(self._varieties)

        bird = " ".join([*descriptors, variety])

        if bird in self._birds:
            return self.fake_bird()

        self._birds.add(bird)
        return bird

    def fake_birds(self) -> Iterator[str]:
        yield self.fake_bird()
