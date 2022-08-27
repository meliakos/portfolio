
public class Gaupe extends Dyr {
	
	private double øretustlengde;

	public Gaupe(String iD, String kjønn, double lengde, double vekt, String tid, String sted, double øretustlengde) {
		super(iD, kjønn, lengde, vekt, tid, sted);
		this.øretustlengde = øretustlengde;
	}

	@Override
	public String toString() {
		return super.toString() + "[ øretustlengde: " + øretustlengde + "]";
	}
	
	
	
}
