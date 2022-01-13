/**
 * Test
 */
public class Capacity {

    public static void main(String[] args) {
        double f = Integer.parseInt(args[0]);
        double phi = Double.parseDouble(args[1]);
        Capacity t = new Capacity();
        System.out.println("C = " + t.capacity(f, phi));
    }

    private double capacity(double f, double phi) {
        double res = Math.sqrt(1 / (Math.pow(2 * Math.PI * f, 2) * Math.pow(50 / Math.cos(phi), 2) - Math.pow(50, 2)));
        return res;
    }
}