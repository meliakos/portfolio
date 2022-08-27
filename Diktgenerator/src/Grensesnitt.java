//OBLIG1 Høst 2021 Amelia Marie Kostov

import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Grensesnitt {
	
	//
	private final String[] ALTERNATIVER = {"Registrer ord", "Skriv dikt", "Tilbake"};
	private final String[] ALTHOVEDMENY = {"Enkelt dikt", "Avansert dikt", "Avslutt"};
	
	// Lager objekt av kontroll
	Kontroll kontroll = new Kontroll();
	
	//Oppretter biblioteket og lister til avansert dikt
	public ArrayList <String> bibliotek = new ArrayList <String>();
	public ArrayList <String> artikkel = new ArrayList <String>();
	public ArrayList <String> adjektiv = new ArrayList <String>();
	public ArrayList <String> substantiv = new ArrayList <String>();
	public ArrayList <String> verb = new ArrayList <String>();
	
	
	//Valg til meny
	public int lesValgHovedmeny() {
		int valg = JOptionPane.showOptionDialog(null,"Velg dikttype", "Diktgenerator Hovedmeny",JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ALTHOVEDMENY, ALTHOVEDMENY[0]);
		
		return valg;
	}
	
	public int lesValgEnkelmeny() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg for Enkelt Dikt", "Diktgenerator Enkelt dikt",JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ALTERNATIVER, ALTERNATIVER[0]);
		
		return valg;
	}
	
	public int lesValgAvansertmeny() {
		int valg = JOptionPane.showOptionDialog(null,"Gjør et valg for Avansert Dikt", "Diktgenerator Avansert dikt",JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, ALTERNATIVER, ALTERNATIVER[0]);
		
		return valg;
	}
	
	public void registrerOrdEnkelt(ArrayList<String> bibliotek) {
		
		String nyttOrd = JOptionPane.showInputDialog("Skriv inn et ord: ");
		
		kontroll.registrerOrdEnkelt(nyttOrd, bibliotek);
		
		
	}
	
	
	public void registrerOrdAvansert(ArrayList<String> artikkel, ArrayList<String> adjektiv, ArrayList<String> substantiv, ArrayList<String> verb) {
		
		String nyArtikkel = JOptionPane.showInputDialog("Skriv inn en artikkel: ");
		String nyttAdjektiv = JOptionPane.showInputDialog("Skriv inn et adjektiv: ");
		String nyttSubstantiv = JOptionPane.showInputDialog("Skriv inn et substantiv: ");
		String nyttVerb = JOptionPane.showInputDialog("Skriv inn et verb: ");
		
		kontroll.registrerOrdAvansert(artikkel, adjektiv, substantiv, verb, nyArtikkel, nyttAdjektiv, nyttSubstantiv, nyttVerb);
		

		
	}
	
	public void skrivDiktEnkelt(ArrayList<String> bibliotek) {
		
		JOptionPane.showMessageDialog(null, kontroll.skrivDiktEnkelt(bibliotek));
	}
	
	public void skrivDiktAvansert(ArrayList<String> artikkel, ArrayList<String> adjektiv, ArrayList<String> substantiv, ArrayList<String> verb) {
		
		JOptionPane.showMessageDialog(null, kontroll.skrivDiktAvansert(artikkel,adjektiv,substantiv,verb));
		
	}
	
	//Menyen
	public void enkelMeny() {
		boolean fortsett = true;
		while(fortsett) {
			//Skriver ut meny og leser menyvalg:
			int valg = lesValgEnkelmeny();
				
			switch(valg) {
			case 0 : registrerOrdEnkelt(bibliotek);
				break;
			case 1 : skrivDiktEnkelt(bibliotek);
				break;
			default : fortsett = false;
			}
		}
			
	}
	
	public void avansertMeny() {
		boolean fortsett = true;
		while(fortsett) {
			//Skriver ut meny og leser menyvalg:
			int valg = lesValgAvansertmeny();
				
			switch(valg) {
			case 0 : registrerOrdAvansert(artikkel,adjektiv,substantiv,verb);
				break;
			case 1 : skrivDiktAvansert(artikkel,adjektiv,substantiv,verb);
				break;
			default : fortsett = false;
			}
		}
			
	}
	
	public void hovedmeny() {
		boolean fortsett = true;
		while(fortsett) {
			//Skriver ut meny og leser menyvalg:
			int valg = lesValgHovedmeny();
				
			switch(valg) {
			case 0 : enkelMeny();
				break;
			case 1 : avansertMeny();
				break;
			default : fortsett = false;
			}
		}
			
	}
	

}


