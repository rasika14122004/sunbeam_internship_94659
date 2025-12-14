function f1() {
    console.log('Inside f1()')
}

function f1(n1, n2) {
    console.log('Inside f1(n1,n2)')
}

// JS does not support function overloading
f1(10, 20) // f1(n1,n2)
f1() // f1(n1,n2)