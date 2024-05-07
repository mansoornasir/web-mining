const scrapeIt = require("scrape-it")

// Promise interface
scrapeIt("https://doggystickers.vercel.app/", {
    title: "img"
}).then(({ data, status }) => {
    console.log(`Status Code: ${status}`)
    console.log(data)
});
