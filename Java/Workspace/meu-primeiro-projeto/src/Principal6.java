
public class Principal6 {

	public static void main(String[] args) {
		Integer i = 10; //new Integer(10);
		Integer a = new Integer(20);
		int y = a;
		
		byte b = i.byteValue();
		
		Integer i1 = 127;
		Integer i2 = 127;
		
		Integer i3 = 128;
		Integer i4 = 128;
		
		System.out.println(i1 == i2);
		System.out.println(i3 == i4);
		System.out.println(i3.equals(i4));
		
		//  wrapps
		// byte - Byte
		// short - Short
		// int - Integer
		// long - Long
		// float - Floag
		// double - Double
		// char - Character
		
	}
}
