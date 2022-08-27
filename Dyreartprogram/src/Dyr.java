//Amelia Kostov OBLIG2 OBJ2000

public class Dyr implements Comparable <Dyr> {
	
	private String ID;
	private String kjønn;
	private double lengde;
	private double vekt;
	private String tid;
	private String sted;
	
	
	public Dyr(String ID, String kjønn, double lengde, double vekt, String tid, String sted) {
		super();
		this.ID = ID;
		this.kjønn = kjønn;
		this.lengde = lengde;
		this.vekt = vekt;
		this.tid = tid;
		this.sted = sted;
	}
	
	

	public Dyr(String ID, double lengde, double vekt, String tid, String sted) {
		super();
		this.ID = ID;
		this.lengde = lengde;
		this.vekt = vekt;
		this.tid = tid;
		this.sted = sted;
	}



	public String getID() {
		return ID;
	}


	public void setID(String ID) {
		this.ID = ID;
	}


	public String getKjønn() {
		return kjønn;
	}


	public void setKjønn(String kjønn) {
		this.kjønn = kjønn;
	}


	public double getLengde() {
		return lengde;
	}


	public void setLengde(double lengde) {
		this.lengde = lengde;
	}


	public double getVekt() {
		return vekt;
	}


	public void setVekt(double vekt) {
		this.vekt = vekt;
	}


	public String getTid() {
		return tid;
	}


	public void setTid(String tid) {
		this.tid = tid;
	}


	public String getSted() {
		return sted;
	}


	public void setSted(String sted) {
		this.sted = sted;
	}
	
	public int compareTo(Dyr dyr) {
		return this.ID.compareTo(dyr.getID());
	}

	@Override
	public String toString() {
		return "[ID: " + ID + ", kjønn: " + kjønn + ", lengde: " + lengde + ", vekt: " + vekt + ", tid: " + tid
				+ ", sted: " + sted + "]";
	}
	
	
	
	
	
	
	
	
	
	
}
