// LocalTime 이용 X

import java.util.*
import java.time.LocalTime

fun main() = with(Scanner(System.`in`)) {
  var hour = nextInt()
  var minute = nextInt()

  minute -= 45
  if (minute < 0) {
      minute += 60
      hour -= 1
  }
  
  if (hour < 0) {
      hour = 23
  }

  print("${hour} ${minute}")
}

// LocalTime 이용 O

import java.util.*
import java.time.LocalTime

fun main() = with(Scanner(System.`in`)) {
  val hour = nextInt()
  val minute = nextInt()

  val beforeTime = LocalTime.of(hour, minute).minusMinutes(45)

  print("${beforeTime.hour} ${beforeTime.minute}")
}
