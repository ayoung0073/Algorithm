class Solution {
    fun solution(num: Int): Int { // num은 val
        var n = num.toLong() // Int와 Long의 차이
        var cnt = 0
        while (cnt < 500) { 
            if (n == 1L) return cnt // input이 1인 경우 고려해서 cnt += 1과 위치 변경
            n = if (n % 2 == 0L) n / 2 else n * 3 + 1 
            cnt += 1 
        }
        return -1
    }
}
