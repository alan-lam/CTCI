#include <iostream>
#include <string>

/* Replace all spaces in a string with "%20" */

int main() {
   std::string ret = "";
   std::string s;
   std::getline(std::cin, s);
   int length;
   std::cin >> length;
   for (int i = 0; i < length; i++) {
      if (isspace(s[i])) {
         ret = ret + "%20";
      }
      else {
         ret = ret + s[i];
      }
   }
   std::cout << ret << "\n";
   return 0;
}

