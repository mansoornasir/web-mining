const axios = require("axios");
const cheerio = require("cheerio");
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

// URL to be scraped
const targetUrl = "https://doggystickers.vercel.app/";

// Make a request to the webpage using axios
var stickersData = []
const csvWriter = createCsvWriter({
    path: 'output.csv',
    header: [
        { title: 'Sticker Name' },
    ]
});
axios
    .get(targetUrl)
    .then((response) => {
        // Load the HTML content into Cheerio
        const $ = cheerio.load(response.data);

        // Use Cheerio selectors to extract information
        $("div.font-primary.text-2xl").each((index, element) => {
            // Extract and print the title of each link
            const name = $(element).text();
            stickersData.push({ title: name })
            
        });
        console.log(stickersData)
    })
    .catch((error) => {
        console.error(`Error fetching ${targetUrl}: ${error.message}`);
    });
    
    csvWriter.writeRecords(stickersData)       // returns a promise
                .then(() => {
                    console.log('...Done');
                });