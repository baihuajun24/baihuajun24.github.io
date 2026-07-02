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
    const flip = () => {
        const flipped = playerCard.classList.toggle('flipped');
        playerCard.setAttribute('aria-pressed', flipped);
    };
    playerCard.addEventListener('click', flip);
    playerCard.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            flip();
        }
    });

    // Live EP stat from the podcast feed; the hardcoded number is the fallback.
    fetch('podcast/feed.xml')
        .then(res => res.ok ? res.text() : Promise.reject(new Error('HTTP ' + res.status)))
        .then(text => {
            const items = new DOMParser().parseFromString(text, 'text/xml').querySelectorAll('item');
            if (items.length) {
                document.querySelectorAll('.fut-ep').forEach(el => el.textContent = items.length);
            }
        })
        .catch(() => { /* keep the snapshot number */ });
}
