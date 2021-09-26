/*
  1. sortedBy와 sortedWith의 차이점
  2. toTypedArray() 
*/

class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        return strings.sortedWith(compareBy({ it[n] }, { it })).toTypedArray() 
        // comparator을 지정해서 다중 기준을 둘 수 있다. 여기서는 우선 인덱스 n번째 글자를 기준으로 정렬한 후, 사전순으로 정렬한다.
        // toTypedArray(): List를 Array로 변환한다.
    }
}
