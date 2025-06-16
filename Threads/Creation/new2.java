class mytask implements Runnable
{
    public void run()
    {
        System.out.println("Hello World!");
    }
}
class mytask2 implements Runnable{
    public void run()
    {
        System.out.println("Hello World!  _ 2");
    }
}
class Main{
    public static void main (String [] args)
    {
        Thread t=new Thread(new mytask());
        t.start();
        Thread t2=new Thread (new mytask2());
        t2.start();
    }
}