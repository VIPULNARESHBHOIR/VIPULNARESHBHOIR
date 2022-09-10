import java.util.Scanner;

class Restuarent{
    //method to calculate amount per distance
    public static int Dis_cost(int distance){
        if (distance <=3)
	    return 0;
	    else if (distance>=3 && distance <=6  )
	    return 1;
	    else
	    return 2;
	        
	    }
	public static void main(String[] args) {
	   
		Scanner x=new Scanner(System.in);
        System.out.println("ENTER V for veg N for Nonveg:");
		char k=x.next().charAt(0); // added charAt(0) also changed type of k to char
        System.out.println(k);
		if (k=='N') // "N" changed to 'N'
		{  
           System.out.print("QUANTITY N:");
		   int Quantity=x.nextInt();
		   int Ncost=15*Quantity;
           System.out.print("DISTANCE (in KMs):");
		   int distance=x.nextInt();
           x.close();
		   int Dcost=Dis_cost(distance);
		   int Total_cost=Ncost+Dcost;
		   System.out.println("Your total bill is "+Total_cost+"$");
		   	   
		}
		else {
           System.out.print("QUANTITY V:");
		   int Quantity=x.nextInt();
		   int Vcost=12*Quantity;
           System.out.print("DISTANCE (in KMs):");
		   int distance=x.nextInt();
		   int Dcost=Dis_cost(distance);
		   int Total_cost=Vcost+Dcost;
		   System.out.println("Your total bill is "+Total_cost+"$");
		}
	}
}