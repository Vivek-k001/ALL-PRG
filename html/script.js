document.addEventListener("DOMContentLoaded", function () {
    const lines = [
        "so imma love you every night like it's the last night",
        "like it's the last night",
        "if the world is ending",
        "i would wanna be next to you",
        "if the party was over",
        "and our time on earth was through",
        "i would hold you just for a while",
        "and die with a smile",
        "if the world was ending",
        "i would wanna be next to you",
        "right next to you",
    ];

    const delays = [600, 700, 1000, 4600, 1000, 3600, 1700, 2000, 900, 1200, 500];

    let container = document.getElementById("lyrics-container");

    async function displayLyrics() {
        for (let i = 0; i < lines.length; i++) {
            let line = lines[i];
            let p = document.createElement("p");
            p.classList.add("lyrics-line");
            container.appendChild(p);

            for (let char of line) {
                let span = document.createElement("span");
                span.textContent = char;
                p.appendChild(span);
                await new Promise(resolve => setTimeout(resolve, 100)); // delay per character
            }

            // Add delay between lines
            await new Promise(resolve => setTimeout(resolve, delays[i]));

            // Make the line visible after it's fully printed
            let spans = p.querySelectorAll('span');
            for (let span of spans) {
                span.style.opacity = 1;
            }
        }
    }

    displayLyrics();
});
