var links = document.documentElement.innerHTML.match(/href="(.+?)".*?/gm);
var absoluteUrls = [];

if (links) {
    links.forEach(function (link) {
        // Извлекаем значение атрибута href
        var hrefValue = link.match(/href="(.+?)"/)[1];

        // Создаем абсолютный URL
        var absoluteUrl = new URL(hrefValue, window.location.href).href;

        // Добавляем абсолютный URL в массив
        absoluteUrls.push(absoluteUrl);
    });
} else {
    console.log('Ссылок не найдено');
}

// Теперь absoluteUrls содержит массив абсолютных URL-ов
console.log(absoluteUrls);