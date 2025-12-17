const arr=[11,22,33,44,55,66,77,88]

for(const e of arr)
    if(e% 2==0)
        console.log(e)

console.log("using filter ->")
arr
    .filter((value,index,array)=>{
        return value %2==0
    })
    .forEach(value=> console.log(value))
    console.log("using filter in single line ->")
    arr.filter(value=> value%2!=0).forEach(value=>console.log(value))