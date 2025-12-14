function arithmeticExecuter(fn) {
    const res1 = fn(20, 10)
    console.log(`Result in Executer - ${res1}`)
}

arithmeticExecuter((n1, n2) => n1 + n2)
arithmeticExecuter((n1, n2) => n1 - n2)
arithmeticExecuter((n1, n2) => n1 * n2)
arithmeticExecuter((n1, n2) => n1 / n2)
