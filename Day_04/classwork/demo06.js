function f1(n1 = 1, n2 = 2, n3 = 3) {
    console.log('Inside f1()')
    console.log(`n1 - ${n1}, n2 - ${n2},  n3 - ${n3}`)
}

f1(10, 20, 30)
f1(10, 20)
f1(10)
f1()
f1(11, 22, 33, 44, 55)