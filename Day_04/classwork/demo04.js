function f1() {
    console.log('Inside f1()')
}


function f2(n1, n2) {
    console.log('Inside f2()')
    console.log(`n1 - ${n1} , typeof(n1) - ${typeof (n1)}`)
    console.log(`n2 - ${n2} , typeof(n2) - ${typeof (n2)}`)

}

f1()
f2(10, 20)
f2(10, true)
f2(null, 'sunbeam')
f2(false)
f2()
