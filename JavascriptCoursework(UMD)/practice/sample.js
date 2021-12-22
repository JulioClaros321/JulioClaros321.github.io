
function callbackFnDemo(arg1, cb) {
    if(arg1 === x){
        cb = arg1 * 2;
    }
} 

callbackFnDemo(2, (x) => {
    callbackFnDemo(x, function (x){
        callbackFnDemo(3, () => {
            x
        })
    })
})