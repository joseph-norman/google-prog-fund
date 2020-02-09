// withoutString.java 
// 
// Given two strings, base and remove, reurn a version of the base string where all
// instances of the remove string have been removed (not case sensitive). You may
// assume that the remove string is of length 1 or more. 
//
// Remove only non-overlapping instances, so with "xxx", removing "xx" leaves "x".
//
// withoutString("Hello there", "llo") -> "He there"
// withoutString("Hello there", "e") -> "Hllo thr"
// withoutString("Hello there", "x") -> "Hello there"
class main {
    public static void main(String[] args) {
        String base = "This is a FISH";
        String remove = "IS";
        String result = "";

        for (int i = 0; i < base.length(); i++) {
            if (base.charAt(i) == remove.charAt(0)) {
                if (remove.length() == 1) {
                    // Remove it
                    base = base.replace(base.valueOf(base.charAt(i)), "");
                } else {
                    String toCompare = base.substring(i, i + remove.length());
                    
                    System.out.println("Compare:" + toCompare);

                    if (toCompare.equals(remove)) {
                        base = base.replace(toCompare, "");
                    }
                }
            }
        }

        System.out.println(base);
    }
}







