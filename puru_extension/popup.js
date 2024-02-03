const HARM_LEVEL_CLASS = {
    0: "list-group-item-success",
    1: "list-group-item",
    2: "list-group-item-warning",
    3: "list-group-item-danger"
}
function tileToHarmLevel(tile) {
    var className = tile.className
    if (className.includes("danger")) {
        return 3;
    } else if (className.includes("warning")) {
        return 2;
    } else if (className.includes("success")) {
        return 1;
    } else {
        return 0;
    }
}
function createIngredientTile(ingredient) {
    try {
        var info = queryIngredient(ingredient)
    } catch (err) {
        var info = {
            "benefit": [],
            "harmful_level": 1,
            "comment": ""
        }
    }
    console.log(info)
    var li = document.createElement("li");
    li.classList.add("list-group-item")
    li.classList.add("d-flex")
    li.classList.add("justify-content-between")
    li.classList.add("align-items-start")
    li.classList.add(HARM_LEVEL_CLASS[info['harmful_level']])
    li.classList.add(info['harmful_level'])
    var card = document.createElement("div")
    card.classList.add("ms-2")
    card.classList.add("me-auto")
    var content = document.createElement("div")
    content.classList.add("fw-bold")
    content.innerText = ingredient
    card.append(content)
    if (info['harmful_level'] == 0) {
        card.innerHTML += `${ingredient} is good for ${info['benefit'].join(', ')}`
    } else {
        card.innerHTML += info['comment']
    }
    li.append(card);
    return li
}
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function queryIngredient(ingredient) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", `http://127.0.0.1:5000/query/${encodeURIComponent(ingredient)}`, false );
    console.log(xmlHttp)
    xmlHttp.send( null );
    return JSON.parse(xmlHttp.response);
}

chrome.storage.sync.get(["ingredients"], data => {
    var list = document.getElementById("ingredients")
    list.innerHTML = ""
    var tiles = data["ingredients"].map((ing) => createIngredientTile(ing))
    tiles.sort((tile1, tile2) => tileToHarmLevel(tile2) - tileToHarmLevel(tile1))
    tiles.map((tile) => list.append(tile))
});

chrome.runtime.onMessage.addListener(
    function (msg, sender, sendResponse) {
        console.log('receive', msg);
        for (const key in msg) {
            if (key == "ingredients") {
                var list = document.getElementById("ingredients")
                list.innerHTML = ""
                var tiles = msg[key].map((ing) => createIngredientTile(ing))
                console.log(tiles)
                tiles.sort((tile1, tile2) => tileToHarmLevel(tile2) - tileToHarmLevel(tile1))
                tiles.map((tile) => list.append(tile))
            }
        }
        sendResponse({ farewell: "goodbye" });
    }
);