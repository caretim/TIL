import kotlin.math.max
import kotlin.math.min

fun main() {
    val k = readLine()!!.toInt()
    val word = readLine().toString()
    var result = 0
    var temp_a = word[0]
    var temp_cnt = 1
    var pre_cnt = 0


    //문자열이 변경 될 때
    //1. 변경시 count세면서
    for (i in 1 until k){
        if (word[i] == temp_a){
            temp_cnt+=1
        }

        else{
            result = max((min(pre_cnt,temp_cnt)),result)
            temp_a = word[i]
            pre_cnt = temp_cnt
            temp_cnt = 1
        }
    }
    result = max((min(pre_cnt,temp_cnt)),result)
    println(result*2)
}