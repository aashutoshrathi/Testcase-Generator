import java.util.*;

public class logic {
	public static void main(String[] args) {
		int t;
		Scanner s = new Scanner(System.in);
		t = s.nextInt();
		while(t-->0) {
			long n, x, res;
			n = s.nextLong();
			x = (n*(n+1))/2;
			res = x*x;
			System.out.println(res%1000000007);
		}
		s.close();
	}
}
