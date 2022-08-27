//OBLIG1 Høst 2021 Amelia Marie Henriksen Kostov

import java.util.ArrayList;

import javax.swing.JOptionPane;

public class Kontroll {
	
	
	
	public void registrerOrdEnkelt(String nyttOrd, ArrayList <String> bibliotek) {
		
		//Legger ordet hentet fra input inn i listen
		bibliotek.add(nyttOrd);
		
		
	}
	
	public String skrivDiktEnkelt(ArrayList <String> bibliotek) {
		
		//Oppretter liste for å legge ordene inn i
		ArrayList <String> dikt = new ArrayList <String>();
		
		//finner størrelsen på biblioteket for å vite antall alternativ
		int antOrd = bibliotek.size();
		
		//for løkke for å finne 4x4 ord med randomisering av index		
		for (int y=0; y<4; y++) {
			for (int r=1; r < 5; r++) {	
				//Finner random nummer
			
				int randomnr = (int)(Math.random()*antOrd);
				//Henter ordet på den randomiserte indeksen
				String ord = bibliotek.get(randomnr);
				//Legger ordet inn i dikt-listen som skal printes
				dikt.add(ord);

			}
			
			//Legger til et linjeskift etter hver løkke
			dikt.add("\n");
			
			
		} 
		
		//formatterer listen for å fjerne komma og klammer
	
		String formattert = String.join(" ", dikt);
	
		
		return formattert;
		
	
		
		
	}
	
	public void registrerOrdAvansert(ArrayList <String> artikkel,ArrayList <String> adjektiv, ArrayList <String> substantiv, ArrayList <String> verb, String nyArtikkel,String nyttAdjektiv,String nyttSubstantiv,String nyttVerb) {
		
		//Legger ordene hentet fra grensesnittet inn i listene
		artikkel.add(nyArtikkel);
		adjektiv.add(nyttAdjektiv);
		substantiv.add(nyttSubstantiv);
		verb.add(nyttVerb);
		
		
	}
	
	public String skrivDiktAvansert(ArrayList <String> artikkel,ArrayList <String> adjektiv, ArrayList <String> substantiv, ArrayList <String> verb) {
		
		//Oppretter liste for å legge ord inn i
		ArrayList <String> dikt = new ArrayList <String>();
		
		//finner størrelsen på de ulike listene
		int antArtikkel = artikkel.size();
		int antAdjektiv = adjektiv.size();
		int antSubstantiv = substantiv.size();
		int antVerb = verb.size();
		
		//Løkke for å randomisere indeks og hente inn ord fra de ulike listene		
		for (int y=0; y<3; y++) {
			
				//Finner random nummer
			
				int randomnr1 = (int)(Math.random()*antArtikkel);
				int randomnr2 = (int)(Math.random()*antAdjektiv);
				int randomnr3 = (int)(Math.random()*antSubstantiv);
				int randomnr4 = (int)(Math.random()*antVerb);
				
			
				String ranArtikkel = artikkel.get(randomnr1);
				String ranAdjektiv = adjektiv.get(randomnr2);
				String ranSubstantiv = substantiv.get(randomnr3);
				String ranVerb = verb.get(randomnr4);
				
				//Legger ordene og et linjeskift inn i dikt-listen
				dikt.add(ranArtikkel);
				dikt.add(ranAdjektiv);
				dikt.add(ranSubstantiv);
				dikt.add(ranVerb);
				dikt.add("\n");
				
			
			
		} 
		
		//finner random ord og indekser for siste linje som er formulert i annen rekkefølge
		int randomnr4 = (int)(Math.random()*antVerb);
		int randomnr1 = (int)(Math.random()*antArtikkel);
		int randomnr2 = (int)(Math.random()*antAdjektiv);
		int randomnr3 = (int)(Math.random()*antSubstantiv);
		
		
	
		String ranArtikkel = artikkel.get(randomnr1);
		String ranAdjektiv = adjektiv.get(randomnr2);
		String ranSubstantiv = substantiv.get(randomnr3);
		String ranVerb = verb.get(randomnr4);
		
		//Legger de inn i riktig rekkefølge
		dikt.add(ranVerb);
		dikt.add(ranArtikkel);
		dikt.add(ranAdjektiv);
		dikt.add(ranSubstantiv);
		dikt.add("?");
		
		
		//Formatterer hele diktet for å fjerne komma og klammer
		String formattert = String.join(" ", dikt);
	
		return formattert;
		
		
		
	}
	
	
	
	

}
