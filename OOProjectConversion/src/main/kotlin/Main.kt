import java.lang.Math.pow
import kotlin.math.pow

fun main() {
    // Lambda functions to be called in the map
    // Kotlin does not have a predefined exponent, so pow is needed
    val add = { a: Float, b: Float -> a + b }
    val sub = { a: Float, b: Float -> a - b }
    val mult = {a: Float, b: Float -> a * b}
    val div = {a: Float, b: Float -> a / b}
    val expo ={a: Float, b: Float -> a.pow(b)}

    // Defining the map/dictionary wiht the lambda functions
    val ops = mapOf("+" to add, "-" to sub, "*" to mult, "/" to div, "^" to expo)
    // Input text! change this to test code!
    val text = "5 + 2 * 3 - 1"

    //Split the input text by space, puts into a list called equation
    val equation = mutableListOf<String>()
    for(item in text.split(" "))
    {
        equation.add(item)
    }

    // Takes the input of an operator, calls the lambda function based on the key input into the function
    // Does the math based on the 1 number above and below the operator
    // returns equation
    fun doMath(oper: String, equation: MutableList<String>): MutableList<String>{
        //print(ops[oper]?.let { it(1f, 2f) })
        val myIndex = equation.indexOf(oper)
        val result = ops[oper]?.let { it(equation[myIndex - 1].toFloat(), equation[myIndex + 1].toFloat()) }

        equation.removeAt(myIndex - 1)
        equation.removeAt(myIndex -1)
        equation[myIndex -1] = result.toString()

        return equation

    }
    // runs the equation in the order of the operators lists, calls doMath() and returns new equation
    // added a print for testing
    fun runEquation(equation: MutableList<String>): MutableList<String>
    {
        val operators = listOf<String>("^","*","/","+","-")
        var newEquation = mutableListOf<String>()
        for(oper in operators)
        {
            while(oper in equation)
            {
                newEquation = doMath(oper, equation)
            }
        }
        //Test, remove if needed
        print(newEquation)
        return newEquation
    }


    runEquation(equation)

}