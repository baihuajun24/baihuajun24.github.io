// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Reveal sections on scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.6s ease-out';
    observer.observe(section);
});

// Profile photo ⇄ player-card easter egg
const playerCard = document.getElementById('player-card');
if (playerCard) {
    const cardFront = playerCard.querySelector('.card-front');
    const cardBack = playerCard.querySelector('.card-back');
    const flip = () => {
        const flipped = playerCard.classList.toggle('flipped');
        playerCard.setAttribute('aria-pressed', flipped);
        if (cardFront && cardBack) {
            cardFront.setAttribute('aria-hidden', flipped);
            cardBack.setAttribute('aria-hidden', !flipped);
        }
    };
    playerCard.addEventListener('click', flip);
    playerCard.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            flip();
        }
    });
}
