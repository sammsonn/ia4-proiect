// Modify the suggestions to include image file names and links
const suggestions = [
    { text: "APARAT KEBAB-SHAORMA ELECTRIC 2 X 5 ARZATOARE KLG172T", image: "img/KLG172T.jpeg", link: "APARAT KEBAB-SHAORMA ELECTRIC 2 X 5 ARZATOARE KLG172T.html" },
    { text: "APARAT KEBAB-SHAORMA ELECTRIC 2 X 5 ARZATOARE KLG172T", image: "img/KLG172T.jpeg", link: "APARAT KEBAB-SHAORMA ELECTRIC 2 X 5 ARZATOARE KLG172T.html" },
    { text: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG161", image: "img/KLG161.jpeg", link: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG161.html" },
    { text: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG231HG", image: "img/KLG231HG.jpeg", link: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG231HG.html" },
    { text: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG231HG", image: "img/KLG231HG.jpeg", link: "APARAT KEBAB-SHAORMA ELECTRIC 4 ARZATOARE KLG231HG.html" },
    { text: "APARAT KEBAB-SHAORMA PE GAZ 2 X 4 ARZATOARE KLG224T", image: "img/KLG224T.jpeg", link: "APARAT KEBAB-SHAORMA PE GAZ 2 X 4 ARZATOARE KLG224T.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC 6 pizza Ø35 cm E6351W", image: "img/E6351W.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC 6 pizza Ø35 cm E6351W.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC 6+6 pizza Ø35 cm E6352D", image: "img/E6352D.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC 6+6 pizza Ø35 cm E6352D.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC 6+6 pizza Ø35 cm E6352W", image: "img/E6352W.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC 6+6 pizza Ø35 cm E6352W.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 4 pizza Ø30 cm E4301AB", image: "img/E4301AB.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 4 pizza Ø30 cm E4301AB.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 4 pizza Ø33 cm E4331AB", image: "img/E4331AB.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 4 pizza Ø33 cm E4331AB.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 6 pizza Ø30 cm E6301WAB", image: "img/E6301WAB.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 6 pizza Ø30 cm E6301WAB.html" },
    { text: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 9 pizza Ø35 cm E9351A", image: "img/E9351A.jpeg", link: "CUPTOR PENTRU PIZZA ELECTRIC-ANALOG CONTROL 9 pizza Ø35 cm E9351A.html" },
    { text: "FRITEUZA DUBLA ELECTRICA 11LT+11L F6060E", image: "img/F6060E.jpeg", link: "FRITEUZA DUBLA ELECTRICA 11LT+11L F6060E .html" },
    { text: "FRITEUZA DUBLA ELECTRICA DE BANC F8070E", image: "img/F8070E.jpeg", link: "FRITEUZA DUBLA ELECTRICA DE BANC F8070E .html" },
    { text: "FRITEUZA DUBLA ELECTRICA PE SUPORT 12L+12L FCS8070E" ,image: "img/FCS8070E.jpeg", link: "FRITEUZA DUBLA ELECTRICA PE SUPORT 12L+12L FCS8070E.html" },
    { text: "FRITEUZA ELECTRICA PE SUPORT 12L FCS4070E" ,image: "img/FCS4070E.jpeg", link: "FRITEUZA ELECTRICA PE SUPORT 12L FCS4070E.html" },
    { text: "FRITEUZA MONOBLOC ELECTRICA FCS4090E", image: "img/FCS4090E.jpeg", link: "FRITEUZA MONOBLOC ELECTRICA FCS4090E.html" },
    { text: "HOTA CU MOTOR PENTRU CUPTOR PIZZA 906 X 1115 X 360 MM KALITEGAZ PHME4301A", image: "PHME4301A.jpeg", link: "HOTA CU MOTOR PENTRU CUPTOR PIZZA 906 X 1115 X 360 MM KALITEGAZ PHME4301A.html" },
    { text: "HOTA CUPTOR PIZZA 906 X 900 X 147 MM KALITEGAZ PHE4301A", image: "PHE4301A.jpeg", link: "HOTA CUPTOR PIZZA 906 X 900 X 147 MM KALITEGAZ PHE4301A.html" },
    { text: "HOTA DIN INOX PROFESIONALA CUBICA 1250X1100 MM CU VENTILATOR HCBM11-12", image: "img/HCBM11-12.jpg", link: "HOTA DIN INOX PROFESIONALA CUBICA 1250X1100 MM CU VENTILATOR HCBM11-12.html" },
    { text: "HOTA DIN INOX PROFESIONALA CUBICA 2000X1100 MM CU VENTILATOR HCBI11-20", image: "img/HCBI11-20.jpg", link: "HOTA DIN INOX PROFESIONALA CUBICA 2000X1100 MM CU VENTILATOR HCBI11-20.html" },
    { text: "HOTA DIN INOX PROFESIONALA CUBICA 2500X1100 MM CU VENTILATOR HCBM11-25", image: "img/HCBM11-25.jpg", link: "HOTA DIN INOX PROFESIONALA CUBICA 2500X1100 MM CU VENTILATOR HCBM11-25.html" },
    { text: "MASA DIN INOX CU SPALATOR 1000X600X850 MM MS6P-10-1404025", image: "img/MS6P-10-1404025.jpg", link: "MASA DIN INOX CU SPALATOR 1000X600X850 MM MS6P-10-1404025.html" },   
    { text: "MASA DIN INOX CU SPALATOR 1200X600X850 MM MS6P-12-1504025", image: "img/MS6P-12-1504025.jpg", link: "MASA DIN INOX CU SPALATOR 1200X600X850 MM MS6P-12-1504025.html" },
    { text: "MASA DIN INOX CU SPALATOR 1200X700X850 MM MS7P-12-1505030", image: "img/MS7P-12-1505030.jpg", link: "MASA DIN INOX CU SPALATOR 1200X700X850 MM MS7P-12-1505030.html" },
    { text: "MASA DIN INOX CU SPALATOR 1400X700X850 MM MS7P-14-1505030", image: "img/MS7P-14-1505030.jpg", link: "MASA DIN INOX CU SPALATOR 1400X700X850 MM MS7P-14-1505030.html" },   
    { text: "MASA DIN INOX CU SPALATOR 1800X700X850 MM MS7P-18-1505030", image: "img/MS7P-18-1505030.jpg", link: "MASA DIN INOX CU SPALATOR 1800X700X850 MM MS7P-18-1505030.html" },
    { text: "MASA DIN INOX TIP DULAP CU USI GLISANTE, SERIA 600 MM MD6", image: "img/MD6.jpg", link: "MASA DIN INOX TIP DULAP CU USI GLISANTE, SERIA 600 MM MD6.html" },    
    { text: "MASA DIN INOX TIP DULAP CU USI GLISANTE, SERIA 700 MM MD7", image: "img/MD7.jpg", link: "MASA DIN INOX TIP DULAP CU USI GLISANTE, SERIA 700 MM MD7.html" }
////////////
]

// Getting all required elements
const searchInput = document.querySelector(".searchInput");
const input = searchInput.querySelector("input");
const resultBox = searchInput.querySelector(".resultBox");
const icon = searchInput.querySelector(".icon");
let linkTag = searchInput.querySelector("a");
let webLink;

// If the user presses any key and releases
input.onkeyup = (e) => {
    let userData = e.target.value.toLowerCase(); // User entered data
    let emptyArray = [];
    if (userData) {
        emptyArray = suggestions.filter((item) => {
            return item.text.toLowerCase().startsWith(userData);
        });

        emptyArray = emptyArray.map((item) => {
            // Wrap the entire suggestion content in an <a> tag
            return `<li><a href="${item.link}" target="_blank" class="suggestion-link">
                <div class="suggestion-content">
                    ${item.text}
                    <img class="suggestion-image" src="${item.image}" alt="${item.text} Image">
                </div>
            </a></li>`;
        });
        

        searchInput.classList.add("active"); // Show autocomplete box
        showSuggestions(emptyArray);
        let allList = resultBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            // Adding onclick attribute in all li tags
            allList[i].setAttribute("onclick", "select(this)");
        }
    } else {
        searchInput.classList.remove("active"); // Hide autocomplete box
    }
}

function showSuggestions(list) {
    let listData;
    if (!list.length) {
        userValue = inputBox.value;
        listData = '<li>' + userValue + '</li>';
    } else {
        listData = list.join('');
    }
    resultBox.innerHTML = listData;
}
