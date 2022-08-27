//Amelia Kostov OBLIG2 OBJ2000

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
	
	private ArrayList<Dyr> hareliste = new ArrayList<>();
	private ArrayList<Dyr> gaupeliste = new ArrayList<>();
	private ArrayList<Dyr> dyreliste = new ArrayList<>();
	private ArrayList<Dyr> gjenfangstliste = new ArrayList<>();
	private ArrayList<Dyr> egenliste = new ArrayList<>();
	
	 
	
	public String finnNyHareID() {
		
		String nyHareID = "H" + Integer.toString(hareliste.size()+1);
		
		return nyHareID;
		
	}
	
	public String finnNyGaupeID() {
		
		String nyGaupeID = "G" + Integer.toString(gaupeliste.size()+1);
		
		return nyGaupeID;
	}
	
	
	public void nyHare(Hare hare) {
				
		hareliste.add(hare);
		dyreliste.add(hare);
	
	}
	
	public void nyGaupe(Gaupe gaupe) {	
		
		gaupeliste.add(gaupe);
		dyreliste.add(gaupe);

		
		
	}

	
	public void nyHareGjenfangst(HareGjenfangst hareGjenfangst) {
		
		hareliste.add(hareGjenfangst);
		gjenfangstliste.add(hareGjenfangst);

		
		
	}
	
	public void nyGaupeGjenfangst(GaupeGjenfangst gaupeGjenfangst) {
		
		gaupeliste.add(gaupeGjenfangst);
		gjenfangstliste.add(gaupeGjenfangst);

		
		
	}

	public Dyr finnHareBinært(String innID) {
		
		
		Collections.sort(hareliste);
		
		Dyr dummy = new Hare(innID, null,0, 0, null,null,null,null);
		
		int indeks = Collections.binarySearch(hareliste, dummy);
		
		if(indeks>=0) return hareliste.get(indeks);
			
		
		else return null;
		
		
		
		
		//FÅR IKKE UT ALT 
	}
	
	public Dyr finnGaupeBinært(String innID) {
		
		
		Collections.sort(gaupeliste);
		
		Dyr dummy = new Hare(innID, null,0, 0, null,null,null,null);
		
		int indeks = Collections.binarySearch(hareliste, dummy);
		
		if(indeks>=0) return hareliste.get(indeks);
			
		
		else return null;
		
	}
	
	public ArrayList<Dyr> finnHareLinjært(String innID) {
		
		for(int i=0; i < hareliste.size(); i++) {
			Dyr hare = hareliste.get(i);
			
			if(hare.getID().equals(innID)) egenliste.add(hare);
			System.out.println(egenliste);
			
		
		}
		System.out.println(egenliste);
		return egenliste;
		
		
		
	}
	
	public ArrayList<Dyr> finnGaupeLinjært(String innID) {
		
		for(int i=0; i < gaupeliste.size(); i++) {
			Dyr gaupe = gaupeliste.get(i);
			
			if(gaupe.getID().equals(innID)) egenliste.add(gaupe);
			System.out.println(egenliste);
			
		
		}
		System.out.println(egenliste);
		return egenliste;
		
		
		
	}
	
	
	public ArrayList<Dyr> getDyrene() {
		Collections.sort(dyreliste);
		return dyreliste;
	}
	
	public ArrayList<Dyr> getGjenfangstene() {
		Collections.sort(gjenfangstliste);
		return gjenfangstliste;
	}
}
