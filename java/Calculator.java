import java.util.Scanner;

class Cal{
    public int sum(int a,int b){
        return a+b;
    }
    public int sub(int a,int b){
        return (a-b);
    }
    public float mult(int a,int b){
        return a*b;
    }
    public float div(int a,int b){
        return b/a;
    }
}

class Calculator{
    public static void main( String[] args){
        Scanner sc=new Scanner(System.in);
        int a,b;
        int y;
        Cal obj=new Cal();
        System.out.println("enter 4. sub 3. add 2. div 1. add");
        System.out.print("a:");  a=sc.nextInt();
        System.out.print("b:");  b=sc.nextInt();

        y=sc.nextInt();
        
        switch(y)
        {
            case 1:
            System.out.println(obj.mult(a,b));
            break;
            case 2:
            System.out.println(obj.div(a,b));
            break;
            case 3:
            System.out.println(obj.sum(a,b));
            break;
            case 4:
            System.out.println(obj.sub(a,b));
            break;
            default:
            System.out.println("enter correct choice");
            break;
        
        }
        sc.close();

        
        



    }
    
}
