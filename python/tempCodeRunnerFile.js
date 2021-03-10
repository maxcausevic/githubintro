function parensValid(str){
    let map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    let stck = []
    for (let i = str.length; i>=0; i++){
        if(str[i]==='(' || str[i]==='[' || str[i]==='{' || str[i]===')' || str[i]===']'||str[i]==='}'){
            stck.push(s[i]);
        return true;
        }
        else return false;
    }
    return stck.length? false : true
}
console.log(parensValid('y(3(p)p(3)r)s'))