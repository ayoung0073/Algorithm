class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer: MutableList<Int> = ArrayList()
        val s1 = intArrayOf(1, 2, 3, 4, 5)
        val s2 = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
        val s3 = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        val ans = IntArray(3)
        for (i in answers.indices) {
            if (answers[i] == s1[i % s1.size]) ans[0] += 1
            if (answers[i] == s2[i % s2.size]) ans[1] += 1
            if (answers[i] == s3[i % s3.size]) ans[2] += 1
        }
        val maxValue = ans.max()
        if (maxValue == ans[0]) answer.add(1)
        if (maxValue == ans[1]) answer.add(2)
        if (maxValue == ans[2]) answer.add(3)
        return answer.toIntArray()
    }
}
