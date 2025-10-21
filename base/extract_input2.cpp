#include <iostream>
#include <thread>
#include <chrono>
#include <cassert>

void sleep_n_milliseconds(int milliseconds) {
    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));
}

int main() {
    int wait_time_ms;
    // std::cin >> wait_time_ms;

    auto start = std::chrono::steady_clock::now();
    sleep_n_milliseconds(wait_time_ms);
    auto end = std::chrono::steady_clock::now();

    auto actual_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    // std::cout << "Expected: " << wait_time_ms << " ms, actual: " << actual_ms << " ms\n";

    long diff = actual_ms - wait_time_ms;

    if (diff == 0)
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    else if (diff == -1)
        std::this_thread::sleep_for(std::chrono::milliseconds(400));
    else if (diff == 1)
        std::this_thread::sleep_for(std::chrono::milliseconds(600));
    else if (diff < -1)
        std::this_thread::sleep_for(std::chrono::milliseconds(300));
    else if (diff > 1)
        std::this_thread::sleep_for(std::chrono::milliseconds(700));

    // Optional assertions
    assert(actual_ms >= wait_time_ms - 2 && actual_ms <= wait_time_ms + 2 && "Sleep timing too inaccurate!");

    return 0;
}
