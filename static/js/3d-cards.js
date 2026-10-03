document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".dashboard-card");

    cards.forEach((card) => {
        card.addEventListener("mousemove", (event) => {
            const rect = card.getBoundingClientRect();

            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -7;
            const rotateY = ((x - centerX) / centerX) * 7;

            card.style.transform =
                "perspective(800px) rotateX(" +
                rotateX +
                "deg) rotateY(" +
                rotateY +
                "deg) translateY(-7px)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform =
                "perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0)";
        });
    });
});
