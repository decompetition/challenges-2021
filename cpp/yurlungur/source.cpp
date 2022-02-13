#include <iostream>
#include <random>

using RNG = std::mt19937_64;

RNG create(int argc, char** argv) {
  if(argc == 1) {
    RNG::result_type seed = std::random_device()();
    return RNG(seed);
  }

  if(argc == 2) {
    RNG::result_type seed = std::atoi(argv[1]);
    return RNG(seed);
  }

  throw std::runtime_error("The serpent devours you.");
}

void mutate(RNG& rng, unsigned char state[3]) {
  std::uniform_int_distribution<int> index(0, 2);
  std::uniform_int_distribution<int> delta(0, 1);

  unsigned char& c = state[index(rng)];
  c += 2 * delta(rng) - 1;

  if(c > 9) c = 1;
  if(c > 5) c = 4;
}

int escape(unsigned char state[3]) {
  return 36 * state[0] + 6 * state[1] + state[2] + 16;
}

int main(int argc, char** argv) {
  RNG rng = create(argc, argv);

  std::uniform_int_distribution<unsigned char> dist(0, 5);
  unsigned char state[3] = {
    dist(rng),
    dist(rng),
    dist(rng)
  };

  char c;
  while(std::cin.get(c)) {
    std::cout << "\x1b[38;5;" << escape(state) << 'm' << c;
    mutate(rng, state);
  }

  std::cout << "\x1b[0m";
  return 0;
}
