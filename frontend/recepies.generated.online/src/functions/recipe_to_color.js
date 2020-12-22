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
    // lightblue is default color
    let num = (parseInt(id, 20) || 2) % colors.length;
    return colors[num];
};