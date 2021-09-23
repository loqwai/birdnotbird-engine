#!/usr/bin/env python3

from bird_faker import BirdFaker


def main():
    bird_faker = BirdFaker()
    bird_faker.train('./birds.txt')

    with open('./fake_birds.txt', 'w') as f:
        for _ in range(10976):  # 10976 is the number of real birds
            f.write(bird_faker.fake_bird())
            f.write('\n')

    fake_birder = BirdFaker()
    fake_birder.train('./fake_birds.txt')
    print(bird_faker._descriptor_weights)
    print(fake_birder._descriptor_weights)


if __name__ == "__main__":
    main()
