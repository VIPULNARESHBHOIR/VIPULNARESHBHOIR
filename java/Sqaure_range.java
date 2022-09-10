//enter the no.s and get there square as mo. of elements you want 
import java.util.Arrays;
import java.util.Scanner;
class Sqaure_range{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n;
        System.out.print("range:");// how may no.s square you want
        n=sc.nextInt();
        System.out.println("\nEnter Number according to your choice: "); //enter that no.s one by one
        int[] arr=new int[n];
        for (int i=0;i<n;i++)
        {
           arr[i]=sc.nextInt();
        }
        System.out.println("\n Square of numbers:\n");
        Arrays.sort(arr);//sorting array small to big no.
        for (int i=0;i<n;i++){
            System.out.println(arr[i]+" = "+arr[i]*arr[i]);
        }
        
    sc.close();// good habit to closed every open object of module 


    }
}
