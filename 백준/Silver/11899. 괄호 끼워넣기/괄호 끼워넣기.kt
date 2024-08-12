
import java.util.*
fun main(){

    val input = readLine()
    fun check(arr:String) : Int{
        var result = 0
        var stack = Stack<Char>()
        var cnt = 0
        for (i in 0.. arr.length-1){
//            print(arr[i])
            if (arr[i] =='(')
                stack.add(arr[i])
            else if (arr[i] ==')')
                if (stack.size==0)
                    cnt+=1
                else
                    stack.pop()
        }
        result = cnt+stack.size


        return  result
    }
    print(check(input.toString()))

}

