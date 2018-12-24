using System;
namespace LogicApplication {
 class Logic {
  static void Main(string[] args) {
   int t = Convert.ToInt32(Console.ReadLine());
   while (t > 0) {
    long n, x, res;
    n = long.Parse(Console.ReadLine());
    x = (n * (n + 1)) / 2;
    res = x * x;
    Console.WriteLine(res % 1000000007 + "\n");
    t--;
   }
  }
 }
}