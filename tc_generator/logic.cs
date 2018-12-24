using System;

namespace HelloWorldApplication {
   
   class HelloWorld {
      
      static void Main(string[] args) {
         Console.WriteLine("Hello World");
         Console.ReadKey();
         
         int t = Convert.ToInt32(Console.ReadLine());
         
         while(t>0)
         {
             long n,x,res;
             n = long.Parse(Console.ReadLine());
             x= (n*(n+1))/2;
             res=x*x;
             Console.WriteLine(res%1000000007 + "\n");
             t--;
         }
      }
   }
}