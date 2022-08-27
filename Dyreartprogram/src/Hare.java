//Amelia Kostov OBLIG2 OBJ2000

public class Hare extends Dyr {
	
	private String haretype;
	private String pelsfarge;
	
	
	public Hare(String iD, String kjønn, double lengde, double vekt, String tid, String sted, String haretype,
			String pelsfarge) {
		super(iD, kjønn, lengde, vekt, tid, sted);
		this.haretype = haretype;
		this.pelsfarge = pelsfarge;
	}


	@Override
	public String toString() {
		return super.toString() + "[ haretype: " + haretype + ", pelsfarge: " + pelsfarge + "]";
	}
	
	
	
	
	
	
}
