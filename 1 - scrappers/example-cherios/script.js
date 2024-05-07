const axios = require("axios");
const cheerio = require("cheerio");

// URL to be scraped
const targetUrl = "https://example.com";

// Make a request to the webpage using axios
axios
    .get(targetUrl)
    .then((response) => {
        // Load the HTML content into Cheerio
        const $ = cheerio.load(response.data);

        // Use Cheerio selectors to extract information
        $("a").each((index, element) => {
            // Extract and print the title of each link
            const linkTitle = $(element).text();
            console.log(`Link Title: ${linkTitle}`);
        });
    })
    .catch((error) => {
        console.error(`Error fetching ${targetUrl}: ${error.message}`);
    });
