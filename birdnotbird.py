#!/usr/bin/env python3

from bird_faker import BirdFaker


def main():
    bird_faker = BirdFaker()
    bird_faker.train('./birds.txt')

    for fake_bird in bird_faker.fake_birds():
        print(fake_bird)
        input


if __name__ == "__main__":
    main()
