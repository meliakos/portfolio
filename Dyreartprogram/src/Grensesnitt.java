//Amelia Kostov OBLIG2 OBJ2000

import java.util.ArrayList;


import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class Grensesnitt {
	
	private final String[] alternativ_hovedmeny = {"Registrer nytt dyr","Registrer gjenfangst av dyr", "Søk etter dyr", "Lag rapport over dyr", "Avslutt" };
	private final String[] alternativ_registreringsmeny = {"Hare", "Gaupe", "Tilbake"};
	
	Kontroll kontroll = new Kontroll();
	
	public int lesValgHovedmeny() {
		
		int valg = JOptionPane.showOptionDialog(null, "Velkommen til Vulkanovia!", "Hovedmeny", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, alternativ_hovedmeny, alternativ_hovedmeny[0]);
		
		return valg;
	}
	
	public int lesValgRegistrerNyttDyr() {
		int valg = JOptionPane.showOptionDialog(null, "Hvilket dyr ønsker du å registrere?", "Registrer nytt dyr", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, alternativ_registreringsmeny, alternativ_registreringsmeny[0]);
	
		return valg;
	}
	
	public int lesValgRegistrerGjenfangst() {
		int valg = JOptionPane.showOptionDialog(null, "Hvilket dyr ønsker du å registrere gjenfangst på?", "Registrer gjenfangst", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, alternativ_registreringsmeny, alternativ_registreringsmeny[0]);
	
		return valg;
	}
	
	public void registrerNyHare() {
		
		JTextField kjønn_felt = new JTextField();
        JTextField lengde_felt = new JTextField();
        JTextField vekt_felt = new JTextField();
        JTextField tid_felt = new JTextField();
        JTextField sted_felt = new JTextField();
        JTextField haretype_felt = new JTextField();
        JTextField pelsfarge_felt = new JTextField();
        
        Object [] felt = {
            "Kjønn:", kjønn_felt,
            "Lengde:", lengde_felt,
            "Vekt:", vekt_felt,
            "Tid:", tid_felt,
            "Sted:", sted_felt,
            "Haretype:", haretype_felt,
            "Pelsfarge:", pelsfarge_felt
        };
        
        JOptionPane.showConfirmDialog(null,felt,"Fyll ut info om ny Hare",JOptionPane.OK_CANCEL_OPTION);
        
        String kjønn = kjønn_felt.getText();
        String lengde_streng = lengde_felt.getText();
        double lengde = Double.parseDouble(lengde_streng);
        String vekt_streng = vekt_felt.getText();
        double vekt = Double.parseDouble(vekt_streng);
        String tid = tid_felt.getText();
        String sted = sted_felt.getText();
        String haretype = haretype_felt.getText();
        String pelsfarge = pelsfarge_felt.getText();
        
        String ID = kontroll.finnNyHareID();
       
        kontroll.nyHare(new Hare(ID, kjønn, lengde, vekt, tid, sted, haretype, pelsfarge));
        
        
        
	}
	
	
	public void registrerNyGaupe() {
		JTextField kjønn_felt = new JTextField();
        JTextField lengde_felt = new JTextField();
        JTextField vekt_felt = new JTextField();
        JTextField tid_felt = new JTextField();
        JTextField sted_felt = new JTextField();
        JTextField øretustlengde_felt = new JTextField();
        
        
        Object [] felt = {
            "Kjønn:", kjønn_felt,
            "Lengde:", lengde_felt,
            "Vekt:", vekt_felt,
            "Tid:", tid_felt,
            "Sted:", sted_felt,
            "Øretustlengde:", øretustlengde_felt
            
        };
        
        JOptionPane.showConfirmDialog(null,felt,"Fyll ut info om ny Hare",JOptionPane.OK_CANCEL_OPTION);
        
        String kjønn = kjønn_felt.getText();
        String lengde_streng = lengde_felt.getText();
        double lengde = Double.parseDouble(lengde_streng);
        String vekt_streng = vekt_felt.getText();
        double vekt = Double.parseDouble(vekt_streng);
        String tid = tid_felt.getText();
        String sted = sted_felt.getText();
        String øretustlengde_streng = øretustlengde_felt.getText();
        double øretustlengde = Double.parseDouble(øretustlengde_streng);
        
        String ID = kontroll.finnNyGaupeID();
       
        kontroll.nyGaupe(new Gaupe(ID, kjønn, lengde, vekt, tid, sted, øretustlengde));
        
        
	}
	
	public void registrerHareGjenfangst() {
		
		JTextField ID_felt = new JTextField();
        JTextField lengde_felt = new JTextField();
        JTextField vekt_felt = new JTextField();
        JTextField tid_felt = new JTextField();
        JTextField sted_felt = new JTextField();
        JTextField pelsfarge_felt = new JTextField();
        
        Object [] felt = {
            "ID:", ID_felt,
            "Lengde:", lengde_felt,
            "Vekt:", vekt_felt,
            "Tid:", tid_felt,
            "Sted:", sted_felt,
            "Pelsfarge:", pelsfarge_felt
        };
        
        JOptionPane.showConfirmDialog(null,felt,"Fyll ut gjenfangstinfo om Hare",JOptionPane.OK_CANCEL_OPTION);

        String ID = ID_felt.getText();
        String lengde_streng = lengde_felt.getText();
        double lengde = Double.parseDouble(lengde_streng);
        String vekt_streng = vekt_felt.getText();
        double vekt = Double.parseDouble(vekt_streng);
        String tid = tid_felt.getText();
        String sted = sted_felt.getText();
        String pelsfarge = pelsfarge_felt.getText();
		
		
		kontroll.nyHareGjenfangst(new HareGjenfangst(ID, lengde, vekt, tid, sted,pelsfarge));
	}
	
	public void registrerGaupeGjenfangst() {
		
		JTextField ID_felt = new JTextField();
        JTextField lengde_felt = new JTextField();
        JTextField vekt_felt = new JTextField();
        JTextField tid_felt = new JTextField();
        JTextField sted_felt = new JTextField();
        JTextField øretustlengde_felt = new JTextField();
        
        Object [] felt = {
            "ID:", ID_felt,
            "Lengde:", lengde_felt,
            "Vekt:", vekt_felt,
            "Tid:", tid_felt,
            "Sted:", sted_felt,
            "Øretustlengde:", øretustlengde_felt
        };
        
        JOptionPane.showConfirmDialog(null,felt,"Fyll ut gjenfangstinfo om Gaupe",JOptionPane.OK_CANCEL_OPTION);

        String ID = ID_felt.getText();
        String lengde_streng = lengde_felt.getText();
        double lengde = Double.parseDouble(lengde_streng);
        String vekt_streng = vekt_felt.getText();
        double vekt = Double.parseDouble(vekt_streng);
        String tid = tid_felt.getText();
        String sted = sted_felt.getText();
        String øretustlengde_streng = øretustlengde_felt.getText();
        double øretustlengde = Double.parseDouble(øretustlengde_streng);
		
		
		kontroll.nyGaupeGjenfangst(new GaupeGjenfangst(ID, lengde, vekt, tid, sted,øretustlengde));
	
	}
	
	public void finnDyr() {
		
		String innID = JOptionPane.showInputDialog("Skriv inn ID: ");
		if(innID.startsWith("H")) {
			Dyr dyr = kontroll.finnHareBinært(innID); 
			if(dyr !=null) {
				
				ArrayList<Dyr> egenliste = kontroll.finnHareLinjært(innID);
				String uttekst = "";
				for (Dyr d: egenliste) {
					uttekst += d.toString() + "\n";
				}
				JOptionPane.showMessageDialog(null,uttekst);
			}
				
			else JOptionPane.showMessageDialog(null, "Finner ikke det registrerte dyret.");
			}
		else { 
			
			Dyr dyr = kontroll.finnGaupeBinært(innID);
			if(dyr !=null) {
				
				ArrayList<Dyr> egenliste = kontroll.finnGaupeLinjært(innID);
				String uttekst = "";
				for (Dyr d: egenliste) {
					uttekst += d.toString() + "\n";
				}
				JOptionPane.showMessageDialog(null,uttekst);
			}
				
			else JOptionPane.showMessageDialog(null, "Finner ikke det registrerte dyret.");
		}
		
	}
		
	public void lagRapport() {
		
		
		ArrayList<Dyr> dyreliste = kontroll.getDyrene();
		String uttekst = "Dyr: " + "\n" ;
		for (Dyr d : dyreliste) {
			uttekst += d.toString() + "\n";
		}
		
		ArrayList<Dyr> gjenfangstliste = kontroll.getGjenfangstene();
		uttekst += "Gjenfangster: " + "\n" ;
		for (Dyr g : gjenfangstliste) {
			uttekst += g.toString() + "\n";
		}
		
		JOptionPane.showMessageDialog(null, uttekst);
		
	}
	
	// Hovedmenyen
	
	public void hovedmeny() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValgHovedmeny();
			
			switch(valg) {
			case 0 : registrerNytt();
				break;
			case 1 : registrerGjenfangst();
				break;
			case 2 : finnDyr();
				break;
			case 3 : lagRapport();
				break;
			default : fortsett = false;
			}
		}
	}
		
		
		//Registreringsmeny
		
	public void registrerNytt() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValgRegistrerNyttDyr();
			
			switch(valg) {
			case 0 : registrerNyHare();
				break;
			case 1 : registrerNyGaupe();
				break;
			default : fortsett = false;
			}
			
		}
	}
		
	public void registrerGjenfangst() {
		boolean fortsett = true;
		while(fortsett) {
			int valg = lesValgRegistrerGjenfangst();
			
			switch(valg) {
			case 0 : registrerHareGjenfangst();
				break;
			case 1 : registrerGaupeGjenfangst();
				break;
			default : fortsett = false;
			}
			
		}
	}
	
	
	
		
}
