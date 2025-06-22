class SharedResource
{
    int data;
    boolean available=false;
    synchronized void produce(int value)    //creating method for produce
    {
        try{
            while(available)
            {
                wait();
            }
            data=value;
            System.out.println("Produced data : "+data);
            available=true;
            notify();
        }
        catch(InterruptedException e)
        {
            System.out.println("Producer interrupted!");
        }
    }
 
    synchronized void  consume()    // creating method for consume
    {
        try
        {
            while(!available)
            {
                wait();
            }
            System.out.println("Consumed data : "+data);
            available=false;
            notify();
        }
        catch(InterruptedException e)
        {
            System.out.println("Consumer Interrupted!");
        }
    }
}
class Producer extends Thread
{
    SharedResource sr;
    Producer(SharedResource sr)
    {
        this.sr=sr;
    }
    int i=1;
    public void run()// this the task that the method should do
    {
        while(i<=5)
        {   sr.produce(i++);     // using the method created.  Here the increment value is the data
            try{
                Thread.sleep(1000);
            }
            catch(InterruptedException e)
            {
                System.out.println("Producion interrupted");
            }
        }
    }
}
class Consumer extends Thread
{
    SharedResource sr;

    Consumer(SharedResource sr)
    {
        this.sr=sr;
    }
    int i=1;
    public void run()  // this is the task that the method should do
    {
        
        while (i<=5)
        {sr.consume(); //using the method to consume
            try
            {
                Thread.sleep(1000);
            }
            catch(InterruptedException e)
            {
                System.out.println("Consumption Interrupted");
            }
            
        }
    }
}
class Main
{
    public static void main (String [] args)
    {
        SharedResource sr=new SharedResource();
        Producer p=new Producer(sr);
        Consumer c=new Consumer(sr);
        p.start();c.start();
    }
}