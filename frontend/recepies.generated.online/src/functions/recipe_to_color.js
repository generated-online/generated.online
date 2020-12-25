function stringToIntHash(str, upperbound, lowerbound) {
    let result = 0;
    for (let i = 0; i < str.length; i++) {
        result = result + str.charCodeAt(i);
    }

    if (!lowerbound) lowerbound = 0;
    if (!upperbound) upperbound = 500;

    return (result % (upperbound - lowerbound)) + lowerbound;
}

export default (id) => {
    const colors = [
        "lightcoral",
        "lightcyan",
        "lightblue",
        "lightgoldenrodyellow",
        "lightgreen",
        "lightpink",
        "lightsalmon",
        "lightskyblue",
        "lightsteelblue",
        "lightyellow",
        "lightseagreen",
    ]
    let num;
    if (id === null){
        // lightblue is default color
        num = 2
    }
    else {
        num = stringToIntHash(id, colors.length, 0);
    }
    return colors[num];
};