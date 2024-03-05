const Crawler = require('crawler');

// Create a new instance of the crawler
const crawler = new Crawler();

// URL to be crawled
const targetUrl = 'https://example.com';

// Use the queue method to add a URL to the list of pages to crawl
crawler.queue({
  uri: targetUrl,
  callback: (error, res, done) => {
    if (error) {
      console.error(error);
    } else {
      // Use jQuery-style selector to extract information from the page
      const pageTitle = res.$('title').text();
    //   console.log(`Title of ${targetUrl}: ${pageTitle}`);
    console.log(res.body)
    }
    done();
  },
});

// Run the crawler
crawler.on('drain', () => {
  console.log('Crawling finished!');
});