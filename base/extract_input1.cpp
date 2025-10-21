#include <iostream>
#include <thread>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int wait_time_ms;
    cin >> wait_time_ms;

    // Precompute wait duration
    const auto wait_duration = milliseconds(wait_time_ms*100);

    // Record start
    auto start = steady_clock::now();

    // Sleep
    this_thread::sleep_for(wait_duration);

    // Optional: micro-adjust if system underslept
    auto end = steady_clock::now();
    auto actual = end - start;

    // If underslept more than 0.5 ms, sleep the remainder once
    if (actual < wait_duration) {
        auto remaining = wait_duration - actual;
        if (remaining > microseconds(500))
            this_thread::sleep_for(remaining);
    }

    return 0;
}
