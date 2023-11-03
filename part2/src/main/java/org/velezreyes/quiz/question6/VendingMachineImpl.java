package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
    private static int quarters;
    
    @Override
    public void insertQuarter() {
        quarters += 25;
    }  
    
    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
//        Drinks objScottCola = new Drinks("ScottCola", true);
//        Drinks objKarenTea = new Drinks("KarenTea", false);


        if (quarters < 75 && "ScottCola".equals(name)){
            throw new NotEnoughMoneyException();
        }
        else if (quarters < 100 && "KarenTea".equals(name)){
            throw new NotEnoughMoneyException();
        }
        quarters = 0;
        
        if ("ScottCola".equals(name)){
            return new Drinks("ScottCola", true);
        }
        else if ("KarenTea".equals(name)){
            return new Drinks("KarenTea", false);
        }
        else {
            throw new UnknownDrinkException();
        }
        
        

    }
        public static VendingMachine getInstance() {
        return new VendingMachineImpl();
    }
    
        
        
        
        
        
        
    private class Drinks implements Drink{
        private String drink_name;
        private boolean fizzy;

      public Drinks(String drink_name, boolean fizzy) {
        this.drink_name = drink_name;
        this.fizzy = fizzy;
      }
        @Override
        public String getName() {
          return drink_name;
        }

        @Override
        public boolean isFizzy() {
          return fizzy;
        }

    }
}







    




