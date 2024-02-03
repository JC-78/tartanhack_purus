chrome.storage.onChanged.addListener(async function (changes, namespace) {
    var msg = {};
    for (let [key, { oldValue, newValue }] of Object.entries(changes)) {
        msg[key] = newValue
    }
    console.log(msg)
    chrome.runtime.sendMessage(msg, (res)=>console.log(res));
});