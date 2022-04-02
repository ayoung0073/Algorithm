class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val impossibleStudents = lost - reserve
        val realReserve = reserve - lost

        realReserve.forEach {
            when {
                it - 1 in impossibleStudents -> impossibleStudents.remove(it - 1)
                it + 1 in impossibleStudents -> impossibleStudents.remove(it + 1)
            }
        }

        return n - impossibleStudents.size
    }

    operator fun IntArray.minus(arr: IntArray): MutableList<Int> =
        this.filter { it !in arr }.toMutableList()
}
