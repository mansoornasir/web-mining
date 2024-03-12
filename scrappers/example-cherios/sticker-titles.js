const axios = require("axios");
const cheerio = require("cheerio");

// URL to be scraped
const targetUrl = "https://doggystickers.vercel.app/";

// Make a request to the webpage using axios
axios
    .get(targetUrl)
    .then((response) => {
        // Load the HTML content into Cheerio
        const $ = cheerio.load(response.data);

        // Use Cheerio selectors to extract information
        $("div.font-primary.text-2xl").each((index, element) => {
            // Extract and print the title of each link
            const linkTitle = $(element).text();
            console.log(`Link Title: ${linkTitle}`);
        });
        // console.log(response.data)
    })
    .catch((error) => {
        console.error(`Error fetching ${targetUrl}: ${error.message}`);
    });
