



var result: Double = 0.0

fun main() {
    val input = readLine()!!.split(' ').map { it.toInt() }
    val moveCount = input[0]  // 이동 횟수
    val probabilities = input.subList(1, 5).map { it / 100.0 } // 확률 배열

    val dy = intArrayOf(1, -1, 0, 0)
    val dx = intArrayOf(0, 0, 1, -1)
    val visited = Array((moveCount + 1) * 2) { IntArray((moveCount + 1) * 2) }

    fun dfs(y: Int, x: Int, cnt: Int, percent: Double) {
        if (cnt == moveCount) {
            result += percent
            return
        }

        visited[y][x] = 1

        for (i in 0 until 4) {
            val ny = dy[i] + y
            val nx = dx[i] + x
            if (ny in 0 until (moveCount + 1) * 2 && nx in 0 until (moveCount + 1) * 2) {
                if (visited[ny][nx] == 0) {
                    dfs(ny, nx, cnt + 1, percent * probabilities[i])
                }
            }
        }

        visited[y][x] = 0
    }

    dfs(input[0], input[0], 0, 1.0)


    println(result)
}