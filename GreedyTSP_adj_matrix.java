/**
 * Created by saurabh on 2016-10-21.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class adjcgreedy {

    public static Double dist2(Double x1, Double y1, Double x2, Double y2) {
        Double distance = Math.hypot(x2 - x1, y2 - y1);
        // Round distance
        //int intdistance = (int) Math.rint(x);

        //System.out.println("Distance = " + distance);
        return distance;
    }

    public static void main(String[] args){

        /*
10
95.0129 61.5432
23.1139 79.1937
60.6843 92.1813
48.5982 73.8207
89.1299 17.6266
76.2097 40.5706
45.6468 93.5470
1.8504 91.6904
82.1407 41.0270
44.4703 89.3650
*/
        // Read the input
//
//        Scanner sc = new Scanner(System.in);
//        while (sc.hasNextLong()) {
//            long a = sc.nextLong(), b = sc.nextLong();
//            // solve test case and output answer
//        }

        Scanner sc = new Scanner(System.in);
        String in = sc.next();

        int n = Integer.parseInt(in);
        Double[] cordinates = new Double[n*2];
        Double test = 0.0;
        for(int i = 0; i < n * 2 ; i++){
                //cordinates = "";
            //while (sc.hasNextLine()) {
                //test = sc.nextDouble();
                //System.out.println(test);
            cordinates[i] = sc.nextDouble();
            //}

        }

        //String cordinates = "6 95.0129 61.5432 23.1139 79.1937 60.6843 92.1813 48.5982 73.8207 89.1299 17.6266 45.67 93.33";
        //Split by spaces
        //String[] inputAsArray = cordinates.split(" ");
        //Integer numberofcities = Integer.valueOf(inputAsArray[0]).intValue();  // N
        Integer numberofcities = n;
        // Creating the adjacency matrix

        int rowSize = numberofcities;
        int colSize = numberofcities;
        int[][] myArray = new int[rowSize][colSize]; // Initialise the no of rows and col's
       // List b = Arrays.asList(ArrayUtils.toObject(myArray));


        int count = 0;

        for(int i = 0; i < rowSize ; i++) {
            for(int j = 0; j < colSize ; j++, count++) {
                //myArray[i][j] = dist2(Double i*2+1, Double i*2+2, Double j*2+1, Double j*2+2)  //
                Double x1 = cordinates[i*2];
                Double y1 = cordinates[i*2 + 1];
                Double x2 = cordinates[j*2];
                Double y2 = cordinates[j*2 + 1];

                //System.out.println(x1);
                myArray[i][j] = (int) Math.rint(dist2(x1, y1, x2, y2));
                // myArray[i][j] = dist2(coords[i], coords[j]);   // Replace with distance between city i and j
            }
        }
// Print the created adjacency matrix with distances
        /*
        for(int i = 0; i < rowSize; i++) {

            // print the row of space-separated values
            for(int j = 0; j < colSize; j++) {
                System.out.print(myArray[i][j] + " ");
            }
            // end of row is reached, print newline
            System.out.println();
        }
*/
        //int[] tour = {0};
        //List tour = new ArrayList<Integer>(); // New array for the tour, length 0
        ArrayList<Integer> tour = new ArrayList<>();
        tour.add(0);
        boolean[] used = new boolean[myArray.length];
        used[0] = true;


        int best = -1;

        int index = 0;
        int currentrow = 0;
//
        // Find  the smallest number

        for (int i = index; i < myArray.length -1 ; i++ ){
            int smallest = 50000000;// each row
            for (int j = 0; j < myArray.length  ; j++ ){

                //int current_count = 0;
                if (!used[j] && myArray[currentrow][j] != 0  ){
                    if(myArray[currentrow][j] < smallest ){
                        smallest = myArray[currentrow][j];
                         index = j;

                        //System.out.println(used[2]);


                    }

                }


            }
            currentrow = index;
            used[index] = true;
            //tour.add(index); // Add city to the tour
            tour.add(currentrow);
            //System.out.println(tour);

        }
        //System.out.println(tour);
        tour.forEach(System.out::println);
        //tour.toArray();
        //for (int i = 0; i < n; i++){
        //    System.out.println(tour[i]);
        //}











        // Create an array with cities

//        for(int i = 0; i < numberofcities; i++){
//
//            Double[] citycoord = {Double.valueOf(inputAsArray[i * 2 + 1]).doubleValue(), Double.valueOf(inputAsArray[i * 2 + 2]).doubleValue()};
//
//            // Print the list of cities in citycoord
//
//            for (int j = 0; j < citycoord.length; j++){
//
//                System.out.println(citycoord[j] + " ");
//            }
//
//
//        }





    }



}
