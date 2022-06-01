//to run a kotlin file in the command line: kotlinc myfilename.kt -include-runtime -d myfilename.jar
//java -jar myfilename.jar

val add = {a: Double,b:Double -> a + b}

fun main() {
    println(add(5.toDouble(),7.toDouble()))
}