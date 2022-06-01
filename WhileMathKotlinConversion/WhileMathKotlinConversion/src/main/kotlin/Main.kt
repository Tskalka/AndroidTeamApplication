fun main() {

    val equation: MutableList<String> = mutableListOf()

    val text = "5 + 3"
    for(item in text.split(" "))
    {
        equation.add(item)
    }

    // lambda functions, kotlin map with string to nameless operator function

    val add = {a: Float,b:Float -> a + b}//(Float, Float) -> Float = {a: Float, b: Float -> a.plus(b) }

    val ops = mapOf("+" to add,"-" to 2, "*" to 3, "/" to 4, "^" to 5 )

    fun doMath(oper: String, equation: MutableList<String>): MutableList<String> {
        val myIndex = equation.indexOf(oper)
        val result =  ops[oper](equation[myIndex -1].toFloat()),(equation[myIndex +1].toFloat()))
        print(result)
        equation[myIndex -1] = result.toString()
        return equation
        print(equation)

    }

    fun runEquation(equation: MutableList<String>): MutableList<String> {
        val operators: MutableList<String> = mutableListOf("^", "*", "/", "+", "-")
        var newEquation: MutableList<String> = equation
        for(oper in operators)
        {
            while (oper in equation)
            {
                newEquation = doMath(oper, equation)
            }
        }
        return newEquation
    }

    runEquation(equation)



}


