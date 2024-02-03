function init() {
    chrome.storage.sync.clear()
    var ingredients = parseIngredientAmazon(getIngredientsAmazon());
    console.log(ingredients);
    syncIngredient(ingredients);
}

// Amazon ingredients of cosmetic would be in important information section
function getIngredientsAmazon() {
    var important_infos = document.getElementById("important-information").getElementsByTagName("div");
    var ingredients;
    for (var i = 0; i < important_infos.length; i++) {
        if (important_infos[i].getElementsByTagName('h4')[0].innerText == "Ingredients") {
            ingredients = [...important_infos[i].getElementsByTagName('p')].map((p) => p.innerText).join(" ");
            break;
        }
    }
    return ingredients
}

function parseIngredientAmazon(raw_text) {
    var ingredients = raw_text.toLowerCase().split(',').map((ingredient) => ingredient.trim());
    return ingredients;
}

function syncIngredient(ingredients) {
    var toStorage = {"ingredients": ingredients}
    chrome.storage.sync.set(toStorage, () => {console.log("set done")});
}

init();
