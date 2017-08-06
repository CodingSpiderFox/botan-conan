#include "botan/asn1_time.h"
#include <chrono>

int main()
  {
  Botan::X509_Time time{std::chrono::system_clock::now()};
  }


