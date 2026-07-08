class Tejas{
    String reverse(){
        char arr[] = {'(' , ')'};
        int l = 0;
        int r = arr.length -1;
        while(l < r){
            char t = arr[l];
            arr[l] = arr[r];
            arr[r] = t;
            l++;
            r--;
        }
        return new String(arr);

    }
    void main() {
        System.out.println(reverse());
    }
}