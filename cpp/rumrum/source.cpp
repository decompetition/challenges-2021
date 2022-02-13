#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
#include <getopt.h> /* getopt */

#define BUFSIZE 128

std::condition_variable not_full;
std::condition_variable not_empty;
std::mutex mutex;
std::vector<std::string> buffer;
std::string FOUND = "";


uint32_t MurmurOAAT32(std::string key){
    uint32_t h(3323198485ul);
    for (auto c : key){
        h ^= c;
        h *= 0x5bd1e995;
        h ^= h >> 15;
    }
    return h;
}


std::string gen_random(std::string charset, const int length) {
    std::string tmp_s;
    tmp_s.reserve(length);

    for (int i = 0; i < length; ++i)
        tmp_s += charset[rand() % (charset.size() - 1)];

    return tmp_s;
}


void produce(std::string charset, const int length) {
    while(true){
        std::unique_lock<std::mutex> lock(mutex);

        not_full.wait(lock, [](){
            return buffer.size() != BUFSIZE || FOUND == "";
        });

        if(FOUND != "") return;

        buffer.push_back(gen_random(charset, length));
        lock.unlock();
        not_empty.notify_one();
    }
}


void consume(uint32_t hash) {
    while(true){
        std::unique_lock<std::mutex> lock(mutex);

        not_empty.wait(lock, [](){
            return buffer.size() != 0;
        });

        std::string guess = buffer.back();
        buffer.pop_back();

        if (MurmurOAAT32(guess) == hash){
            FOUND = guess;
            not_full.notify_one();
            return;
        }

        lock.unlock();
        not_full.notify_one();
    }
}


int main(int argc, char **argv) {
    int opt;
    int length = 4;
    uint32_t hash = 0;
    std::string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    while ((opt = getopt(argc, argv, "c:l:h:")) != -1){
        switch (opt)
            {
            case 'c':
                charset = std::string(optarg);
                break;
            case 'l':
                length = std::atoi(optarg);
                break;
            case 'h':
                hash = std::stoul(optarg, nullptr, 0);
                break;
            case ':':
                std::cout << "Missing argument for %c" << optopt << "\n";
                break;
            }
    }

    if(hash == 0){
        std::cout << "Usage: ./cracker -h 0xhash [-c charset] [-l length]\n";
        return -1;
    }

    std::thread producer = std::thread(produce, charset, length);
    std::thread consumer = std::thread(consume, hash);

    producer.join();
    consumer.join();

    std::cout << "[*] Cracked: " << FOUND << "\n";

}
