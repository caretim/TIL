fun main() {
    val input = readLine()
//    println("입력값$input")
    val(a,b,c)=input?.split(' ')!!.map { it.toInt() }
    if(a+b==c)
        print("$a+$b=$c")
    else if(a-b==c)
        print("$a-$b=$c")
    else if(a*b==c)
        print("$a*$b=$c")
    else if(a.toDouble()/b.toDouble()==c.toDouble())
        print("$a/$b=$c")
    else if(a==b+c)
        print("$a=$b+$c")
    else if(a==b-c)
        print("$a=$b-$c")
    else if(a==b*c)
        print("$a=$b*$c")
    else if(a.toDouble()==b.toDouble()/c.toDouble())
        print("$a=$b/$c")
}

