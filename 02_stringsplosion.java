class main {
    public static void main(String[] args) {
        String s = "Code";
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            result += s.substring(0, i);
        }

        result += s;
        System.out.println(result);
    }
}
