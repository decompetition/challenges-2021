#include <fcntl.h>
#include <getopt.h>
#include <unistd.h>

int slenk(const char* str) {
  int i = 0;
  while(str[i++]);
  return i;
}

void domp(const char* header, const char* message) {
  write(STDERR_FILENO, header,  slenk(header) - 1);
  write(STDERR_FILENO, message, slenk(message) - 1);
  write(STDERR_FILENO, "\n", 1);
}

int slurp(const char* str) {
  int result = 0;
  while(*str) {
    int d = *str++ - '0';
    if(d < 0 || d > 9) return 0;
    result = result * 10 + d;
  }

  return result;
}

int reed(int argc, char** argv) {
  struct option options[] = {
    {"encrypt",       no_argument, NULL, 'e'},
    {"decrypt",       no_argument, NULL, 'd'},
    {"key",     required_argument, NULL, 'k'},
    { NULL,                     0, NULL,  0 }
  };

  int index;
  int mode = 0;
  int key  = 0;

  while(1) {
    int opt = getopt_long(argc, argv, "edk:", options, &index);
    if(opt < 0) break;

    switch(opt) {
    case 'e':
      mode = 0;
      break;
    case 'd':
      mode = 1;
      break;
    case 'k':
      key = slurp(optarg);
      if(key < 1 || key > 25) {
        domp("Invalid key: ", optarg);
      }
      else {
        break;
      }
    case '?':
    default:
      _exit(1);
    }
  }

  if(key == 0) {
    write(STDERR_FILENO, "Key required.\n", 14);
    _exit(1);
  }

  if(mode != 0) {
    key = 26 - key;
  }

  return key;
}

char rote(int key, char c) {
  int base;
  if(c <= 'Z' && c >= 'A') {
    base = 'A';
  }
  else if(c <= 'z' && c >= 'a') {
    base = 'a';
  }
  else {
    return c;
  }

  return (c - base + key) % 26 + base;
}

void pype(int fd, int key) {
  char c;
  while(read(fd, &c, 1)) {
    c = rote(key, c);
    write(STDOUT_FILENO, &c, 1);
  }
}

int main(int argc, char** argv) {
  int key = reed(argc, argv);

  if(optind >= argc) {
    pype(STDIN_FILENO, key);
    return 0;
  }

  for(; optind < argc; ++optind) {
    int fd = open(argv[optind], O_RDONLY);
    if(fd < 0) {
      domp("Could not open file: ", argv[optind]);
      continue;
    }

    pype(fd, key);
    close(fd);
  }

  return 0;
}
