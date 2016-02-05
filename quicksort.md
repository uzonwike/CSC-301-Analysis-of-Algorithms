1.	static int partition(int a[], int left, int right) {

        int l_spot = left + 1;
        int r_spot = right;
        int temp = 0;

        while (r_spot > l_spot - 1) {
            if (a[r_spot] >= a[left])
                r_spot--;
            else if (a[l_spot] <= a[left])
                l_spot++;
            else {
                temp = a[r_spot];
                a[r_spot] = a[l_spot];
                a[l_spot] = temp;
            }
        }

        /*
         * After the loop, swap the pivot into the middle position at
         * r_spot==l_spot
         */
        temp = a[r_spot];
        a[r_spot] = a[left];
        a[left] = temp;
        return r_spot;
    }

	/*
	 * Quicksort method for an integer array.
	 */
	static void quicksort(String a[], int n) {
		quicksort_helper(a, 0, n - 1);
	}

	
	/*
	 * (continued) Recursive helper function for quicksort.
	 * It partitions the array, and then partitions the resulting
	 * half-arrays, recursing until it reaches single elements.
	 */
	static void quicksort_helper(String a[], int left, int right) {
		if (left < right) {
			int middle = partition(a, left, right);
			quicksort_helper(a, left, middle - 1);
			quicksort_helper(a, middle + 1, right);
		}
	}
