import java.util.*;

class VaultDoor8Solver {
    public static void main(String args[]) {
        // The target array from the original challenge
        char[] expected = {
            0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 
            0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 
            0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0x94, 
            0xC1, 0x95, 0xE0, 0xA4, 0xA5, 0x95, 0xF0, 0xE0 
        }; 

        VaultDoor8Solver solver = new VaultDoor8Solver();
        char[] flagContents = solver.unscramble(expected);
        
        // Wrap the solved password inside the traditional flag format
        System.out.print("picoCTF{");
        System.out.print(new String(flagContents));
        System.out.println("}");
    } 

    public char[] unscramble(char[] scrambled) {
        char[] a = new char[scrambled.length]; 
        for (int b = 0; b < scrambled.length; b++) {
            char c = scrambled[b]; 
            
            // Swaps are executed in the exact opposite sequence to unscramble the bits
            c = switchBits(c, 6, 7); 
            c = switchBits(c, 2, 5); 
            c = switchBits(c, 3, 4); 
            c = switchBits(c, 0, 1); 
            c = switchBits(c, 4, 7);
            c = switchBits(c, 5, 6); 
            c = switchBits(c, 0, 3); 
            c = switchBits(c, 1, 2); 
            
            a[b] = c; 
        } 
        return a;
    } 

    public char switchBits(char c, int p1, int p2) {
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); 
        char bit1 = (char)(c & mask1); 
        char bit2 = (char)(c & mask2); 
        char rest = (char)(c & ~(mask1 | mask2)); 
        char shift = (char)(p2 - p1); 
        char result = (char)((bit1 << shift) | (bit2 >> shift) | rest); 
        return result;
    } 
}

