//Amelia Kostov OBLIG2 OBJ2000

public class GaupeGjenfangst extends Dyr {
	
	private double øretustlengde;

	
	public GaupeGjenfangst(String iD, double lengde, double vekt, String tid, String sted, double øretustlengde) {
		super(iD, lengde, vekt, tid, sted);
		this.øretustlengde = øretustlengde;
	}



	@Override
	public String toString() {
		return super.toString()+ "Gjenfangst av Gaupe [ øretustlengde: " + øretustlengde + "]";
	}
	
	
	
}
