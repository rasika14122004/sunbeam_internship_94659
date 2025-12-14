function add(n1, n2) {
    console.log(`Addition - ${n1 + n2}`)
}

// function alias
const myadd = add

add(10, 20)
myadd(11, 22)
console.log(`typeof(myadd) - ${typeof (myadd)}`)
console.log(`myadd - ${myadd}`)
