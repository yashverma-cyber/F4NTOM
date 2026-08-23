import java.util.*;

public class VD3solver {
    public static void main(String args[]) {
        String scrambled = "jU5t_a_sna_3lpm16g041_u_4_m2r547";
        char[] password = new char[32];
        int i;

        // Loop 1: Map positions 0 to 7
        for (i = 0; i < 8; i++) {
            password[i] = scrambled.charAt(i);
        }

        // Loop 2: Map positions 8 to 15
        for (; i < 16; i++) {
            password[23 - i] = scrambled.charAt(i);
        }

        // Loop 3: Map even positions from 16 to 30
        for (; i < 32; i += 2) {
            password[46 - i] = scrambled.charAt(i);
        }

        // Loop 4: Map odd positions from 31 down to 17
        for (i = 31; i >= 17; i -= 2) {
            password[i] = scrambled.charAt(i);
        }

        // Print the final reconstructed flag
        System.out.println("picoCTF{" + new String(password) + "}");
    }
}

