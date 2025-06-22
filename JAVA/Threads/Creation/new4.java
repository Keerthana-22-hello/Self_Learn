class Main
{
    public static void main (String [] args)
    {
        Thread t=new Thread(() ->
        {
            System.out.println("Hello World !");
        });
        t.start();
        Thread t2=new Thread(()->{
            System.out.println("Hello World ! - 2");
        });
        t2.start();
    }
}