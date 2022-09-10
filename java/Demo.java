class Method{
public static void method1(){
System.out.println("im now in method1");
}
public static void method2(){
System.out.println("im now in method2");
}
public static void method3(){
System.out.println("im now in method3");
}
}

class Demo {
public static void main(String[] args){
Method m=new Method();
m.method1();
m.method2();
m.method3();
System.out.println("now im out of the method class");
}
}

