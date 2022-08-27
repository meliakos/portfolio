//Amelia Kostov OBLIG2 OBJ2000

public class HareGjenfangst extends Dyr {
	
	private String pelsfarge;

	

	public HareGjenfangst(String ID, double lengde, double vekt, String tid, String sted, String pelsfarge) {
		super(ID, lengde, vekt,tid, sted);
		this.pelsfarge = pelsfarge;
	}



	@Override
	public String toString() {
		return super.toString() + "Gjenfangst av Hare [pelsfarge: " + pelsfarge + "]";
	}
	
	
	
}
