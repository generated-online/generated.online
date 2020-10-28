export default (id) => {
    const colors = [
        "lightcoral",
        "lightcyan",
        "lightblue",
        "lightgoldenrodyellow",
        "lightgreen",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightsteelblue",
        "lightyellow",
    ]
    let num = parseInt(id, 36) % colors.length;
    return colors[num];
};