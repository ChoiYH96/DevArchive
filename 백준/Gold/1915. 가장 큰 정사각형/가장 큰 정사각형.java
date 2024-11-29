import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(reader.readLine());

        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());

        int[][] squareMap = new int[n][m];
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            String[] temp = reader.readLine().split("");
            for (int j = 0; j < m; j++) {
                count += Integer.parseInt(temp[j]);
                squareMap[i][j] = Integer.parseInt(temp[j]);
            }
        }
        
        if (count == 0) {
            System.out.println(0);
        } else if (Math.min(n,m) == 1) {
            System.out.println(1);
        } else {
        int maxValue = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                int check = Math.min(Math.min(squareMap[i-1][j-1],squareMap[i-1][j]),squareMap[i][j-1]);
                squareMap[i][j] = Math.min(check,squareMap[i][j]) != 0? check+1: squareMap[i][j];
                maxValue = Math.max(maxValue,squareMap[i][j]);
            }
        }
        System.out.println(maxValue*maxValue);
        }
    }
}