import java.util.Scanner;

public class ex {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);	
	
		System.out.println("Enter a sentence");
		
		String str = scan.nextLine();
		
		System.out.println("Words: " + str.split(" ").length);
		
		int lower=0, upper=0, digit=0, space=0, special=0;
		
		for(char ch : str.toCharArray()) {
			
			if(Character.isAlphabetic(ch)) {
				if(Character.isLowerCase(ch))
					lower++;
				else
					upper++;
			}			
			else if(Character.isDigit(ch))
				digit++;
			
			else if(ch == 32)
				space++;
			
			else
				special++;
		}		

		System.out.println(lower + " " + upper + " " + digit + " " + space + " " + special);
		
	}
}
