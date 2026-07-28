class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> map = new LinkedHashMap<>();

        for (String s : arr){
            if (!map.containsKey(s)){
                map.put(s, 1);
            } else {
                map.put(s, map.get(s) + 1);
            }
        }

        for (String key : map.keySet()) {
            if (map.get(key) == 1) {
                k--;
                if (k == 0) {
                    return key;
                }
            }
        }

        return "";
    }
}