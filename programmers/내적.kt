class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        var answer = 0
        for (idx in a.indices) {
            answer += a[idx] * b[idx]
        }
        return answer
    }
}

// mapIndexed()

class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        return a.mapIndexed { idx, num -> num * b[idx] }.sum()
    }
}

// zip()

class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        return a.zip(b).map { it.first * it.second }.sum() 
    }
}
