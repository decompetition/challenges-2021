#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
#include <getopt.h>

std::condition_variable not_full;
std::condition_variable not_empty;
std::mutex mutex;
std::vector<std::string> buffer;
std::string FOUND = "";

int main(int argc, char **argv) {
    // Let your threads crack this password!
}
