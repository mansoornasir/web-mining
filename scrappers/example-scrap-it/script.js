const scrapeIt = require("scrape-it")

// Promise interface
scrapeIt("https://ionicabizau.net", {
    title: ".header h1"
  , desc: ".header h2"
  , avatar: {
        selector: ".header img"
      , attr: "src"
    }
}).then(({ data, status }) => {
    console.log(`Status Code: ${status}`)
    console.log(data)
});


// Async-Await
(async () => {
    const { data } = await scrapeIt("https://ionicabizau.net", {
        // Fetch the articles
        articles: {
            listItem: ".article"
          , data: {

                // Get the article date and convert it into a Date object
                createdAt: {
                    selector: ".date"
                  , convert: x => new Date(x)
                }

                // Get the title
              , title: "a.article-title"

                // Nested list
              , tags: {
                    listItem: ".tags > span"
                }

                // Get the content
              , content: {
                    selector: ".article-content"
                  , how: "html"
                }

                // Get attribute value of root listItem by omitting the selector
              , classes: {
                    attr: "class"
                }
            }
        }

        // Fetch the blog pages
      , pages: {
            listItem: "li.page"
          , name: "pages"
          , data: {
                title: "a"
              , url: {
                    selector: "a"
                  , attr: "href"
                }
            }
        }

        // Fetch some other data from the page
      , title: ".header h1"
      , desc: ".header h2"
      , avatar: {
            selector: ".header img"
          , attr: "src"
        }
    })
    console.log(data)
    // { articles:
    //    [ { createdAt: Mon Mar 14 2016 00:00:00 GMT+0200 (EET),
    //        title: 'Pi Day, Raspberry Pi and Command Line',
    //        tags: [Object],
    //        content: '<p>Everyone knows (or should know)...a" alt=""></p>\n',
    //        classes: [Object] },
    //      { createdAt: Thu Feb 18 2016 00:00:00 GMT+0200 (EET),
    //        title: 'How I ported Memory Blocks to modern web',
    //        tags: [Object],
    //        content: '<p>Playing computer games is a lot of fun. ...',
    //        classes: [Object] },
    //      { createdAt: Mon Nov 02 2015 00:00:00 GMT+0200 (EET),
    //        title: 'How to convert JSON to Markdown using json2md',
    //        tags: [Object],
    //        content: '<p>I love and ...',
    //        classes: [Object] } ],
    //   pages:
    //    [ { title: 'Blog', url: '/' },
    //      { title: 'About', url: '/about' },
    //      { title: 'FAQ', url: '/faq' },
    //      { title: 'Training', url: '/training' },
    //      { title: 'Contact', url: '/contact' } ],
    //   title: 'Ionică Bizău',
    //   desc: 'Web Developer,  Linux geek and  Musician',
    //   avatar: '/images/logo.png' }
})()