
public class Aula15{
	public static void main(String[] args){

		new Thread(t1).start();
		new Thread(t2).start();

	}
	private static Runnable t1 = new Runnable(){
	
		@Override
		public void run() {
			for(int i = 0; i<10;i++){
				System.out.println("Ride 1:" + i);

			}
		}
	};

	private static Runnable t2 = new Runnable(){
	
		@Override
		public void run() {
			for(int i = 0;i<10;i++){
				System.out.println("Ride 2:" + i);
			}
		}
	};

}
