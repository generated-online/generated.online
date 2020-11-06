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
    let num = parseInt(id, 36) % colors.length;
    return colors[num];
};